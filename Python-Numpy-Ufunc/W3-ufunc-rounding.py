# numpy ufunc rounding
import numpy as np
import math

arr = np.trunc([-3.1666, 3.6667])
print("np trunc:",arr)

arr = np.fix([-6.1666, 3.6667])
print("np fix:", arr)

arr = np.around([4.125, 5.46, 3.478])
print("np around:", arr)

arr = np.floor(arr)
print("np floor:", arr)

#print(math.floor(arr))

arr = np.ceil([4.5,5.6,6.7,2.3])
print("np ceil:", arr)

