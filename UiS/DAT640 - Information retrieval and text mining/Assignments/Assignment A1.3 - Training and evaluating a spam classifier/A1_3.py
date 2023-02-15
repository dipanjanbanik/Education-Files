from typing import List, Tuple, Union
from numpy import ndarray
import pandas as pd
import string

# pip install nltk
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.svm import SVC

# reference - https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a


def load_data(path: str) -> Tuple[List[str], List[int]]:
    """Loads data from file. Each except first (header) is a datapoint
    containing ID, Label, Email (content) separated by "\t". Lables should be
    changed into integers with 1 for "spam" and 0 for "ham".

    Args:
        path: Path to file from which to load data

    Returns:
        List of email contents and a list of lobels coresponding to each email.
    """

    df = pd.read_csv(path, sep="\t")
    df = df.drop("Id", axis=1)
    df["Label"] = df["Label"].replace(["ham", "spam"], [0, 1])
    listOfLabels = df["Label"].values.tolist()
    listOfEmails = df["Email"].values.tolist()

    return listOfEmails, listOfLabels


def preprocess(doc: str) -> str:
    """Preprocesses text to prepare it for feature extraction.

    Args:
        doc: String comprising the unprocessed contents of some email file.

    Returns:
        String comprising the corresponding preprocessed text.
    """
    # TODO
    doc = doc.translate(str.maketrans("", "", string.punctuation))
    cachedStopWords = stopwords.words("english")
    doc = " ".join([word for word in doc.split() if word not in cachedStopWords])
    return doc
    ...


def preprocess_multiple(docs: List[str]) -> List[str]:
    """Preprocesses multiple texts to prepare them for feature extraction.

    Args:
        docs: List of strings, each consisting of the unprocessed contents
            of some email file.

    Returns:
        List of strings, each comprising the corresponding preprocessed
            text.
    """
    # TODO
    newDocs = []
    for i, val in enumerate(docs):
        newDocs.append(preprocess(val))
    return newDocs


def extract_features(
    train_dataset: List[str], test_dataset: List[str]
) -> Union[Tuple[ndarray, ndarray], Tuple[List[float], List[float]]]:
    """Extracts feature vectors from a preprocessed train and test datasets.

    Args:
        train_dataset: List of strings, each consisting of the preprocessed
            email content.
        test_dataset: List of strings, each consisting of the preprocessed
            email content.

    Returns:
        A tuple of of two lists. The lists contain extracted features for
          training and testing dataset respectively.
    """
    # TODO

    # Term Frequency, Inverse Document Frequenc
    # vectorizer = TfidfVectorizer()

    # CountVectorizer
    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(train_dataset)
    Y = vectorizer.transform(test_dataset)

    return X, Y


def train(X: ndarray, y: List[int]) -> object:
    """Trains a classifier on extracted feature vectors.

    Args:
        X: Numerical array-like object (2D) representing the instances.
        y: Numerical array-like object (1D) representing the labels.

    Returns:
        A trained model object capable of predicting over unseen sets of
            instances.
    """
    # TODO

    # Linear Regression
    # clf = LinearRegression()

    # Logistic Regression
    clf = LogisticRegression(max_iter=1000)

    # Support Vector Machines
    # clf = SVC(kernel="linear")

    clf.fit(X, y)
    return clf


def evaluate(y: List[int], y_pred: List[int]) -> Tuple[float, float, float, float]:
    """Evaluates a model's predictive performance with respect to a labeled
    dataset.

    Args:
        y: Numerical array-like object (1D) representing the true labels.
        y_pred: Numerical array-like object (1D) representing the predicted
            labels.

    Returns:
        A tuple of four values: recall, precision, F_1, and accuracy.
    """
    # TODO
    recall = recall_score(y, y_pred)
    precision = precision_score(y, y_pred)
    F_1_score = f1_score(y, y_pred)
    accuracy = accuracy_score(y, y_pred)
    return (recall, precision, F_1_score, accuracy)


if __name__ == "__main__":
    print("Loading data...")
    train_data_raw, train_labels = load_data("data/train.tsv")
    test_data_raw, test_labels = load_data("data/test.tsv")

    print("Processing data...")
    train_data = preprocess_multiple(train_data_raw)
    test_data = preprocess_multiple(test_data_raw)

    print("Extracting features...")
    train_feature_vectors, test_feature_vectors = extract_features(
        train_data, test_data
    )

    print("Training...")
    classifier = train(train_feature_vectors, train_labels)

    print("Applying model on test data...")
    predicted_labels = classifier.predict(test_feature_vectors)

    print("Evaluating")
    recall, precision, f1, accuracy = evaluate(test_labels, predicted_labels)

    print(f"Recall:\t{recall}")
    print(f"Precision:\t{precision}")
    print(f"F1:\t{f1}")
    print(f"Accuracy:\t{accuracy}")
