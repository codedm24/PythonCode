# numpy array reshape
import numpy as np

print('convert 1-D array to 2-D array')
arr = np.array([1,2,3,4,5,6,7,7,8,9,9,10])
newarr = arr.reshape(4,3)
print(arr)
print(newarr)

print('convert 1-D array to 3-D array')
newarr = arr.reshape(2,3,2)
print(newarr)
print('dimension: ', newarr.ndim)
print('shape: ', newarr.shape)
print('base of reshape: ', newarr.base)

print('convert with unknown dimesion')
arr = np.array([1,2,3,4,5,6,7,7])
newarr = arr.reshape(2,2,-1)
print(newarr)

print('flattening array')
arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1)
print(newarr)