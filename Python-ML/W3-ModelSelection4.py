#Machine Learning - Model Selection
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Your dataset
X = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Fit Linear Regression using numpy
coefficients_linear = np.polyfit(X, y, 1)  # Degree 1 for linear regression
print(coefficients_linear)
linear_model = np.poly1d(coefficients_linear)

# Predict values using linear model
y_pred_linear = linear_model(X)

# Polynomial Regression (degree=2)
degree = 2
poly_features = PolynomialFeatures(degree)
print(f"X.reshape(-1, 1): {X.reshape(-1, 1)}") 
X_poly = poly_features.fit_transform(X.reshape(-1, 1))
print(f"X_poly: {X_poly}")
print(f"X_poly[:, 1]: {X_poly[:, 1]}")
coefficients_poly = np.polyfit(X_poly[:, 1], y, degree)
print(f"coefficients_poly: {coefficients_poly}")
poly_model = np.poly1d(coefficients_poly)
y_poly = poly_model(X_poly[:, 1])

# Predict values using polynomial model
X_test = np.linspace(min(X), max(X), 100)
print(f"X_test: {X_test}")
X_test_poly = poly_features.transform(X_test.reshape(-1, 1))
print(f"X_test_poly: {X_test_poly[:, 1]}")
y_pred_poly = poly_model(X_test_poly[:, 1])

# Metrics Calculation
mse_linear = mean_squared_error(y, y_pred_linear)
r2_linear = r2_score(y, y_pred_linear)
#mse_poly = mean_squared_error(y, poly_model(poly_features.transform(X.reshape(-1, 1))[:, 1]))
mse_poly = mean_squared_error(y, y_poly)
#r2_poly = r2_score(y, poly_model(poly_features.transform(X.reshape(-1, 1))[:, 1]))
r2_poly = r2_score(y, y_poly)

# Print Metrics
print("Linear Regression:")
print(f"  MSE: {mse_linear}")
print(f"  R²: {r2_linear}")

print("\nPolynomial Regression (degree 2):")
print(f"  MSE: {mse_poly}")
print(f"  R²: {r2_poly}")

# Plotting the results
plt.scatter(X, y, color='blue', label='Original data')

# Linear Regression Line
plt.plot(X, y_pred_linear, color='green', label='Linear regression')

# Polynomial Regression Line (generate more points for smooth curve)
plt.plot(X_test, y_pred_poly, color='red', label='Polynomial regression (degree 2)')

plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear vs Polynomial Regression')
plt.show()
