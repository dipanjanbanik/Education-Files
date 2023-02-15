from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from urllib.request import urlopen
from PIL import Image

# actual = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0]
# predicted = [1, 1, 1, 1, 0, 0, 1, 0, 0, 1]
# True Positive = someone is sick and the person is sick.
# True Negative = someone is not sick and the person is not sick.
# False Positive = someone is sick and the person is not sick.
# False Negative = someone is not sick and the person is sick.

actual = [0, 1, 1, 0, 0, 0, 1, 1, 0, 0]
predicted = [1, 1, 1, 1, 0, 0, 1, 0, 0, 1]
cm = confusion_matrix(actual, predicted)
print("(TN) " + " (FP)\n" + "(FN) " + " (TP)")
print("confusion matrix: \n", cm)
print("precision: ", precision_score(actual, predicted))
print("recall: ", recall_score(actual, predicted))
print("f1: ", f1_score(actual, predicted))
print("accuracy: ", accuracy_score(actual, predicted))
