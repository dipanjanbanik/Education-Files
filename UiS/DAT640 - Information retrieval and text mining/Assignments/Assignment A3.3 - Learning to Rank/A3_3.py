import json
from typing import Callable, Dict, List, Set, Tuple

import numpy as np
from elasticsearch import Elasticsearch
from collections import defaultdict
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

FIELDS = ["title", "body"]

INDEX_SETTINGS = {
    "properties": {
        "title": {"type": "text", "term_vector": "yes", "analyzer": "english"},
        "body": {"type": "text", "term_vector": "yes", "analyzer": "english"},
    }
}

FEATURES_QUERY = [
    "query_length",
    "query_sum_idf",
    "query_max_idf",
    "query_avg_idf",
]
FEATURES_DOC = ["doc_length_title", "doc_length_body"]
FEATURES_QUERY_DOC = [
    "unique_query_terms_in_title",
    "sum_TF_title",
    "max_TF_title",
    "avg_TF_title",
    "unique_query_terms_in_body",
    "sum_TF_body",
    "max_TF_body",
    "avg_TF_body",
]


def analyze_query(
    es: Elasticsearch, query: str, field: str, index: str = "toy_index"
) -> List[str]:
    """Analyzes a query with respect to the relevant index.

    Args:
        es: Elasticsearch object instance.
        query: String of query terms.
        field: The field with respect to which the query is analyzed.
        index: Name of the index with respect to which the query is analyzed.

    Returns:
        A list of query terms that exist in the specified field among the
        documents in the index.
    """
    tokens = es.indices.analyze(index=index, body={"text": query})["tokens"]
    query_terms = []
    for t in sorted(tokens, key=lambda x: x["position"]):
        # Use a boolean query to find at least one document that contains the
        # term.
        hits = (
            es.search(
                index=index,
                query={"match": {field: t["token"]}},
                _source=False,
                size=1,
            )
            .get("hits", {})
            .get("hits", {})
        )
        doc_id = hits[0]["_id"] if len(hits) > 0 else None
        if doc_id is None:
            continue
        query_terms.append(t["token"])
    return query_terms


def get_doc_term_freqs(
    es: Elasticsearch, doc_id: str, field: str, index: str = "toy_index"
) -> Dict[str, int]:
    """Gets the term frequencies of a field of an indexed document.

    Args:
        es: Elasticsearch object instance.
        doc_id: Document identifier with which the document is indexed.
        field: Field of document to consider for term frequencies.
        index: Name of the index where document is indexed.

    Returns:
        Dictionary of terms and their respective term frequencies in the field
        and document.
    """
    tv = es.termvectors(index=index, id=doc_id, fields=field, term_statistics=True)
    if tv["_id"] != doc_id:
        return None
    if field not in tv["term_vectors"]:
        return None
    term_freqs = {}
    for term, term_stat in tv["term_vectors"][field]["terms"].items():
        term_freqs[term] = term_stat["term_freq"]
    return term_freqs


def extract_query_features(
    query_terms: List[str], es: Elasticsearch, index: str = "toy_index"
) -> Dict[str, float]:
    """Extracts features of a query.

    Args:
        query_terms: List of analyzed query terms.
        es: Elasticsearch object instance.
        index: Name of relevant index on the running Elasticsearch service.
    Returns:
        Dictionary with keys 'query_length', 'query_sum_idf',
            'query_max_idf', and 'query_avg_idf'.
    """
    # TODO

    q_features = {}

    if len(query_terms) == 0:
        q_features["query_length"] = 0
        q_features["query_sum_idf"] = 0
        q_features["query_max_idf"] = 0
        q_features["query_avg_idf"] = 0
        return q_features

    q_features["query_length"] = len(query_terms)

    count_docs_with_term = []
    total_docs_in_index = int(
        es.cat.count(index=index, params={"format": "json"})[0]["count"]
    )

    for query in query_terms:
        res = es.count(index=index, body={"query": {"match": {"body": query}}})["count"]
        count_docs_with_term.append(res)

    q_features["query_sum_idf"] = sum(
        [np.log(total_docs_in_index / freq) for freq in count_docs_with_term]
    )
    q_features["query_max_idf"] = max(
        [np.log(total_docs_in_index / freq) for freq in count_docs_with_term]
    )
    q_features["query_avg_idf"] = np.mean(
        [np.log(total_docs_in_index / freq) for freq in count_docs_with_term]
    )

    return q_features


