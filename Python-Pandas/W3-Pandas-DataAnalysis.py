# Pandas data analysis using DataFrame

import pandas as pd
import numpy as np

df = pd.read_csv("F:\Projects\Python\PythonCode\Python-Pandas\Movie-Data.csv")
print("Display heads of the dataframe")
print(df.head(10))

print("Display tails of the dataframe")
print(df.tail(10))

print("Display info of dataframe")
print(df.info())