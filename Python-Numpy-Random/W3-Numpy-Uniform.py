# numpy random uniform distribution

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(size=(2,3))
print(x)

print('Generate uniform distribution')
x = random.uniform(size=1000)
sns.displot(x,kind='kde')
plt.show()

print('Generate uniform distribution of 2-D array')
x = random.uniform(size=(4,3))
sns.displot(x,kind='kde')
plt.show()