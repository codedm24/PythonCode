# numpy array copy view
import numpy as np

print('array copy')
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
print('arr base: ', arr.base)
print('copy base: ', x.base)

print('array view')
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42
print(x)
print(arr)
print('arr base: ',arr.base)
print('view base: ',x.base)

x[0] = 1
print(x)
print(arr)