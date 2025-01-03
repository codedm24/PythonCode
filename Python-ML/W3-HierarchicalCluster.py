#Machine Learning - Hierarchical Clustering
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]

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


