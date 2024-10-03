# numpy ufunc set operations
import numpy as np

arr = np.array([1,1,1,2,3,4,5,5,6,7])
x = np.unique(arr)
print("unique values in arry", x)

arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.union1d(arr1,arr2)
print("union of two array", newarr)

newarr = np.intersect1d(arr1,arr2, assume_unique=True)
print("intersection of two array", newarr)

newarr = np.setdiff1d(arr1,arr2,assume_unique=True)
print("diff between two array with values from 1st array", newarr)

newarr = np.setxor1d(arr1,arr2,assume_unique=True)
print("symmetric diff between two array", newarr)


 

arr = np.array([1,2,3,4,5,6,7])
print(arr[::2])
print(arr.dtype)
print(arr.shape)
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
arr = np.concatenate(arr1,arr2)
print(arr)