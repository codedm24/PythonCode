# numpy random logistic distribution
import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

x = random.logistic(loc=1, scale=2,size=100)
print(x)
sns.displot(x,kind='kde')
plt.show()

print('Difference between normal and logistic distribution')
x = random.normal(scale=2,size=1000)
y = random.logistic(size=1000)

df = pd.DataFrame({'Normal':x, 'Logistic':y})
df_melted = pd.melt(df,var_name='Distribution',value_name='Value')
sns.displot(df_melted,x='Value',hue='Distribution',kind='kde',height=6,aspect=1.5)
plt.show()