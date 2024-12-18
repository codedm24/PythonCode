#MachineLearning - Data Distribution
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0,5.0,250)

#print(f"Data distribution: {x}")

#draw histogram
plt.hist(x, 5)
plt.show()

#draw histogram for big dataset
x = np.random.uniform(0.0,5.0,100000)

plt.hist(x,100)
plt.show()