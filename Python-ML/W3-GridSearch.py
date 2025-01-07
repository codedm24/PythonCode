#Machine Learning - Grid search
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

dataset = datasets.load_iris()
print(dataset.keys())

X = dataset['data']
y = dataset['target']

#Train data
#train_X = X[:80]
#train_y = y[:80]

#Test data
#test_X = X[80:]
#test_y = y[80:]

#Train Test split
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)   

#print(f"train_X shape: {train_X.shape}")
print(f"train_X shape: {train_X}")
print(f"test_X shape: {test_X}")
print(f"train_y shape: {train_y}")
print(f"test_y shape: {test_y}")

#create linearregression model
model = LogisticRegression(max_iter = 10000)

#train the model
#print(model.fit(X,y))
model.fit(train_X,train_y)

score = model.score(test_X, test_y)
print(f"score: {score}")

#Grid search
C = [0.25,0.5,0.75,1,1.25,1.5,1.75,2]

#Loop through the values of C
scores = []
for c in C:
    model.set_params(C=c)
    model.fit(train_X,train_y)
    score = model.score(test_X,test_y)
    scores.append(score)
    print(f"C: {c}, score: {score}")