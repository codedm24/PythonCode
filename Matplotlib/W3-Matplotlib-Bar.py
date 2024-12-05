#Matplotlib bar
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

#horizontal bar
# plt.barh(x,y)
# plt.show() 

#add color
# plt.bar(x,y, color='red')
# plt.show()

#bar width
# plt.bar(x,y, color='red', width=0.1)
# plt.show()

#bar height
plt.barh(x,y, color='red', height=0.1)
plt.show()