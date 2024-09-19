# import numpy random Chi Square distribution
import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.chisquare(df=2,size=(2,3))
print(x)
sns.displot(x,kind='kde')
plt.show()

x = random.chisquare(df=1,size=100)
sns.displot(x,kind='kde')
plt.show()

