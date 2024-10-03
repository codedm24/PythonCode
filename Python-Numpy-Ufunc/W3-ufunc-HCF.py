# numpy ufunc HCF

import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1,num2)
print("HCF",x)

arr = np.array([20,8,32,36,16])
x = np.gcd.reduce(arr)
print("hcf",x)