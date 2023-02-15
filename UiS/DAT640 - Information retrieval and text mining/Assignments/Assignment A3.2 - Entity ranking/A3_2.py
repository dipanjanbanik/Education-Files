import abc
import time
from typing import Any, Dict, List
import math
from elasticsearch import Elasticsearch
from matplotlib import ft2font

_DEFAULT_FIELD = "body"


class Entity:
    def __init__(self, doc_id: str, stats: Dict[str, Dict[str, Any]]):
        """Representation of an entity.

        Args:
          doc_id: Document id
          stats: Term vector stats from elasticsearch. Keys are field and
            values are term and field statistics.
        """
        self.doc_id = doc_id
        self._stats = stats
        self._terms = {}

    def term_stats(self, term: str, field: str = _DEFAULT_FIELD) -> Dict[str, Any]:
        """Term statistics including term frequency and total term frequency."""
        return self._stats[field]["terms"].get(term)

    def field_stats(self, field: str = _DEFAULT_FIELD):
        """Field statistics including sum of total term frequency."""
        return self._stats[field]["field"]

    def terms(self, field: str = _DEFAULT_FIELD) -> List[str]:
        """Reconstructed document field from indexed positional information."""
        if field in self._terms:
            return self._terms[field]

        pos = {
            token["position"]: term
            for term, tinfo in self._stats[field]["terms"].items()
            for token in tinfo["tokens"]
        }
        self._terms[field] = [None] * (max(pos.keys()) + 1)
        for p, term in pos.items():
            self._terms[field][p] = term
        return self._terms[field]

    def length(self, field: str = _DEFAULT_FIELD) -> int:
        """Length of the document field."""
        return sum(term["term_freq"] for term in self._stats[field]["terms"].values())


class ElasticsearchCollection:
    def __init__(self, index_name):
        """Interface to an Elasticsearch index.

        Args:
          index_name: Name of the index to use.
        """
        self._index_name = index_name
        self.es = Elasticsearch()

    def baseline_retrieval(
        self, query: str, k: int = 100, field: str = None
    ) -> List[str]:
        """Performs baseline retrieval on index.

        Args:
          query: A string of text, space separated terms.
          k: Number of documents to return.
          field: If specified, match only on the specified field.

        Returns:
          A list of entity IDs as strings, up to k of them, in descending
          order of scores.
        """
        res = self.es.search(
            index=self._index_name,
            q=query if not field else None,
            query={"match": {field: query}} if field else None,
            size=k,
        )
        return [x["_id"] for x in res["hits"]["hits"]]

    def get_query_terms(self, text: str) -> List[str]:
        """Analyzes text with the same pipeline that was used for indexing
        documents. It returns None in place of a term if it was removed (e.g.,
        using stopword removal).

        Args:
          text: Text to analyze.

        Returns:
          List of terms.
        """
        tokens = self.es.indices.analyze(index=self._index_name, body={"text": text})[
            "tokens"
        ]
        query_terms = [None] * (
            max(tokens, key=lambda x: x["position"])["position"] + 1
        )
        for token in tokens:
            query_terms[token["position"]] = token["token"]
        return query_terms

    def get_document(self, doc_id: str) -> Entity:
        """Generates entity representation given document id."""
        tv = self.es.termvectors(
            index=self._index_name,
            id=doc_id,
            term_statistics=True,
        )["term_vectors"]

        return Entity(
            doc_id,
            stats={
                field: {
                    "terms": tv[field]["terms"],
                    "field": tv[field]["field_statistics"],
                }
                for field in tv
            },
        )

    def index(self, collection: Dict[str, Any], settings: Dict[str, Any]):
        if self.es.indices.exists(index=self._index_name):
            self.es.indices.delete(index=self._index_name)
        self.es.indices.create(index=self._index_name, mappings=settings)
        for (doc_id, doc) in collection.items():
            self.es.index(document=doc, id=doc_id, index=self._index_name)
        time.sleep(10)


