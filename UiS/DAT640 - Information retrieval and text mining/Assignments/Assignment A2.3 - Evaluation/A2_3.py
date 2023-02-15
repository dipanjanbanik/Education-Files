from typing import Callable, Dict, List, Set

import ir_datasets, csv


def load_rankings(
    filename: str = "system_rankings.tsv",
) -> Dict[str, List[str]]:
    """Load rankings from file. Every row in the file contains query ID and
    document ID separated by a tab ("\t").

        query_id    doc_id
        646	        4496d63c-8cf5-11e3-833c-33098f9e5267
        646	        ee82230c-f130-11e1-adc6-87dfa8eff430
        646	        ac6f0e3c-1e3c-11e3-94a2-6c66b668ea55

    Example return structure:

    {
        query_id_1: [doc_id_1, doc_id_2, ...],
        query_id_2: [doc_id_1, doc_id_2, ...]
    }

    Args:
        filename (optional): Path to file with rankings. Defaults to
            "system_rankings.tsv".

    Returns:
        Dictionary with query IDs as keys and list of documents as values.
    """
    # TODO
    filePath = "./data/" + filename
    rankingDict = {}
    with open(filePath, "r") as fileData:
        reader = csv.reader(fileData, delimiter="\t")
        next(reader)
        for row in reader:
            if row[0] not in rankingDict:
                rankingDict[row[0]] = []
                rankingDict[row[0]].append(row[1])
            else:
                rankingDict[row[0]].append(row[1])
    return rankingDict


def load_ground_truth(
    collection: str = "wapo/v2/trec-core-2018",
) -> Dict[str, Set[str]]:
    """Load ground truth from ir_datasets. Qrel is a namedtuple class with
    following properties:

        query_id: str
        doc_id: str
        relevance: int
        iteration: str

    relevance is split into levels with values:

        0	not relevant
        1	relevant
        2	highly relevant

    This function considers documents to be relevant for relevance values
        1 and 2.

    Generic structure of returned dictionary:

    {
        query_id_1: {doc_id_1, doc_id_3, ...},
        query_id_2: {doc_id_1, doc_id_5, ...}
    }

    Args:
        filename (optional): Path to file with rankings. Defaults to
            "system_rankings.tsv".

    Returns:
        Dictionary with query IDs as keys and sets of documents as values.
    """
    truthDict = {}
    dataset = ir_datasets.load(collection)
    for qrel in dataset.qrels_iter():
        # TODO
        ...
        if qrel.relevance >= 1:
            if qrel.query_id not in truthDict:
                truthDict[qrel.query_id] = set()
                truthDict[qrel.query_id].add(qrel.doc_id)
            else:
                truthDict[qrel.query_id].add(qrel.doc_id)
        else:
            continue
    return truthDict


def get_precision(
    system_ranking: List[str], ground_truth: Set[str], k: int = 100
) -> float:
    """Computes Precision@k.

    Args:
        system_ranking: Ranked list of document IDs.
        ground_truth: Set of relevant document IDs.
        k: Cutoff. Only consider system rankings up to k.

    Returns:s
        P@K (float).
    """
    # TODO
    totalItem = docId = 0
    while docId in range(0, k):
        if system_ranking[docId] in ground_truth:
            totalItem += 1
        docId += 1
    precisionValue = totalItem / k
    return precisionValue


def get_average_precision(system_ranking: List[str], ground_truth: Set[str]) -> float:
    """Computes Average Precision (AP).

    Args:
        system_ranking: Ranked list of document IDs.
        ground_truth: Set of relevant document IDs.

    Returns:
        AP (float).
    """
    # TODO

    val = docId = totalItem = 0
    k = len(system_ranking)
    for i in range(0, k):
        if system_ranking[i] in ground_truth:
            while docId in range(0, i + 1):
                if system_ranking[docId] in ground_truth:
                    totalItem += 1
                docId += 1
            precisionValue = totalItem / (i + 1)
            val += precisionValue
    averagePrecision = val / len(ground_truth)
    return averagePrecision


def get_reciprocal_rank(system_ranking: List[str], ground_truth: Set[str]) -> float:
    """Computes Reciprocal Rank (RR).

    Args:
        system_ranking: Ranked list of document IDs.
        ground_truth: Set of relevant document IDs.

    Returns:
        RR (float).
    """
    # TODO
    allRank = []
    for x in system_ranking:
        if x in ground_truth:
            rankValue = 1 / (system_ranking.index(x) + 1)
            allRank.append(rankValue)
    return allRank[0]


def get_mean_eval_measure(
    system_rankings: Dict[str, List[str]],
    ground_truths: Dict[str, Set[str]],
    eval_function: Callable,
) -> float:
    """Computes a mean of any evaluation measure over a set of queries.

    Args:
        system_rankings: Dict with query ID as key and a ranked list of
            document IDs as value.
        ground_truths: Dict with query ID as key and a set of relevant document
            IDs as value.
        eval_function: Callback function for the evaluation measure that mean
            is computed over.

    Returns:
        Mean evaluation measure (float).
    """
    # TODO
    val = reciprocalRank = 0
    k = len(system_rankings)
    for queryKey in system_rankings:
        reciprocalRank = eval_function(
            system_rankings[queryKey], ground_truths[queryKey]
        )
        val += reciprocalRank
    meanEvalMeasure = val / k
    return meanEvalMeasure


if __name__ == "__main__":
    system_rankings = load_rankings()
    ground_truths = load_ground_truth()
