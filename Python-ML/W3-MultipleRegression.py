#Machine Learning - Multiple Regression
import pandas
from sklearn import linear_model
import os

print('current directory',os.getcwd())
os.chdir('Python-ML')
print('current directory',os.getcwd())

df = pandas.read_csv("data.csv")

#print(df)
#print(df.describe())
#print(df.head())
#print(df.columns)

cols = ['Volume','Weight']
X = df[cols]
y = df['CO2']

#create a model with LinearRegression
model = linear_model.LinearRegression()
model.fit(X,y)

#predict value
testdata = {
    'Volume': [1300],
    'Weight': [2300]
}
#predictCO2 = model.predict([[2300, 1300]])
predictCO2 = model.predict(pandas.DataFrame(testdata))
print(f'Predicted value: {predictCO2}')
print(f'Coefficient: {model.coef_}')
print(f'Intercept: {model.intercept_}')
print(f'Coefficient weight:{model.coef_[1]}')

coeff_weight = model.coef_[1]

#When Weight is 2300 Kg then CO2 emission is 107.2087328 g/km
#So when Weight is 3300 Kg then CO2 emission is 107.2087328 + coeff_weight*1000 = 110.4370128 g/km
CO2_calculated = 107.2087328 + coeff_weight*1000
print(f'Calculated value: {CO2_calculated}')

#Now get the value from model
test_data = {
    'Volume': [1300],
    'Weight': [3300]
}
CO2_predicted = model.predict(pandas.DataFrame(test_data))

print(f'Predicted value: {CO2_predicted}')