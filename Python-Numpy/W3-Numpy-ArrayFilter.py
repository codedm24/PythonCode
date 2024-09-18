# numpy array filter
import numpy as np

arr = np.array([41,40,43,45])
x = [True,False,True,False]
newarr = arr[x]
print(newarr)

print('create filter array using condition')
arr = np.array([41,42,43,40,44])
filterarr = []

for x in arr:
    if x > 42 :
        filterarr.append(True)
    else:
        filterarr.append(False)

print(filterarr)
newarr = arr[filterarr]
print(newarr)

arr = np.array([1,2,3,4,5,6,7])

filter_arr =[]
for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

print(filter_arr)
newarr = arr[filter_arr]
print(newarr)

print('creating filter directly from array')

arr = np.array([41,42,40,43,39])
filter = arr > 40
print(arr[filter])
filter = arr % 2 == 0
print(arr[filter])