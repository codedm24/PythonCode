# numpy ufunc difference
import numpy as np

arr = np.array([10,15,25,5])
newarr = np.diff(arr)
print("difference:",newarr)

newarr = np.diff(arr,n=2)
print("repeated differnece: ", newarr)

arr1 = np.array([1,2,3,4])
arr2 = np.array([6,7,8,9])
newarr = np.diff([arr1,arr2])
print("difference multiple array:",newarr)