def extract_doc_features(
    doc_id: str, es: Elasticsearch, index: str = "toy_index"
) -> Dict[str, float]:
    """Extracts features of a document.

    Args:
        doc_id: Document identifier of indexed document.
        es: Elasticsearch object instance.
        index: Name of relevant index on the running Elasticsearch service.

    Returns:
        Dictionary with keys 'doc_length_title', 'doc_length_body'.
    """
    # TODO

    doc_features = {}

    terms = get_doc_term_freqs(es, doc_id, "body", index)
    if terms is None:
        doc_features["doc_length_body"] = 0
    else:
        doc_features["doc_length_body"] = sum(terms.values())

    terms = get_doc_term_freqs(es, doc_id, "title", index)
    if terms is None:
        doc_features["doc_length_title"] = 0
    else:
        doc_features["doc_length_title"] = sum(terms.values())

    return doc_features


def extract_query_doc_features(
    query_terms: List[str],
    doc_id: str,
    es: Elasticsearch,
    index: str = "toy_index",
) -> Dict[str, float]:
    """Extracts features of a query and document pair.

    Args:
        query_terms: List of analyzed query terms.
        doc_id: Document identifier of indexed document.
        es: Elasticsearch object instance.
        index: Name of relevant index on the running Elasticsearch service.

    Returns:
        Dictionary with keys 'unique_query_terms_in_title',
            'unique_query_terms_in_body', 'sum_TF_title', 'sum_TF_body',
            'max_TF_title', 'max_TF_body', 'avg_TF_title', 'avg_TF_body'.
    """
    # TODO

    q_doc_features = {}

    if len(query_terms) == 0:
        q_doc_features["unique_query_terms_in_title"] = 0
        q_doc_features["unique_query_terms_in_body"] = 0
        q_doc_features["sum_TF_body"] = 0
        q_doc_features["max_TF_body"] = 0
        q_doc_features["avg_TF_body"] = 0
        q_doc_features["sum_TF_title"] = 0
        q_doc_features["max_TF_title"] = 0
        q_doc_features["avg_TF_title"] = 0
        return q_doc_features

    terms_title = get_doc_term_freqs(es, doc_id, "title", index)
    terms_body = get_doc_term_freqs(es, doc_id, "body", index)

    def agg(terms_dict, query_terms_list, func):
        freq_list = []
        for term in query_terms_list:
            if term in terms_dict.keys():
                freq_list.append(terms_dict[term])
            else:
                freq_list.append(0)
        return func(freq_list)

    if terms_title is None:
        q_doc_features["sum_TF_title"] = 0
        q_doc_features["max_TF_title"] = 0
        q_doc_features["avg_TF_title"] = 0
    else:
        q_doc_features["sum_TF_title"] = agg(terms_title, query_terms, sum)
        q_doc_features["max_TF_title"] = agg(terms_title, query_terms, max)
        q_doc_features["avg_TF_title"] = agg(terms_title, query_terms, np.mean)

    if terms_body is None:
        q_doc_features["sum_TF_body"] = 0
        q_doc_features["max_TF_body"] = 0
        q_doc_features["avg_TF_body"] = 0
    else:
        q_doc_features["sum_TF_body"] = agg(terms_body, query_terms, sum)
        q_doc_features["max_TF_body"] = agg(terms_body, query_terms, max)
        q_doc_features["avg_TF_body"] = agg(terms_body, query_terms, np.mean)

    # UNIQUE QUERY TERMS
    query_terms = set(query_terms)
    if terms_title is None:
        q_doc_features["unique_query_terms_in_title"] = 0
    else:
        q_doc_features["unique_query_terms_in_title"] = len(
            [t for t in query_terms if t in terms_title.keys()]
        )
    if terms_body is None:
        q_doc_features["unique_query_terms_in_body"] = 0
    else:
        q_doc_features["unique_query_terms_in_body"] = len(
            [t for t in query_terms if t in terms_body.keys()]
        )

    return q_doc_features


