# numpy ufunc LCM
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print("LCM",x)

arr1 = np.array([3,6,9])
x = np.lcm.reduce(arr1)
print("LCM",x)

arr1 = np.arange(1,11)
print(arr1)
x = np.lcm.reduce(arr1)
print("LCM",x) 