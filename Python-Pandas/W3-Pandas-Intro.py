# pandas intro
import pandas as pd

df = pd.read_csv('F:\\Projects\\Python\\PythonCode\\Python-Pandas\\Movie-Data.csv')
#print(df.to_string())
print(df.describe)
print(df.head())