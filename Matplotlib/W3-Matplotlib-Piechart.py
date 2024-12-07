#Matplotlib piechart
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
myexplode = [0.2,0,0,0]
mycolors = ["red","yellow","green","blue"]
plt.pie(y, labels=mylabels, startangle=90, explode = myexplode, shadow = True, colors=mycolors)
plt.legend(title = "Four Fruits:", loc="upper right")
plt.show()