# Numpy data type
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.dtype)

arr = np.array(['apple','banana','cherry'])
print(arr.dtype)

print('create array with defined type')
arr = np.array([1,2,3,4],dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)

arr = np.array(['A','a','b','C'],dtype='S')
print(arr)
print(arr.dtype)

print('convert array type')
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

