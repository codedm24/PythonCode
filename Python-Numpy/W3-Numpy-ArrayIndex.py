#array indexing
import numpy as np

print('1-D array')
arr = np.array([1,2,3,4,5])
print(arr[0])
print(arr[2]+arr[3])

print('2-D array')
arr = np.array([[1,2,3,4,5],[4,5,7,9,10]])
print('second element of 1st row: ', arr[0,1])
print(arr[0,1] + arr[1,2])
print('5th element on 2nd row: ', arr[1,4])

print('3-D array')
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])

print('negative indexing')
arr = np.array([[1,2,3,4,5],[7,8,9,10,11]])
print(arr[1,-1])