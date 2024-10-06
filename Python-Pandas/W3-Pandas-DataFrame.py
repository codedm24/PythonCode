# Pandas DataFrame - 2-Dimensional data structure, 2-dimensional array, table
import pandas as pd
import numpy as np

print("creating dataframe")

data = {
    "calories" : [420,380,390],
    "duration" : [50,50,45]
}

df = pd.DataFrame(data)

print(df)

print("Access DataFrame item")
print(df.loc[0])

print("Access multiple DataFrame items")
print(df.loc[[0,1]])

print("Name own index for DataFrame rows")
myvar = pd.DataFrame(data, index=["day1","day2","day3"])
print(myvar)


print("Select data using index")
print(myvar.loc["day2"])

print("Load data from file")
df = pd.read_csv('F:\Projects\Python\PythonCode\Python-Pandas\Movie-Data.csv')
print("DataFramme columns:")
print(df.columns)
print("Entire DataFrame")
print(df.to_string())
print("print first 10 rows")
print(df.head())