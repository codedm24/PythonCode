# numpy random exponential distribution
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2,3))
print(x)
sns.displot(x,kind='kde')
plt.show()

x = random.exponential(scale=2, size=1000)
print(x)
sns.displot(x,kind='kde')
plt.show()