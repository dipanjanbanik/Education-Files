from typing import Dict, List
import string


def get_word_frequencies(doc: str) -> Dict[str, int]:
    """Extracts word frequencies from a document.

    Args:
        doc: Document content given as a string.

    Returns:
        Dictionary with words as keys and their frequencies as values.
    """
    # TODO

    # create empty dictionary
    newDict = {}

    # replace all the punctuation with white space
    for character in string.punctuation:
        doc = doc.replace(character, " ")

    # create a list of dictionary with frequency
    words = doc.split()
    for word in words:
        if word in newDict:
            newDict[word] = newDict[word] + 1
        else:
            newDict[word] = 1

    return newDict


def get_word_feature_vector(
    word_frequencies: Dict[str, int], vocabulary: List[str]
) -> List[int]:
    """Creates a feature vector for a document, comprising word frequencies
        over a vocabulary.

    Args:
        word_frequencies: Dictionary with words as keys and frequencies as
            values.
        vocabulary: List of words.

    Returns:
        List of length `len(vocabulary)` with respective frequencies as values.
    """
    # TODO
    # create empty list
    newList = []

    # check each vocabulary word by their frequency and make feature vector
    for eachVocabularyWord in vocabulary:
        if eachVocabularyWord in word_frequencies:
            newList.append(word_frequencies[eachVocabularyWord])
        elif eachVocabularyWord not in word_frequencies:
            newList.append(0)

    return newList
