#import numpy random 
import numpy as np
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

x = random.rayleigh(scale=2,size=(2,3))
print(x)
sns.displot(x,kind='kde')
plt.show()

x = random.rayleigh(scale=2,size=100)
print(x)
sns.displot(x,kind='kde')
plt.show()