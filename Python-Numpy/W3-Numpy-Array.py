#numpy array

import numpy as np
#o D array
print("0-D array")
arr = np.array(42)
print(arr)
print('number of dimesions: ',arr.ndim)

print("1-D Array")
arr = np.array([1,2,3,4,5])
print(arr)
print('number of dimesions: ',arr.ndim)

print("2-D array")
arr = np.array([[1,2,3],[4,2,3]])
print(arr)
print('number of dimesions: ',arr.ndim)

print("3-D array")
arr = np.array([[[1,2,3],[2,3,1]],[[4,5,6],[20,11,30]]])
print(arr)
print('number of dimesions: ',arr.ndim)

print("n-d array")
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print('number of dimesions: ',arr.ndim)