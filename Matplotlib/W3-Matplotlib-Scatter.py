#Matplotlib scatter
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#plt.scatter(x,y, color='hotpink')

#color for each dots
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
#plt.scatter(x,y,color=colors, cmap='virdis')

#size for each dots
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#plt.scatter(x,y,s=sizes)

#Transparency
plt.scatter(x,y,s=sizes,alpha=0.5)


#day two, the age and speed of 15 cars
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x,y,color='#88c999')

#color for each dot
plt.colorbar()

plt.show()

#Combine color,size,alpha
x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
colors = np.random.randint(100,size=(100))
sizes = 10 * np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()