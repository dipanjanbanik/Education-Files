from typing import List


def get_confusion_matrix(actual: List[int], predicted: List[int]) -> List[List[int]]:
    """Computes confusion matrix from lists of actual or predicted labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        List of two lists of length 2 each, representing the confusion matrix.
    """
    # TODO

    # another method
    # fp = fn = tp = tn = 0
    # for actual_value, predicted_value in zip(actual, predicted):
    #     # let's first see if it's a true (t) or false prediction (f)
    #     if predicted_value == actual_value:  # t?
    #         if predicted_value == 1:  # tp
    #             tp += 1
    #         else:  # tn
    #             tn += 1
    #     else:  # f?
    #         if predicted_value == 1:  # fp
    #             fp += 1
    #         else:  # fn
    #             fn += 1

    # matrix = [[tn, fp], [fn, tp]]
    # return matrix

    # another method
    # unique = set(actual)
    # matrix = [list() for x in range(len(unique))]
    # for i in range(len(unique)):
    #     matrix[i] = [0 for x in range(len(unique))]
    # lookup = dict()
    # for i, value in enumerate(unique):
    #     lookup[value] = i
    # for i in range(len(actual)):
    #     x = lookup[actual[i]]
    #     y = lookup[predicted[i]]
    #     matrix[x][y] += 1

    # another method
    unique = set(actual)
    matrix = [[0 for _ in unique] for _ in unique]
    imap = {key: i for i, key in enumerate(unique)}
    # Generate Confusion Matrix
    for p, a in zip(predicted, actual):
        matrix[imap[a]][imap[p]] += 1
    return matrix


def accuracy(actual: List[int], predicted: List[int]) -> float:
    """Computes the accuracy from lists of actual or predicted labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        Accuracy as a float.
    """
    # TODO

    matrix = get_confusion_matrix(actual, predicted)
    fp = matrix[0][1]
    fn = matrix[1][0]
    tp = matrix[1][1]
    tn = matrix[0][0]
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    return accuracy

    # another method
    # correct = 0
    # for i in range(len(actual)):
    #     if actual[i] == predicted[i]:
    #         correct += 1
    # accuracy = correct / float(len(actual))


def precision(actual: List[int], predicted: List[int]) -> float:
    """Computes the precision from lists of actual or predicted labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        Precision as a float.
    """
    # TODO

    matrix = get_confusion_matrix(actual, predicted)
    fp = matrix[0][1]
    fn = matrix[1][0]
    tp = matrix[1][1]
    tn = matrix[0][0]
    precision = tp / (tp + fp)
    return precision


def recall(actual: List[int], predicted: List[int]) -> float:
    """Computes the recall from lists of actual or predicted labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        Recall as a float.
    """
    # TODO

    matrix = get_confusion_matrix(actual, predicted)
    fp = matrix[0][1]
    fn = matrix[1][0]
    tp = matrix[1][1]
    tn = matrix[0][0]
    recall = tp / (tp + fn)
    return recall


def f1(actual: List[int], predicted: List[int]) -> float:
    """Computes the F1-score from lists of actual or predicted labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        float of harmonic mean of precision and recall.
    """
    # TODO

    re_call = recall(actual, predicted)
    pre_cision = precision(actual, predicted)
    f1 = (2 * pre_cision * re_call) / (pre_cision + re_call)
    return f1


def false_positive_rate(actual: List[int], predicted: List[int]) -> float:
    """Computes the false positive rate from lists of actual or predicted
        labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        float of number of instances incorrectly classified as positive divided
            by number of actually negative instances.
    """
    # TODO

    matrix = get_confusion_matrix(actual, predicted)
    fp = matrix[0][1]
    fn = matrix[1][0]
    tp = matrix[1][1]
    tn = matrix[0][0]
    false_positive_rate = fp / (fp + tn)
    return false_positive_rate


def false_negative_rate(actual: List[int], predicted: List[int]) -> float:
    """Computes the false negative rate from lists of actual or predicted
        labels.

    Args:
        actual: List of integers (0 or 1) representing the actual classes of
            some instances.
        predicted: List of integers (0 or 1) representing the predicted classes
            of the corresponding instances.

    Returns:
        float of number of instances incorrectly classified as negative divided
            by number of actually positive instances.
    """
    # TODO

    matrix = get_confusion_matrix(actual, predicted)
    fp = matrix[0][1]
    fn = matrix[1][0]
    tp = matrix[1][1]
    tn = matrix[0][0]
    false_negative_rate = fn / (fn + tp)
    return false_negative_rate
