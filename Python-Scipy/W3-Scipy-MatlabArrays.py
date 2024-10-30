#Scipy matlab arrays
from scipy import io
import numpy as np
import os

arr = np.arange(10)
print("data to save")
print(arr)
print("save matlab data in .mat file")
io.savemat("arr.mat",{"vec":arr})

print("import data from .mat file")

filename ="arr.mat"
if(os.path.exists(filename)):
    arr = io.loadmat(filename,squeeze_me = True)
    print("data from file")
    print(arr)
    print(arr['vec'])