def extract_features(
    query_terms: List[str],
    doc_id: str,
    es: Elasticsearch,
    index: str = "toy_index",
) -> List[float]:
    """Extracts query features, document features and query-document features
    of a query and document pair.

    Args:
        query_terms: List of analyzed query terms.
        doc_id: Document identifier of indexed document.
        es: Elasticsearch object instance.
        index: Name of relevant index on the running Elasticsearch service.

    Returns:
        List of extracted feature values in a fixed order.
    """
    query_features = extract_query_features(query_terms, es, index=index)
    feature_vect = [query_features[f] for f in FEATURES_QUERY]

    doc_features = extract_doc_features(doc_id, es, index=index)
    feature_vect.extend([doc_features[f] for f in FEATURES_DOC])

    query_doc_features = extract_query_doc_features(
        query_terms, doc_id, es, index=index
    )
    feature_vect.extend([query_doc_features[f] for f in FEATURES_QUERY_DOC])

    return feature_vect


def index_documents(filepath: str, es: Elasticsearch, index: str) -> None:
    """Indexes documents from JSONL file."""
    bulk_data = []
    with open(filepath, "r") as docs:
        for doc in docs:
            doc = json.loads(doc)
            bulk_data.append({"index": {"_index": index, "_id": doc.pop("doc_id")}})
            bulk_data.append(doc)
    es.bulk(index=index, body=bulk_data, refresh=True)


def load_queries(filepath: str) -> Dict[str, str]:
    """Given a filepath, returns a dictionary with query IDs and corresponding
    query strings.

    This is an example query:

    ```
    <top>
    <num> Number: OHSU1
    <title> 60 year old menopausal woman without hormone replacement therapy
    <desc> Description:
    Are there adverse effects on lipids when progesterone is given with estrogen replacement therapy
    </top>

    ```

    Take as query ID the value (on the same line) after `<num> Number: `,
    and take as the query string the rest of the line after `<title> `. Omit
    newline characters.

    Args:
        filepath: String (constructed using os.path) of the filepath to a
        file with queries.

    Returns:
        A dictionary with query IDs and corresponding query strings.
    """
    # TODO

    queries = defaultdict(list)

    with open(filepath) as f:
        with open(filepath) as g:
            all_lines = g.readlines()
            print(len(all_lines))
            for line_number, line in enumerate(f, 1):
                clean_line = line.strip()
                if (line_number == 2) or ((line_number - 2) % 7) == 0:
                    # print(clean_line.split("Number: "))
                    # print(f'line_number is {line_number}')
                    # print(all_lines[line_number].split("<title> "))
                    q_id = clean_line.split("Number: ")[1]
                    pas_id = str(all_lines[line_number].split("<title> ")[1]).strip()
                    queries[q_id] = pas_id
    # print(queries)
    return queries


def load_qrels(filepath: str) -> Dict[str, List[str]]:
    """Loads query relevance judgments from a file.
    The qrels file has content with tab-separated values such as the following:

    ```
    MSH1	87056458
    MSH1	87056800
    MSH1	87058606
    MSH2	87049102
    MSH2	87056792
    ```

    Args:
        filepath: String (constructed using os.path) of the filepath to a
            file with queries.

    Returns:
        A dictionary with query IDs and a corresponding list of document IDs
            for documents judged relevant to the query.
    """
    # TODO

    qrels = defaultdict(list)
    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            q_id = line.split("\t")[0]
            pas_id = str(line.split("\t")[1]).strip()
            qrels[q_id].append(pas_id)
    # print(qrels)
    return qrels


def prepare_ltr_training_data(
    query_ids: List[str],
    all_queries: Dict[str, str],
    all_qrels: Dict[str, List[str]],
    es: Elasticsearch,
    index: str,
) -> Tuple[List[List[float]], List[int]]:
    """Prepares feature vectors and labels for query and document pairs found
    in the training data.

        Args:
            query_ids: List of query IDs.
            all_queries: Dictionary containing all queries.
            all_qrels: Dictionary with keys as query ID and values as list of
                relevant documents.
            es: Elasticsearch object instance.
            index: Name of relevant index on the running Elasticsearch service.

        Returns:
            X: List of feature vectors extracted for each pair of query and
                retrieved or relevant document.
            y: List of corresponding labels.
    """
    # TODO

    X = list()
    y = list()
    # print(f'query_ids {len(query_ids)}')
    for query in query_ids:
        print(query)
        # print(query)
        query_terms = analyze_query(es, all_queries[query], "body", index)

        for d_id in all_qrels.get(query, {}):
            X.append(extract_features(query_terms, d_id, es, index))
            y.append(1)

        res = es.search(index=index, q=" ".join(query_terms), size=100)["hits"]["hits"]
        for doc in res:
            if doc["_id"] not in all_qrels.get(query, {}):
                X.append(extract_features(query_terms, doc["_id"], es, index))
                y.append(0)

    return X, y


