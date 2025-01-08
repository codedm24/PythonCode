#Machine Learning - K-means
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]

#plot dataset
plt.scatter(X,y)
plt.show()

#create model data
data = list(zip(X,y))
inertias = []

for i in range(1,11):
    model = KMeans(n_clusters=i)
    model.fit(data)
    inertias.append(model.inertia_)

plt.plot(range(1,11),inertias,marker='o')    
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

#use the best value of K as per the plot of cluster with inertia
model = KMeans(n_clusters=2)
model.fit(data)
centroid = model.cluster_centers_
print(f"Cluster Centroid: {centroid}")
plt.scatter(X,y,c=model.labels_,cmap='rainbow')
plt.scatter(centroid[:,0],centroid[:,1],c='green',s=100,marker='X')
plt.show()

