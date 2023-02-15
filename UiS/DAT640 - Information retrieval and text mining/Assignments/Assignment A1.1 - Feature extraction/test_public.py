import A1_1 as module


def test_get_word_frequencies_1():
    """This test is 0.5 points."""
    doc = "and with great power\ncomes great responsibility\nand few vacations"
    frequencies = {
        "with": 1,
        "great": 2,
        "power": 1,
        "comes": 1,
        "responsibility": 1,
        "and": 2,
        "few": 1,
        "vacations": 1,
    }
    assert module.get_word_frequencies(doc) == frequencies


def test_get_word_frequencies_2():
    """This test is 0.5 points."""
    doc = "document.with, punctuation:   with?spaces\ttabs\nwith newslines\n\n\n"
    frequencies = {
        "with": 3,
        "document": 1,
        "punctuation": 1,
        "spaces": 1,
        "tabs": 1,
        "newslines": 1,
    }
    assert module.get_word_frequencies(doc) == frequencies


def test_get_word_feature_vector_1():
    """This test is 0.5 points."""
    frequencies = {
        "with": 1,
        "great": 2,
        "power": 1,
        "comes": 1,
        "responsibility": 1,
        "and": 2,
        "few": 1,
        "vacations": 1,
    }
    vocabulary = list(sorted(frequencies))
    feature_vector = [2, 1, 1, 2, 1, 1, 1, 1]
    assert module.get_word_feature_vector(frequencies, vocabulary) == feature_vector


def test_get_word_feature_vector_2():
    """This test is 0.5 points."""
    frequencies = {
        "with": 3,
        "document": 1,
        "punctuation": 1,
        "spaces": 1,
        "tabs": 1,
        "newslines": 1,
    }
    vocabulary = ["document", "spaces", "tabs", "with", "great", "power"]
    feature_vector = [1, 1, 1, 3, 0, 0]
    assert module.get_word_feature_vector(frequencies, vocabulary) == feature_vector


def score_term(self, term: str, query_freq: int):
    """Scores one query term and updates the accumulated document retrieval
    scores (`self.scores`).

    Params:
        term: Query term
        query_freq: Frequency (count) of the term in the query.
    """
    postings = self.get_postings(term)
    for doc_id, payload in postings:
        self.scores[doc_id] += payload * query_freq


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
