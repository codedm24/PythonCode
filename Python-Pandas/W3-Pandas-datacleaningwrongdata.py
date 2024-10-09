#Pandas data cleaning wrong data
import pandas as pd

#Update value of a specific column of a row
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
df.loc[7,"Duration"] = 45
print(df)

#loop through all rows and update wrong data
print("loop through all rows and update wrong data")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print(df)

#remove rows that contain wrong data
print("remove rows that contain wrong data")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)
print(df)