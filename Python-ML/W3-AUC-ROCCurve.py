#Machine Learning - AUC - ROC Curve
import os
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, \
    roc_auc_score, roc_curve

#Set current directory
print(f"Current directory: {os.getcwd()}")
os.chdir("Python-ML")
print(f"Current directory: {os.getcwd()}")

#Create a DataSet
n = 10000
ratio = 0.95
n_0 = int((1 - ratio) * n)
n_1 = int(ratio * n)

print(n_0)
print(n_1)

y = np.array([0] * n_0 + [1] * n_1)
y_prob = np.array([1]*n)
y_pred = y_prob > .5

print(f"y : {y}, length: {len(y)}")
print(f"y_prob: {y_prob}, length: {len(y_prob)}")
print(f"y_prod: {y_pred}, length: {len(y_pred)}")

#Display the score detail
print(f'accuracy score: {accuracy_score(y, y_pred)}')
cf_mat = confusion_matrix(y, y_pred)
print(f"Confusion matrix: {cf_mat}")

print(f"class 0 accuracy: {cf_mat[0][0]/n_0}")
print(f"class 1 accuracy: {cf_mat[1][1]/n_1}")

#Create dataset 2
y_prob_2 = np.array(
    np.random.uniform(0, .7, n_0).tolist() +
    np.random.uniform(.3, 1, n_1).tolist()
)

y_pred_2 = y_prob_2 > .5

print(f"accuracy score: {accuracy_score(y, y_pred_2)}")
cf_mat = confusion_matrix(y, y_pred_2)
print('Confusion matrix')
print(cf_mat)
print(f"class 0 accuracy: {cf_mat[0][0]/n_0}")
print(f"class 1 accuracy: {cf_mat[1][1]/n_1}")

#Use AUC method
import matplotlib.pyplot as plt

def plot_roc_curve(true_y, y_prob):
    '''
    plots the ROC curve based on the probabilities
    '''
    fpr, tpr, thresholds = roc_curve(true_y, y_prob)
    plt.figure()
    plt.plot(fpr,tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()

plot_roc_curve(y, y_prob)
plt.savefig("roc_curve.png")
print(f"Dataset 1 AUC score: {roc_auc_score(y, y_prob)}")

plot_roc_curve(y, y_prob_2)
plt.savefig("roc_curve_2.png")
print(f"Dataset 2 AUC score: {roc_auc_score(y, y_prob_2)}")

#Create dataset 3, 4
print(f"n//2: {n//2}")
y = np.array([0] * n + [1] * n)
y_prob_3 = np.array(
    np.random.uniform(.25,.5,n//2).tolist() +
    np.random.uniform(.3,.7,n).tolist() +
    np.random.uniform(.5,.75,n//2).tolist()
) 

y_prob_4 = np.array(
    np.random.uniform(0,.4,n//2).tolist() +
    np.random.uniform(.3,.7,n).tolist() +
    np.random.uniform(.5,.75,n//2).tolist()
)

print(f"Dataset 3 accuracy score: {accuracy_score(y, y_prob_3>.5)}")
print(f"Dataset 4 accuracy score: {accuracy_score(y,y_prob_4>.5)}")

plot_roc_curve(y, y_prob_3)
plt.savefig("roc_curve_3.png")
print(f"Dataset 3 AUC score: {roc_auc_score(y, y_prob_3)}")
plot_roc_curve(y, y_prob_4)
plt.savefig("roc_curve_4.png")
print(f"Dataset 4 AUC score: {roc_auc_score(y, y_prob_4)}")