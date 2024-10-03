# numpy ufunc hyperbolic func
import numpy as np

x = np.sinh(np.pi/2)
print("sin hyper for pi/2", x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print("cos hyper for array", x)

x = np.arcsinh(1.0)
print("radian from value", x)

arr = np.array([0.1,0.2,0.5])
x = np.arctanh(arr)
print("radian from value", x)
print("degree from radian", np.rad2deg(x))