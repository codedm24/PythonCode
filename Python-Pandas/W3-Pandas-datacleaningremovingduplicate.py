#Pandas data cleaning removing duplicate

import pandas as pd

#display true for duplicate rows else false
print("display true for duplicate rows else false")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
print(df.duplicated())

print("remove duplicate rows")
df.drop_duplicates(inplace=True)
print(df)