# numpy random poisson distribution
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x = random.poisson(lam=2,size=10)
print(x)

sns.displot(random.poisson(lam=50, size=1000),kind='hist')
plt.show()

print('Difference between normal and poisson distribution')
x = random.poisson(lam=50,size=1000)
y = random.normal(loc=50,scale=7,size=1000)

df = pd.DataFrame({'Normal':y,'Poisson':x})
df_melted = pd.melt(df,var_name='Distribution', value_name='Value')
sns.displot(df_melted,x='Value',hue='Distribution',kind='kde',height=6,aspect=1.5)
plt.show()

print('Difference between binomial and poisson distribution')
x = random.binomial(n=1000,p=0.1,size=1000)
y = random.poisson(lam=100,size=1000)

df = pd.DataFrame({'Binomial':x, 'Poisson':y})
df_melted = pd.melt(df,var_name='Distribution',value_name='Value')
sns.displot(df_melted,x='Value',hue='Distribution',kind='kde',height=6,aspect=1.5)
plt.show()