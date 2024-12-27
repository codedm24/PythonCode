#Machine Learning - model selection
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 1.9, 3.1, 3.9, 5.1])

# Fit a polynomial of degree 2
coefficients = np.polyfit(X, y, 2)
poly_model = np.poly1d(coefficients)

# Predict values
X_test = np.array([6, 7, 8])
y_pred = poly_model(X_test)

# Print predictions
for i, x in enumerate(X_test):
    print(f"Prediction for {x}: {y_pred[i]}")

# Plotting the results
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, poly_model(X), color='red', label='Polynomial fit')
plt.scatter(X_test, y_pred, color='green', marker='x', label='Predictions')
plt.legend()
plt.show()
