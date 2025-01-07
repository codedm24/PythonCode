#Machine Learning - GridSearchCV, Support Vector Classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Set up the parameter grid for Support Vector Classification
param_gridSVC = {
    'C': [0.25,0.5,0.75,1,1.25,1.5,1.75,2], # [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['rbf']
}

# Set up the parameter grid for LogisticRegression
param_gridLR = {
    'C': [0.25,0.5,0.75,1,1.25,1.5,1.75,2], # [0.1, 1, 10, 100],
    'penalty': ['l1', 'l2','elasticnet',None],
    'solver':['lbfgs', 'liblinear', 'saga'],
}

# Create a GridSearchCV object
#create linearregression model
model = LogisticRegression(max_iter = 10000)
#create Support Vector Classification model
#model = SVC()
grid = GridSearchCV(model, param_gridLR, refit=True, verbose=2)

# Fit the model
grid.fit(X_train, y_train)

# Make predictions and evaluate the model
grid_predictions = grid.predict(X_test)
print(classification_report(y_test, grid_predictions))

# Find the best parameters
print(f"Best parameters found: {grid.best_params_}")
