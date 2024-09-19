# numpy random distribution
import numpy as np
from numpy import random

print('Generate distribution of 1-D array')
x = random.choice([3,5,7,9],p=[0.1,0.3,0.4,0.2],size=10)
print(x)

print('Generate distribution of 2-D array')

x = random.choice([3,5,7,9],p=[0.1,0.3,0.4,0.2],size=(3,5))
print(x)
print(np.ndim(x))

x = random.choice([3,5,7,9],p=[0.1,0.3,0.4,0.2],size=(3,2))
print(x)
print(np.ndim(x))
#print(x.ndim)
