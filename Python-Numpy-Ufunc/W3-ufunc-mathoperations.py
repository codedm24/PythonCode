# numpy ufunc mathematical operations

import numpy as np

arr1 = np.array([10,11,12,13,14,15])
arr2 = np.array([20,21,22,23,24,25])

newarr = np.add(arr1,arr2)
print("ufunc add")
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([20,21,22,23,24,25])
print("ufunc subtract")
newarr = np.subtract(arr1,arr2)
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([20,21,22,23,24,25])
newarr = np.multiply(arr1,arr2)
print("ufunc multiply")
print(newarr)
#newarr1 = np.multiply(arr1,arr2,newarr)
#print(newarr1)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,10,8,2,33])
newarr = np.divide(arr1,arr2)
print("np divide")
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,5,6,8,2,33])
newarr = np.power(arr1,arr2)
print("np power")
print(newarr)
print(np.power(3,2))

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,7,9,8,2,33])
newarr = np.mod(arr1,arr2)
print("np mod")
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,7,9,8,2,33])
newarr = np.remainder(arr1,arr2)
print("np remainder")
print(newarr)

arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([3,7,9,8,2,33])
newarr = np.divmod(arr1,arr2)
print("np divmod")
print(newarr)
print((newarr[0]))
print(newarr[1])
for x in range(len(newarr[0])):
    print(newarr[0][x])

arr = np.array([-1,-2,1,2,3,-4])
newarr = np.absolute(arr)
print(newarr)    