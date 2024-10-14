# Pandas correlation
import pandas as pd

df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\correlation-data.csv")
print(df.describe())
print(df.corr())