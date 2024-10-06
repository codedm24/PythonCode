# Pandas read csv
import pandas as pd
import numpy as np

df = pd.read_csv("F:\Projects\Python\PythonCode\Python-Pandas\data.csv")
#prints first 5 and last 5 rows
print(df)
#prints entire dataframe
print(df.to_string())

print("max row settings", pd.options.display.max_rows)

print("Update max rows settings")
pd.options.display.max_rows = 60
print(df)