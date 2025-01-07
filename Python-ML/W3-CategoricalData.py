#Machine Learning - Categorical Data
import os
import pandas as pd
from sklearn import linear_model

print(f"Current working directory: {os.getcwd()}")
os.chdir("Python-ML")
print(f"Current working directory: {os.getcwd()}")

#Load Dataset
cars = pd.read_csv('data.csv')
print(cars.to_string())

#Get OneHotEncoding
ohe_cars = pd.get_dummies(cars[['Car']])

print(ohe_cars.to_string())

#prepare dataset
X = pd.concat([cars[['Volume','Weight']], ohe_cars], axis = 1)
y = cars['CO2']

#create a model
model = linear_model.LinearRegression()
model.fit(X,y)

#predict result
predictedCO2 = model.predict([[2300,1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])

print(f"Predicted CO2: {predictedCO2}")

#drop first column
colors = pd.DataFrame({'color':['blue','red']})
print(colors)
dummies = pd.get_dummies(colors[['color']], drop_first = True)
print(dummies)

colors = pd.DataFrame({'color':['blue','red','green']})
print(colors)
dummies = pd.get_dummies(colors[['color']], drop_first = True)
print(dummies)
dummies['color']=colors['color']
print(dummies)