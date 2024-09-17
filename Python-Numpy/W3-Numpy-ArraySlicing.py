# array slicing

import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print('index 1 to 5:',arr[1:5])
print('index 4 to end: ', arr[4:])
print('index start to 4: ', arr[:4])
print('negative index -3 to -1: ', arr[-3:-1])
print('negative index start to 4: ', arr[-4:])
print('slicing with step: ', arr[:5:2])

print('2-D array')
arr = np.array([[1,4,5,7,9],[2,6,8,10,11]])
print('from second element: ', arr[1,1:4])
print('from both elements second element: ', arr[0:2,2])
print('from both elements from 1 to 4: ', arr[0:2,1:4])
print('every other element: ', arr[0:2,::2])