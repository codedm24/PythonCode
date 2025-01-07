#Machine Learning - Bootstrap Aggregating (Bagging)


#Evaluating the base class classifier
import os
import sys
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt

#change current directory
print(f"Current Directory: {os.getcwd()}")
os.chdir("Python-ML")
print(f"Current Directory: {os.getcwd()}")

#Load dataset
data = datasets.load_wine()
X = data.data #data['data']
y = data.target #data['target']

#split dataset for train, test
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size=0.25, random_state=22)

#create a decision tree classifier
model = DecisionTreeClassifier(random_state=22)
model.fit(X_train,y_train)

#Predict a value
y_pred = model.predict(X_test)

print("Train data accuracy:", accuracy_score(y_train, model.predict(X_train)))
print("Test data accuracy:", accuracy_score(y_test, y_pred))

#Evaluating Bootstrap Aggregation
estimator_range = [2,4,6,8,10,12,14,16]

models = []
scores = []

for n_estimator in estimator_range:
    #model = BaggingClassifier(n_estimators=n_estimator, random_state=22)
    # out-of-bag score
    model = BaggingClassifier(n_estimators=n_estimator, oob_score=True, random_state=22)
    model.fit(X_train, y_train)
    models.append(model)
    score = accuracy_score(y_true= y_test, y_pred=model.predict(X_test))
    scores.append(score)

#Generate the plot of scores against number of scores
plt.figure(figsize=(9,6))
plt.plot(estimator_range,scores)

plt.xlabel("n_estimators", fontsize = 18)
plt.ylabel("score", fontsize = 18)
plt.tick_params(labelsize = 16)

plt.show()

#use the best n_estimators value for the model
model = BaggingClassifier(n_estimators=12, oob_score=True, random_state=22)
model.fit(X_train, y_train)
print(f"model oob score: {model.oob_score_}")

#plot the decission tree 
from sklearn.tree import plot_tree
plt.figure(figsize=(30,20))
plot_tree(model.estimators_[0])

plt.savefig("BootstrapAggregation.png")
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()