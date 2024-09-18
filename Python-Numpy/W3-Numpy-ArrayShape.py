# numpy array shape
import numpy as np

print('array shape')
arr = np.array([[1,2,3,7],[4,5,6,9]])
print(arr.shape)

arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print('shape of array: ', arr.shape)