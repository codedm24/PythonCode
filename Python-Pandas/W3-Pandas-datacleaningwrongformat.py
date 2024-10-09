# Pandas data cleaning wrong format
import pandas as pd

#update wrong format value in Date column
print("update wrong format value")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
print(df)
df["Date"] = pd.to_datetime(df["Date"],format='mixed')
print(df)

#drop rows with empty values in a particular column
print("update wrong format value")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
print(df)
df.dropna(subset=['Date'],inplace=True)
print(df)
