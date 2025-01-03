#MachineLearning - Polynomial Regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x,y)
plt.title('Scatter plot of speed and hour of the day')
plt.xlabel('Hour of the day')
plt.ylabel('Speed')
plt.show()

#polynominal regression
print(np.polyfit(x,y,3))
mymodel = np.poly1d(np.polyfit(x,y,3))

myline = np.linspace(1,22,100)

print(myline)
print(len(myline))

plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()

print(r2_score(y, mymodel(x)))

speed = mymodel(17)

print(f"speed: {speed}")

#bad fit polynomial
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = np.poly1d(np.polyfit(x,y,3))
myline =  np.linspace(2,95,100)
plt.scatter(x,y)
plt.plot(myline, mymodel(myline))
plt.show()  

print(f"Score: {r2_score(y, mymodel(x))}")