#Machine Learning - Scale
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import os

print(f'Current directory: {os.getcwd()}')
os.chdir('Python-ML')
print(f'Current directory: {os.getcwd()}')

scale = StandardScaler()

df =pd.read_csv('data1.csv')

cols = ['Volume','Weight']
X = df[cols]
y = df['CO2']

print(f'Before scaling:{X}')
scaledX = scale.fit_transform(X)
print(f'After scaling:{scaledX}')

model = linear_model.LinearRegression()
model.fit(scaledX,y)

testdata = {
    'Volume': [1.3],
    'Weight': [2300]
}

scaled_testdata = scale.transform(pd.DataFrame(testdata))

print(f'Scaled test data:\n{scaled_testdata}')
print(f'Scales test dataframe:\n{pd.DataFrame(scaled_testdata)}')
predictedscaledCO2 = model.predict(pd.DataFrame(scaled_testdata))
print(f'Predicted scaled value: {predictedscaledCO2}')

