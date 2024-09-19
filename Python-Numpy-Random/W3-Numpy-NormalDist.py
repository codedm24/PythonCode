# numpy random normal distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

print('generate a normal distribution of a 2-D array')
x = random.normal(size=(3,2))
print(x)

print('generate a normal distribution of a 2-D array')
x = random.normal(loc = 1, scale = 2, size = (3,5))
print(x)
sns.histplot(x,kde=True)
plt.show()

print('generate a normal distribution of a 1-D array')
x = random.normal(size=100)
print(x)
sns.histplot(x,kde=True)
plt.show()