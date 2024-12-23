#Machine Learning-LinearRegression
"""
This script demonstrates the use of linear regression for predictive analysis using both SciPy and scikit-learn libraries.
The script includes the following sections:
1. Importing necessary libraries.
2. Performing linear regression using SciPy:
    - Scatter plot of the data points.
    - Calculation of the regression line parameters (slope, intercept, etc.).
    - Plotting the regression line.
    - Predicting future values using the regression model.
    - Demonstrating a bad fit for linear regression with a different dataset.
3. Performing linear regression using scikit-learn:
    - Reshaping the data for compatibility with scikit-learn.
    - Creating and training the linear regression model.
    - Making predictions using the trained model.
    - Visualizing the original data points and the regression line.
Functions:
- myFunc(x): Returns the predicted y value for a given x using the calculated slope and intercept from SciPy's linear regression.
Note: Ensure that the required libraries (matplotlib, scipy, sklearn, numpy) are installed in your Python environment.
"""
import matplotlib.pyplot as plt
from scipy import stats
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

#slope, intercept, r -relationship, p, stderr
slope, intercept, r, p, std_err = stats.linregress(x, y)

print(f"slope:{slope}, intercept:{intercept}, r:{r}, p:{p}, std_err:{std_err}")

def myFunc(x):
    return slope * x + intercept

mymodel = list(map(myFunc,x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.title('Linear Regression')
plt.xlabel('age')
plt.ylabel('speed')
plt.show()

#predict future values

print("future predictor")
speed = myFunc(10)
print(f"The predicted spped of a 10 year old car is {speed}")

#bad fit for linear regression
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope,intercept,r,p,std_err= stats.linregress(x,y)

def myFunc(x):
    return slope * x + intercept

mymodel = list(map(myFunc,x))

plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

#another example
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Reshape the data
x = np.array(x).reshape(-1, 1)
print(f"after reshape: {x}")
y = np.array(y)
print(f"after reshape: {y}")

# Create and train the model
model = LinearRegression()
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

print(f"Predicted values: {y_pred}")

print(f"Mean Absolute Error: {mean_absolute_error(y, y_pred)}")

# Visualize the results
plt.scatter(x, y, color='blue')  # Original data points
plt.plot(x, y_pred, color='red')  # Regression line
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression using Sklearn(Scikit-learn)')
plt.show()