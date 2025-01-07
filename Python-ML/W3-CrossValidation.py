#Machine Learning - Cross Validation
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold, \
LeaveOneOut, LeavePOut, ShuffleSplit, cross_val_score

#Load Dataset
X, y = datasets.load_iris(return_X_y=True)
#print(X)
#print(y)

#Createa a model
model = DecisionTreeClassifier(random_state=42)

#set K-Fold
k_folds = KFold(n_splits=5)

#set Stratified K-Fold
k_folds = StratifiedKFold(n_splits=5)

#set Leave-One-Out(LOO)
k_folds = LeaveOneOut()

#set Leave-P-Out(LPO)
k_folds = LeavePOut(p=2)

#set ShuffleSplit
k_folds = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits=5)

#Get the score
scores = cross_val_score(model, X, y, cv = k_folds)

#print the scores detail
print(f"Cross Validation scores: {scores}")
print(f"Average CV score: {scores.mean()}")
print(f"Number of CV scores used in Average: {len(scores)}")
