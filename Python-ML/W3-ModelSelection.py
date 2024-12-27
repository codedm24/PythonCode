#Machine Learning - Selecting between Linear and Ploynomial Regression
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#Data
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6]).reshape(-1,1)
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
print(x)


#Tranform Data for polynomial regression
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)
print(x_poly)

model = LinearRegression()
model.fit(x_poly,y)

#Make prediction
y_pred = model.predict(x_poly)

#Visualize the result
plt.scatter(x,y, color='blue')
plt.plot(x, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression')
plt.show()

#plot residuals
residuals = y - y_pred
plt.scatter(x,residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('X')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.show()

#Calculate error metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R2 Score: {r2}")

#Using Linear Regression
model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)

plt.scatter(x,y, color='blue')
plt.plot(x, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()

#plot residuals
residuals = y - y_pred
plt.scatter(x,residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('X')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.show()

#Calculate error metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error: {rmse}")
print(f"R2 Score: {r2}")