# numpy ufunc summation

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([2,4,6])
arr3 = np.array([6,5,4])

newarr = np.sum([arr1,arr2,arr3])
print(np.add(arr1,arr2))
print(arr3)
print("summation: ",newarr)

newarr = np.sum([arr1,arr2,arr3],axis=1)
print("summation over axis:", newarr)

newarr = np.cumsum(arr1)
print("Cumulative sum of array: ", newarr)

newarr = np.cumsum([arr1,arr2,arr3])
print("Cumulative sum of multiple array: ", newarr)