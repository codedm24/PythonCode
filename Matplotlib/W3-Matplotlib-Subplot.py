#Matplotlib Subplot
import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

#Layout style 1
#plt.subplot(1,2,1)
#Layout style 2
plt.subplot(2, 1, 1)

plt.plot(x,y)
plt.title("Sales")

plt.grid()

#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

#Layout style 1
#plt.subplot(1,2,2)
#layout style 2
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.title("Income")
plt.grid()
plt.suptitle("My Shop")
plt.show()


x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,2)
plt.plot(x,y)

x= np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,3)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,4)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,3,5)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,6)
plt.plot(x,y)

plt.show()