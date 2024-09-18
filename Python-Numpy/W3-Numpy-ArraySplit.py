# numpy array split
import numpy as np

print('split 1-D array')
arr = np.array([1,2,3,4,5,6])
newarr = np.split(arr,3)
print(newarr)
newarr = np.split(arr,3)
print(newarr)
print(newarr[0])
print(np.ndim(newarr))

print('split 2-D array')
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print(arr.__len__())
newarr = np.array_split(arr,3)
print(newarr)
print(np.ndim(newarr))
print(newarr.__len__())

print('hsplit 1-D array')
arr = np.array([1,2,3,4,5,6])
newarr = np.hsplit(arr,3)
print(newarr)
print(newarr[0])
print(np.ndim(newarr))

print('hsplit 2-D array')
arr = np.array([[1,2,3],[3,4,10],[5,6,8],[7,8,31],[9,10,13],[11,12,15]])
print(arr.__len__())
newarr = np.hsplit(arr,3)
print(newarr)
print(np.ndim(newarr))
print(newarr.__len__())

print('hsplit 3-D array')
arr = np.array([[[1,2,3,9],[3,4,10,47],[5,6,8,59]],[[7,8,31,66],[9,10,13,78],[11,12,15,45]]])
print(arr.__len__())
newarr = np.hsplit(arr,[6,2])
print(newarr)
#print(np.ndim(newarr))
print(newarr.__len__())


arr = np.arange(16.0).reshape(4, 4)
print("Original Array:\n", arr)
split_arr = np.hsplit(arr, 2)
print("Split Array:\n", split_arr)