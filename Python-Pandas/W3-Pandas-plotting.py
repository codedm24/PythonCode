# Pandas plotting
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("F:\\Projects\\Python\\PythonCode\\Python-Pandas\\correlation-data.csv")

df.plot()

plt.show()

df.plot(kind='scatter', x = 'Duration', y = 'Calories')

plt.show()

df['Duration'].plot(kind='hist')

plt.show()

data = [20, 23, 25, 27, 29, 30, 35, 36, 37, 40, 45]
plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Histogram of Exam Scores')
plt.show()
