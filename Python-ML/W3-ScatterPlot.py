#machineLearning - ScatterPlot
import numpy as np
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("age")
plt.ylabel("speed")
plt.show()

#random data distribution
x = np.random.normal(5.0,1.0,1000)
y = np.random.normal(10.0,2.0,1000)

plt.scatter(x,y)
plt.title("Random Data Distribution")
plt.xlabel("x data")
plt.ylabel("y data")
plt.show()