class PointWiseLTRModel:
    def __init__(self) -> None:
        """Instantiates LTR model with an instance of scikit-learn regressor."""
        # TODO
        self.regressor = MLPRegressor()

    def _train(self, X: List[List[float]], y: List[float]) -> None:
        """Trains an LTR model.

        Args:
            X: Features of training instances.
            y: Relevance assessments of training instances.
        """
        assert self.regressor is not None
        self.model = self.regressor.fit(X, y)

    def rank(
        self, ft: List[List[float]], doc_ids: List[str]
    ) -> List[Tuple[str, float]]:
        """Predicts relevance labels and rank documents for a given query.

        Args:
            ft: A list of feature vectors for query-document pairs.
            doc_ids: A list of document ids.
        Returns:
            List of tuples, each consisting of document ID and predicted
                relevance label.
        """
        assert self.model is not None
        rel_labels = self.model.predict(ft)
        sort_indices = np.argsort(rel_labels)[::-1]

        results = []
        for i in sort_indices:
            results.append((doc_ids[i], rel_labels[i]))
        return results


def get_rankings(
    ltr: PointWiseLTRModel,
    query_ids: List[str],
    all_queries: Dict[str, str],
    es: Elasticsearch,
    index: str,
    rerank: bool = False,
) -> Dict[str, List[str]]:
    """Generate rankings for each of the test query IDs.

    Args:
        ltr: A trained PointWiseLTRModel instance.
        query_ids: List of query IDs.
        es: Elasticsearch object instance.
        index: Name of relevant index on the running Elasticsearch service.
        rerank: Boolean flag indicating whether the first-pass retrieval
            results should be reranked using the LTR model.

    Returns:
        A dictionary of rankings for each test query ID.
    """

    test_rankings = {}
    for i, query_id in enumerate(query_ids):
        print("Processing query {}/{} ID {}".format(i + 1, len(query_ids), query_id))
        # First-pass retrieval
        query_terms = analyze_query(es, all_queries[query_id], "body", index=index)
        if len(query_terms) == 0:
            print(
                "WARNING: query {} is empty after analysis; ignoring".format(query_id)
            )
            continue
        hits = es.search(index=index, q=" ".join(query_terms), _source=True, size=100)[
            "hits"
        ]["hits"]
        test_rankings[query_id] = [hit["_id"] for hit in hits]

        # Rerank the first-pass result set using the LTR model.
        if rerank:
            # TODO

            test_rankings[query_id] = [hit["_id"] for hit in hits]

            X = list()
            Y = list()
            for d_id in test_rankings[query_id]:
                print("get rankings", d_id)
                X.append(extract_features(query_terms, d_id, es, index))

            for res in ltr.rank(X, test_rankings[query_id]):
                print(res)
                if res[1] > 0:
                    Y.append(res[0])
            test_rankings[query_id] = Y
            print(query_id, test_rankings)
        else:
            test_rankings[query_id] = [hit["_id"] for hit in hits]
    return test_rankings


def get_reciprocal_rank(system_ranking: List[str], ground_truth: List[str]) -> float:
    """Computes Reciprocal Rank (RR).

    Args:
        system_ranking: Ranked list of document IDs.
        ground_truth: Set of relevant document IDs.

    Returns:
        RR (float).
    """
    for i, doc_id in enumerate(system_ranking):
        if doc_id in ground_truth:
            return 1 / (i + 1)
    return 0


def get_mean_eval_measure(
    system_rankings: Dict[str, List[str]],
    ground_truths: Dict[str, Set[str]],
    eval_function: Callable,
) -> float:
    """Computes a mean of any evaluation measure over a set of queries.

    Args:
        system_rankings: Dict with query ID as key and a ranked list of document
            IDs as value.
        ground_truths: Dict with query ID as key and a set of relevant document
            IDs as value.
        eval_function: Callback function for the evaluation measure that mean is
            computed over.

    Returns:
        Mean evaluation measure (float).
    """
    sum_score = 0
    for query_id, system_ranking in system_rankings.items():
        sum_score += eval_function(system_ranking, ground_truths[query_id])
    return sum_score / len(system_rankings)


if __name__ == "__main__":
    index_name = "trec9_index"
    es = Elasticsearch(timeout=120)

    index_documents("data/documents.jsonl", es, index_name)
