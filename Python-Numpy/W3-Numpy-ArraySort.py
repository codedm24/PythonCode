# numpy array sort
import numpy as np

print('1-D array sort')
arr = np.array([3,4,1,7,2,-1,9])
x = np.sort(arr)
print(x)

arr = np.array(['pineapple','grapes','apple','cherry','banana'])
print(np.sort(arr))

arr = np.array([True,False,True])
print(np.sort(arr))

print('2-D array sort')
arr = np.array([[3,2,1],[7,4,9]])
x = np.sort(arr)
print(x)
print(x.base)