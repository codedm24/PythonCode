# numpy array join
import numpy as np

print('join 1-D array')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)

print('join 2-D array')
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)

print('join 2-D array')
arr1 = np.array([[1,2,8],[3,4,10]])
arr2 = np.array([[5,6,12],[7,8,21]])
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)

print('join 3-D array')
arr1 = np.array([[[1,2],[3,4]],[[9,10],[11,12]]])
arr2 = np.array([[[5,6],[7,8]],[[13,14],[15,16]]])
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)
print(np.ndim(arr3))

print('stack 1-D array')
arr1= np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2),axis=1)
print(arr)

print('stack 2-D array')
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr = np.stack((arr1,arr2),axis=1)
print(arr)

print('hstack 1-D array')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.hstack((arr1,arr2))
print(arr)

print('hstack 2-D array')
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr = np.hstack((arr1,arr2))
print(arr)

print('vstack 1-D array')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.vstack((arr1,arr2))
print(arr)

print('vstack 2-D array')
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr = np.vstack((arr1,arr2))
print(arr)

print('dstack 1-D array')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1,arr2))
print(arr)

print('dstack 2-D array')
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr = np.dstack((arr1,arr2))
print(arr)

