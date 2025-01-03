#Machine Learning - Confusion Metrics
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

actual = np.random.binomial(1, 0.9, 1000)
predicted = np.random.binomial(1, 0.9, 1000)

#get confusion matrix
cm = metrics.confusion_matrix(actual, predicted)    

#display confusion matrix
cm_display = metrics.ConfusionMatrixDisplay(cm, display_labels=[0,1]).plot()

plt.show()

#confusion matrix accuracy
accuracy = metrics.accuracy_score(actual, predicted)
print(f"Accuracy: {accuracy}")

#confusion matrix precision
precision = metrics.precision_score(actual, predicted)
print(f"Precision: {precision}")

#confusion matrix recall(sensitivity)
recall = metrics.recall_score(actual, predicted)
print(f"Recall: {recall}")

#confusion matrix f1 score
f1_score = metrics.f1_score(actual, predicted)
print(f"F1 Score: {f1_score}")