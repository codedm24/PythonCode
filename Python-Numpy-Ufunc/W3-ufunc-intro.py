# numpy ufunc

import numpy as np

#combine two lists without ufunc
x = [1,2,3,4]
y = [4,5,6,7]
z = []

print(zip(x,y))
for i, j in zip(x,y):
    z.append(i + j)
print(z)    

print("using ufunc")
z = np.add(x,y)
print(z)
