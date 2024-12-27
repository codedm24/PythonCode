import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
#X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
#y = np.array([1.2, 1.9, 3.1, 3.9, 5.1])
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6]).reshape(-1,1)
x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
print(x)
# Linear Regression
linear_model = LinearRegression()
linear_model.fit(x, y)
y_pred_linear = linear_model.predict(x)

# Polynomial Regression (degree=2)
#poly_features = PolynomialFeatures(degree=2)
#x_poly = poly_features.fit_transform(x)
#poly_model = LinearRegression()
#poly_model.fit(x_poly, y)
#y_pred_poly = poly_model.predict(x_poly)

mymodel = np.poly1d(np.polyfit(x1,y,2))
myline = np.linspace(min(x1),max(x1),13)
y_pred_poly = mymodel(myline)
print(y_pred_poly)

# Plotting
plt.scatter(x, y, color='blue')
plt.scatter(x1, y, color='red')
plt.plot(x, y_pred_linear, color='green', label='Linear Regression')
#plt.plot(x, y_pred_poly, color='red', label='Polynomial Regression')
plt.plot(myline, y_pred_poly, color='red', label='Polynomial Regression')
plt.legend()
plt.show()

# Evaluation
mse_linear = mean_squared_error(y, y_pred_linear)
r2_linear = r2_score(y, y_pred_linear)
mse_poly = mean_squared_error(y, y_pred_poly)
r2_poly = r2_score(y, y_pred_poly)

print(f'Linear Regression - MSE: {mse_linear}, R2: {r2_linear}')
print(f'Polynomial Regression - MSE: {mse_poly}, R2: {r2_poly}')
