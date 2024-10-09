# Pandas data cleaning for empty, NaN values
import pandas as pd

df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
print(df)

#returns a new dataset, does not change the original dataframe
print("return new dataset with removal of empty cells")
new_df = df.dropna()
print(new_df)

#updates original dataset
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
print(df)
print("update original dataset with removal of empty cells")
df.dropna(inplace=True)
print(df)

#remove rows for empty value in a particular column
print("remove rows for empty value in a particular column")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
df.dropna(subset=['Date'],inplace=True)
print(df)

#fill empty cells with a value
print("fill empty cells with a value")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
df.fillna(130,inplace=True)
print(df)

#fill empty cell with a value for a particular column
print("fill empty cell with a value for a particular column")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
#df["Calories"].fillna(130,inplace=True) - deprecated
df.fillna({"Calories":130},inplace=True)
print(df)

#fill empty cell with mean value of that column
#mean - the avg value of the column
print("fill empty cell with mean value of that column")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
x = df["Calories"].mean()
#df["Calories"].fillna(x,inplace=True) - deprecated
df.fillna({"Calories":x},inplace=True)
print(df)

#fill empty cell with median value of that column
#median - the middle value after arranging all values of the column in ascending order
print("fill empty cell with median value of that column")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
x = df["Calories"].median()
#df["Calories"].fillna(x,inplace=True) - deprecated
df.fillna({"Calories":x},inplace=True)
print(df)

#fill empty cell with median value of that column
#mode - value(s) that occur most frequently
print("fill empty cell with mode value of that column")
df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\data-cleaning.csv")
x = df["Calories"].mode()[0]
#df["Calories"].fillna(x,inplace=True) - deprecated
df.fillna({"Calories":x},inplace=True)
print(df)