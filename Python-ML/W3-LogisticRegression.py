#Machine Learning - Logistic Regression
import numpy as np
from sklearn import linear_model

X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)    
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = linear_model.LogisticRegression()
model.fit(X,y)  

predicted = model.predict(np.array([3.46]).reshape(-1,1))
print(predicted)

#coefficients
log_odds = model.coef_
print(f"coefficients: {log_odds}")

#exponential of coefficients
odds = np.exp(log_odds)
print(f"odds: {odds}")

def logit2prob(model, x):
    log_odds = model.coef_ * x + model.intercept_
    odds = np.exp(log_odds)
    probability =  odds / (1 + odds)
    return probability

print(logit2prob(model, X))
