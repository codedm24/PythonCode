# numpy ufunc products
import numpy as np

arr = np.array([1,2,3,4])
x = np.prod(arr)
print("product: ", x)

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
newarr = np.prod([arr1,arr2])
print("product multiple array:", newarr)
newarr = np.prod([arr1,arr2],axis=1)
print("product multiple arra axis 1:", newarr)
#print("arr1:",arr1)

newarr = np.cumprod(arr1)
print("cumulative product:", newarr)

arr3 = np.array([1,2,3,5])
newarr = np.cumprod([arr1,arr2,arr3])
print("cumulative product multiple array:", newarr)


