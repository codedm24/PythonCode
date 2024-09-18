# numpy array iterating
import numpy as np

print('1-D array iteration')
arr = np.array([1,2,3])
for x in arr:
    print(x)

print('2-D array iteration')
arr = np.array([[1,2,3],[4,5,6]])    
for x in arr:
    print(x)
for x in arr:
    for y in x:
        print(y)    

print('3-D array iteration')
arr = np.array([[[1,2,3],[6,5,4]],[[3,7,8],[9,10,12]]])
for x in arr:
    print(x)
for x in arr:
    for y in x:
        for z in y:
            print(z)    

print('using nditer to iterate array of any dimesion')
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])            
for x in np.nditer(arr):
    print(x)

print('data type of array in iteration')
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr, flags=['buffered'], op_dtypes='S'):
    print(x)
for x in np.nditer(arr, flags=['buffered'], op_flags=['readwrite'] ,op_dtypes='S',casting='unsafe'):
    print(x)    

print('2-D array iteration')
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:,::2]):
    print(x)

print(arr[:,::2])  

print('ndenumerate')
arr = np.array([[1,2,3],[4,5,6]])
for x in np.ndenumerate(arr):
    print(x)