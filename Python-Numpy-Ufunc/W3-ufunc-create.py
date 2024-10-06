# numpy ufinc create

import numpy as np

def myAdd(x,y):
    return x+y

myAdd = np.frompyfunc(myAdd,2,1)

print(myAdd([1,2,3,4],[5,6,7,8]))

print(type(myAdd))

print(type(np.add))
print(type(np.concatenate))

if(type(np.add) == np.ufunc):
    print("add is ufunc")
else:
    print("add is not ufunc")

print("np.add")
x = np.add([1,2,3,4],[5,6,7,8])
print(x)