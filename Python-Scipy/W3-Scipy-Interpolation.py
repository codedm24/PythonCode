#Scipy interpolation
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# print("1D interpolation")

# xs = np.arange(10)
# print("x coord data", xs)
# ys = 2 * xs + 1
# print("y coord data", ys)

# interp_func = interp1d(xs, ys)

# arr = np.arange(2.1,3,0.1)
# print("new x coord data", arr)
# newarr = interp_func(arr)
# print("using interpolation")
# print("new y coord data", newarr)

# print("using matplotlib to plot the coords")
# plt.plot(arr,newarr,marker='o')
# plt.title("X vs Y coordinates")
# plt.xlabel("X Coordinates")
# plt.ylabel("Y Coordinates")
# plt.show()

# print("using dataframe")

# dataset = {
#     "X": arr,
#     "Y" : newarr
# }

# df =pd.DataFrame(dataset)

# df.plot(x='X',y='Y',kind='line',marker='o')

# plt.title("X vs Y coordinates")
# plt.xlabel("X Coordinates")
# plt.ylabel("Y Coordinates")
# plt.show()

# print("2D interpolation")


# xs = np.arange(10)
# print("x coord data", xs)

# ys = xs**2 + np.sin(xs) + 1
# print("y coord data", ys)

# interp_func = UnivariateSpline(xs, ys)

# newxs = np.arange(2.1,3,0.1)
# print("new x coord values",newxs)
# print("doing 2d interpolation")
# newys = interp_func(newxs)
# print("interpolated ys value",newys)

# newdataset = {
#     "X":newxs,
#     "Y":newys
# }
# df =pd.DataFrame(newdataset)

# df.plot(x='X',y='Y',kind='line',marker='o')

# plt.title("X vs Y coordinates")
# plt.xlabel("X Coordinates")
# plt.ylabel("Y Coordinates")
# plt.show()

print('Interpolation with radial basis function')

xs = np.arange(10)
print("x coord value",xs)
ys = xs**2 + np.sin(xs) + 1
print('y coord value', ys)

interp_func = Rbf(xs,ys)

newxs = np.arange(2.1,3,0.1)
print('new x coord value',newxs)
print("Doing radial basis interpolation")
newys = interp_func(newxs)
print('new y coord value', newys)

dataset = {
    'X':newxs,
    'Y':newys
}

df = pd.DataFrame(dataset)

df.plot(x='X',y='Y',kind='line',marker='o')

plt.title('X vs Y Coordinate')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
