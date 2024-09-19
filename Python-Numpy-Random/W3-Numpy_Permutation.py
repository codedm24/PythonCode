# numpy random permutation
import numpy as np
from numpy import random

print('using shuffle')
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

print('using permutation')
arr = np.array([1,2,3,4,5])
newarr = random.permutation(arr)
print(newarr)