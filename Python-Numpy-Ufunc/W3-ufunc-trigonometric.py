# numpy ufunc trigonometric functions
import numpy as np

x = np.sin(np.pi/2)
print("sin pi/2", x)
x = np.cos(np.pi/2)
print("cos pi/2",x)
x = np.tan(np.pi/2)
print("tan pi/2",x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print("sin of radian array",x)

arr = np.array([90,180,270,360])
x = np.deg2rad(arr)
print("degree to radian", x)

y = np.rad2deg(x)
print("radian to degree", y)

x = np.arcsin(1.0)
print("radian from value", x)
print("angle from radian", np.rad2deg(x))

arr = np.array([1,-1,0.1])
x = np.arcsin(arr)
print("radian from array value", x)

base = 3
perp = 4
hypot = np.hypot(base,perp)
print("Hypotenues", hypot)