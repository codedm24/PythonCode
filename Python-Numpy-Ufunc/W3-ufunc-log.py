# numpy ufunc log
import numpy as np
from math import log 

arr = np.arange(1, 10)
print("original array: ",arr)
print("log arrary base 2: ",np.log2(arr))


arr = np.arange(1, 10)
logarr = np.log10(arr)
print("log array bae 10", logarr)

arr = np.arange(1, 10)
logarr = np.log(arr)
print("log array base e:", arr)

nplog = np.frompyfunc(log,2,1)
print("log of any base: ", nplog(100,15))


