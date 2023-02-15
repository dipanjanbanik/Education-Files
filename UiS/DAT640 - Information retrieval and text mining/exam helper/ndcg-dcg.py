""" Reference from https://gist.github.com/bwhite/3726239
"""

import numpy as np


def dcg_at_k(r, k, method=0):
    """Score is discounted cumulative gain (dcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
    >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    >>> dcg_at_k(r, 1)
    3.0
    >>> dcg_at_k(r, 1, method=1)
    3.0
    >>> dcg_at_k(r, 2)
    5.0
    >>> dcg_at_k(r, 2, method=1)
    4.2618595071429155
    >>> dcg_at_k(r, 10)
    9.6051177391888114
    >>> dcg_at_k(r, 11)
    9.6051177391888114
    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: Number of results to consider
        method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
                If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
        Discounted cumulative gain
    """
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError("method must be 0 or 1.")
    return 0.0


def ndcg_at_k(r, k, method=0):
    """Score is normalized discounted cumulative gain (ndcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
    >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    >>> ndcg_at_k(r, 1)
    1.0
    >>> r = [2, 1, 2, 0]
    >>> ndcg_at_k(r, 4)
    0.9203032077642922
    >>> ndcg_at_k(r, 4, method=1)
    0.96519546960144276
    >>> ndcg_at_k([0], 1)
    0.0
    >>> ndcg_at_k([1], 2)
    1.0
    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: Number of results to consider
        method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
                If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
        Normalized discounted cumulative gain
    """
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.0
    return dcg_at_k(r, k, method) / dcg_max


# system_ranking_A = [0, 3, 0, 0, 2, 3, 1, 0, 0, 0]
# system_ranking_B = [1, 2, 3, 0, 0, 3, 0, 0, 0, 0]
# print(dcg_at_k(system_ranking_A, 5, method=0))
# print(dcg_at_k(system_ranking_B, 5, method=0))
# print(ndcg_at_k(system_ranking_A, 10, method=0))
# print(ndcg_at_k(system_ranking_B, 10, method=0))


all_values = []
# q1
system_ranking_A = [3, 2, 2, 0, 0]
system_ranking_B = [0, 0, 2, 2, 3]
system_ranking_C = [2, 2, 3, 0, 0]

ndcg_A = ndcg_at_k(system_ranking_A, 5, method=0)
ndcg_B = ndcg_at_k(system_ranking_B, 5, method=0)
ndcg_C = ndcg_at_k(system_ranking_C, 5, method=0)

# print("----------q1----------")
# print(ndcg_A, "\t", ndcg_B, "\t", ndcg_C)

append_value = [ndcg_A, ndcg_B, ndcg_C]
all_values.append(append_value)


# q2
system_ranking_A = [0, 0, 2, 1, 0]
system_ranking_B = [0, 1, 0, 2, 0]
system_ranking_C = [2, 1, 0, 0, 0]

ndcg_A = ndcg_at_k(system_ranking_A, 5, method=0)
ndcg_B = ndcg_at_k(system_ranking_B, 5, method=0)
ndcg_C = ndcg_at_k(system_ranking_C, 5, method=0)

# print("----------q2----------")
# print(ndcg_A, "\t", ndcg_B, "\t", ndcg_C)

append_value = [ndcg_A, ndcg_B, ndcg_C]
all_values.append(append_value)


# q3
system_ranking_A = [1, 0, 0, 3, 2]
system_ranking_B = [0, 2, 0, 1, 3]
system_ranking_C = [1, 0, 2, 3, 0]

ndcg_A = ndcg_at_k(system_ranking_A, 5, method=0)
ndcg_B = ndcg_at_k(system_ranking_B, 5, method=0)
ndcg_C = ndcg_at_k(system_ranking_C, 5, method=0)

# print("----------q3----------")
# print(ndcg_A, "\t", ndcg_B, "\t", ndcg_C)

append_value = [ndcg_A, ndcg_B, ndcg_C]
all_values.append(append_value)

print("----------all values (row wise)----------")
print(*all_values, sep="\n")

print("----------average (column wise)----------")
print(np.sum(all_values, axis=0) / np.shape(all_values)[0])
