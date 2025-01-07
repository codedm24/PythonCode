#Machine Learning - Hierarchical Clustering
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import os, sys

#Set current directory
print(f'Current directory:{os.getcwd()}')
os.chdir('Python-ML')
print(f'Current directory:{os.getcwd()}')

#Dataset 
x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#Dataset from csv file
#df =pd.read_csv('data.csv')
#print(df.info())

#x = df["Volume"]
#y = df["CO2"]
#print(f"x:{x}")
#print(f"y:{y}")
#sys.exit()

plt.scatter(x,y)
plt.show()


#Using scipy -  dendrogram, linkage
data = list(zip(x,y))

linkage_data = linkage(data, method='ward', metric = 'euclidean')
dendrogram(linkage_data)

plt.show()

#Using scikit-learn AgglomerativeClustering

hierarchicl_clustring = AgglomerativeClustering(n_clusters = 2, linkage = 'ward')
labels = hierarchicl_clustring.fit_predict(data)
plt.scatter(x, y, c=labels)
plt.show()


