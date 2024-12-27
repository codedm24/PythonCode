#Machine Learning - model selection
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Your dataset
X = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]).reshape(-1, 1)
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

# Polynomial Regression (degree=2)
degree = 2
poly_features = PolynomialFeatures(degree)
X_poly = poly_features.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)

# Metrics Calculation
mse_linear = mean_squared_error(y, y_pred_linear)
r2_linear = r2_score(y, y_pred_linear)
mse_poly = mean_squared_error(y, y_pred_poly)
r2_poly = r2_score(y, y_pred_poly)

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
X_test = np.linspace(min(X), max(X), 100).reshape(-1, 1)
X_test_poly = poly_features.transform(X_test)
y_pred_test = poly_model.predict(X_test_poly)
plt.plot(X_test, y_pred_test, color='red', label='Polynomial regression (degree 2)')

plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear vs Polynomial Regression')
plt.show()
