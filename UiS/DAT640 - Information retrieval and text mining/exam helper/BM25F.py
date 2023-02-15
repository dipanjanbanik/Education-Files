import abc
from collections import Counter
from collections import UserDict as DictClass
from collections import defaultdict
from typing import Dict, List
import math
import copy

CollectionType = Dict[str, Dict[str, List[str]]]


class DocumentCollection(DictClass):
    """Document dictionary class with helper functions."""

    def total_field_length(self, field: str) -> int:
        """Total number of terms in a field for all documents."""
        return sum(len(fields[field]) for fields in self.values())

    def avg_field_length(self, field: str) -> float:
        """Average number of terms in a field across all documents."""
        return self.total_field_length(field) / len(self)

    def get_field_documents(self, field: str) -> Dict[str, List[str]]:
        """Dictionary of documents for a single field."""
        return {
            doc_id: doc[field] for (doc_id, doc) in self.items() if field in doc
        }

    def avg_fields_length(self, field: str) -> float:
        """Average number of terms in a field across all documents."""
        totlCount = 0
        for j,k in self.items():
            for i,p in k.items():
                totlCount+=len(p)
        return self.total_field_length(field) / totlCount

class Scorer(abc.ABC):
    def __init__(
        self,
        collection: DocumentCollection,
        index: CollectionType,
        field: str = None,
        fields: List[str] = None,
    ):
        """Interface for the scorer class.

        Args:
            collection: Collection of documents. Needed to calculate document
                statistical information.
            index: Index to use for calculating scores.
            field (optional): Single field to use in scoring.. Defaults to None.
            fields (optional): List of fields to use in scoring. Defaults to
                None.

        Raises:
            ValueError: Either field or fields need to be specified.
        """
        self.collection = collection
        self.index = index

        if not (field or fields):
            raise ValueError("Either field or fields have to be defined.")

        self.field = field
        self.fields = fields

        # Score accumulator for the query that is currently being scored.
        self.scores = None

    def score_collection(self, query_terms: List[str]):
        """Scores all documents in the collection using term-at-a-time query
        processing.

        Params:
            query_term: Sequence (list) of query terms.

        Returns:
            Dict with doc_ids as keys and retrieval scores as values.
            (It may be assumed that documents that are not present in this dict
            have a retrival score of 0.)
        """
        self.scores = defaultdict(float)  # Reset scores.
        query_term_freqs = Counter(query_terms)

        for term, query_freq in query_term_freqs.items():
            self.score_term(term, query_freq)

        return self.scores

    @abc.abstractmethod
    def score_term(self, term: str, query_freq: int):
        """Scores one query term and updates the accumulated document retrieval
        scores (`self.scores`).

        Params:
            term: Query term
            query_freq: Frequency (count) of the term in the query.
        """
        raise NotImplementedError

class ScorerBM25F(Scorer):
    def __init__(
        self,
        collection: DocumentCollection,
        index: CollectionType,
        fields: List[str] = ["title", "body"],
        field_weights: List[float] = [0.2, 0.8],
        bi: List[float] = [0.75, 0.75],
        k1: float = 1.2,
    ) -> None:
        super(ScorerBM25F, self).__init__(collection, index, fields=fields)
        self.field_weights = field_weights
        self.bi = bi
        self.k1 = k1

    def findBI(self,doc):
        B_i={}
        field_bi_dis = dict(zip(self.fields, self.bi))
        for f,f_val in self.collection[doc].items():
            ttL_field_len = len(f_val)
            avg_field_len = self.collection.avg_field_length(f)
            B_i[f] = (1 - field_bi_dis[f]) + (field_bi_dis[f] * (ttL_field_len/avg_field_len))
        return B_i

    def score_term(self, term: str, query_freq: int) -> None:
        i=0
        B_i={}
       
        for j,k in self.collection.items():
            B_i = self.findBI(j)
            final_ctd = 0
            for i,(field, terms) in enumerate(k.items()):
                terms_count = Counter(terms)
                ctd = self.field_weights[i] * (terms_count[term] / B_i[field])
                final_ctd = final_ctd + ctd
            
            # Calculate IDF
            N = len(self.collection)
            t_val = 0
            for l,o in self.collection.items():
                if term in o['body']:
                    t_val = t_val + 1
            
            n_t = t_val
            idf = math.log(N/n_t)

            score = (final_ctd / (self.k1 + final_ctd)) * idf

            if self.scores[j]:
                self.scores[j] += score
            else:
                self.scores[j] = score


collection_2 = DocumentCollection(
        {
            "d1": {
                "title": ["t1"],
                "body": ["t1", "t2", "t3", "t1", "t3"],
                "anchors": ["t2", "t2"],
            },
            "d2": {
                "title": ["t4", "t5"],
                "body": ["t1", "t3", "t4", "t4", "t4", "t5"],
                "anchors": ["t5", "t3"],
            },
            "d3": {
                "title": ["t1", "t3", "t5"],
                "body": ["t1", "t1", "t5", "t3", "t5", "t3", "t3"],
                "anchors": ["t1", "t1", "t5"],
            },
        }
    )

index_2 =  {
        "title": {
            "t1": [("d1", 1), ("d3", 1)],
            "t3": [("d3", 1)],
            "t4": [("d2", 1)],
            "t5": [("d2", 1), ("d3", 1)],
        },
        "body": {
            "t1": [("d1", 2), ("d2", 1), ("d3", 2)],
            "t2": [("d1", 1)],
            "t3": [("d1", 2), ("d2", 1), ("d3", 3)],
            "t4": [("d2", 3)],
            "t5": [("d2", 1), ("d3", 2)],
        },
        "anchors": {
            "t1": [("d3", 2)],
            "t2": [("d1", 2)],
            "t3": [("d2", 1)],
            "t5": [("d2", 1), ("d3", 1)],
        },
    }

scorer_bm25f = ScorerBM25F(
        collection_2,
        index_2,
        fields=["title", "body", "anchors"],
        field_weights=[0.1, 0.7, 0.2],
        bi=[0.75, 0.75, 0.75],
    )

scores_bm25f_1 = scorer_bm25f.score_collection(["t2","t4"])
print(scores_bm25f_1["d2"])

scores_bm25f_0 = scorer_bm25f.score_collection(["t3"])
print(scores_bm25f_0["d1"])