class Scorer(abc.ABC):
    def __init__(
        self,
        collection: ElasticsearchCollection,
        feature_weights=[0.85, 0.1, 0.05],
        mu: float = 100,
        window: int = 3,
    ):
        """Interface for the scorer class.

        Args:
          collection: Collection of documents. Needed to calculate document
            statistical information.
          feature_weights: Weights associated with each feature function
          mu: Smoothing parameter
          window: Window for unordered feature function.
        """
        if not sum(feature_weights) == 1:
            raise ValueError("Feature weights should sum to 1.")

        self.collection = collection
        self.feature_weights = feature_weights
        self.mu = mu
        self.window = window

    def score_collection(self, query: str, k: int = 100):
        """Scores all documents in the collection using document-at-a-time query
        processing.

        Args:
          query: Sequence (list) of query terms.
          k: Number of documents to return

        Returns:
          Dict with doc_ids as keys and retrieval scores as values. (It may be
          assumed that documents that are not present in this dict have a
          retrival score of 0.)
        """
        # TODO
        documents: List[Entity] = ...
        query_terms: List[str] = ...

        lT, lO, lU = self.feature_weights
        return {
            doc.doc_id: (
                lT * self.unigram_matches(query_terms, doc)
                + lO * self.ordered_bigram_matches(query_terms, doc, documents)
                + lU * self.unordered_bigram_matches(query_terms, doc, documents)
            )
            for doc in documents
        }

    @abc.abstractmethod
    def unigram_matches(self, query_terms: List[str], doc: Entity) -> float:
        """Returns unigram matches based on smoothed entity language model.

        Args:
          query_terms: List of query terms.
          doc: Entity for which we are calculating the score.

        Returns:
          Score for unigram matches for document
        """
        raise NotImplementedError

    @abc.abstractmethod
    def ordered_bigram_matches(
        self, query_terms: List[str], doc: Entity, documents: List[Entity]
    ) -> float:
        """Returns ordered bigram matches based on smoothed entity language
        model.

        Args:
          query_terms: List of query terms
          doc: Entity we wish to score
          documents: List of all entities in the collection

        Returns:
          Score for ordered bigram matches for document
        """
        raise NotImplementedError

    @abc.abstractmethod
    def unordered_bigram_matches(
        self, query_terms: List[str], doc: Entity, documents: List[Entity]
    ) -> float:
        """Returns unordered bigram matches based on smoothed entity language
        model.

        Args:
          query_terms: List of query terms
          doc: Entity we wish to score
          documents: List of all entities in the collection

        Returns:
          Score for unordered bigram matches for document
        """
        raise NotImplementedError


