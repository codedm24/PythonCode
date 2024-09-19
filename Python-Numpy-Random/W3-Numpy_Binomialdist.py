# numpy random binomial distribution
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

print('generate binomial distribution')
x = random.binomial(n=10, p =0.5, size=10)
print(x)

print('generate plot of a binomial distribution')
x = random.binomial(n=10,p=0.5,size=1000)
sns.displot(x, kind='kde')
plt.show()

print('generate normal and binomial distribution')
x = random.normal(loc=50, scale=5, size=1000)
y = random.binomial(n=100,p=0.5,size=1000)
sns.displot(x,kind='kde',legend='normal')
sns.displot(y,kind='kde',legend='binomial')
plt.show()

df = pd.DataFrame({'Normal': x, 'Binomial': y})
df_melted = pd.melt(df,var_name='Distribution', value_name='Value')
sns.displot(df_melted,x='Value',hue='Distribution', kind='kde',height=6,aspect=1.5)
plt.show()