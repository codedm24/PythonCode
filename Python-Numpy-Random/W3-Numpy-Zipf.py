# numpy random zipf distribution
import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt


x = random.zipf(a=2,size=(2,3))
print(x)
sns.displot(x,kind='kde')
plt.show()

x = random.zipf(a=2,size=1000)
print(x)
sns.displot(x[x < 10],kind='hist')
plt.show()