class SDMScorer(Scorer):
    def unigram_matches(self, query_terms: List[str], doc: Entity) -> float:
        """Returns unigram matches based on smoothed entity language model.

        Args:
          query_terms: List of query terms.
          doc: Entity for which we are calculating the score.

        Returns:
          Score for unigram matches for document
        """
        # TODO
        ...
        docLength = doc.length()
        u = self.mu
        totalFrequencySum = doc.field_stats()["sum_ttf"]
        ft = p = 0
        for term in query_terms:
            if doc.term_stats(term) == None:
                continue
            else:
                totalTermFrequencySum = doc.term_stats(term)["ttf"]
                termFrequency = doc.term_stats(term)["term_freq"]  # c_q_e
                if totalFrequencySum < 0:
                    p = 0
                else:
                    p = totalTermFrequencySum / totalFrequencySum
                formula = (termFrequency + (u * p)) / (docLength + u)
                if formula < 0:
                    ft = 0
                else:
                    ft += math.log(formula)
        return ft

    def ordered_bigram_matches(
        self,
        query_terms: List[str],
        doc: Entity,
        documents: List[Entity],
    ) -> float:
        """Returns ordered bigram matches based on smoothed entity language
        model.

        Args:
          query_terms: List of query terms
          doc: Entity we wish to score
          documents: List of all entities in the collection

        Returns:
          Score for ordered bigram matches for document
        """
        # TODO
        ...
        ft = total_freq = 0
        bigram_list = list(zip(query_terms[:-1], query_terms[1:]))
        u = self.mu

        def innerFunc(term):
            term_freq = sum(
                [
                    1
                    for i in bigram_list
                    for c in range(len(terms) - 1)
                    if terms[c] == i[0] and terms[c + 1] == i[1]
                ]
            )
            return term_freq

        terms = doc.terms()

        term_freq = innerFunc(terms)
        total_length = doc.field_stats()["sum_ttf"]
        length = doc.length()
        totalFrequencySum = doc.field_stats()["sum_ttf"]
        docLength = doc.length()
        for col in documents:
            t = col.terms()
            total_freq += sum(
                [
                    1
                    for i in bigram_list
                    for c in range(len(t) - 1)
                    if t[c] == i[0] and t[c + 1] == i[1]
                ]
            )

        # p = total_freq / total_length if total_length > 0 else 0
        # tmp = (term_freq + self.mu * (p)) / (length + self.mu)
        # score += math.log(tmp) if tmp > 0 else 0

        if total_freq < 0:
            p = 0
        else:
            p = total_freq / totalFrequencySum
        formula = (term_freq + (u * p)) / (docLength + u)
        if formula < 0:
            ft = 0
        else:
            ft += math.log(formula)

        return ft

    def unordered_bigram_matches(
        self,
        query_terms: List[str],
        doc: Entity,
        documents: List[Entity],
    ) -> float:
        """Returns unordered bigram matches based on smoothed entity language
        model.

        Args:
          query_terms: List of query terms
          doc: Entity we wish to score
          documents: List of all entities in the collection

        Returns:
          Score for unordered bigram matches for document
        """
        # TODO
        ...


class FSDMScorer(Scorer):
    def __init__(
        self,
        collection: ElasticsearchCollection,
        feature_weights=[0.85, 0.1, 0.05],
        mu: float = 100,
        window: int = 3,
        fields: List[str] = ["title", "body", "anchors"],
        field_weights: List[float] = [0.2, 0.7, 0.1],
    ):
        """Fielded version of an SDM scorer.

        Args:
          collection: Collection of documents. Needed to calculate document
            statistical information.
          feature_weights: Weights associated with each feature function
          mu: Smoothing parameter
          window: Window for unordered feature function.
          fields: A list of fields to use for the calculating the score
          field_weights: A list of weights to use for each field.
        """
        super().__init__(collection, feature_weights, mu, window)
        assert len(fields) == len(field_weights)
        self.fields = fields
        self.field_weights = field_weights

    def unigram_matches(self, query_terms: List[str], doc: Entity) -> float:
        """Returns unigram matches based on smoothed entity language model.

        Args:
          query_terms: List of query terms.
          doc: Entity for which we are calculating the score.

        Returns:
          Score for unigram matches for document
        """
        # TODO
        ...

    def ordered_bigram_matches(
        self, query_terms: List[str], doc: Entity, documents: List[Entity]
    ) -> float:
        """Returns ordered bigram matches based on smoothed entity language
        model.

        Args:
          query_terms: List of query terms
          doc: Entity we wish to score
          documents: List of all entities in the collection

        Returns:
          Score for ordered bigram matches for document
        """
        # TODO
        ...

    def unordered_bigram_matches(
        self, query_terms: List[str], doc: Entity, documents: List[Entity]
    ) -> float:
        """Returns unordered bigram matches based on smoothed entity language
        model.

        Args:
          query_terms: List of query terms
          doc: Entity we wish to score
          documents: List of all entities in the collection

        Returns:
          Score for unordered bigram matches for document
        """
        # TODO
        ...
