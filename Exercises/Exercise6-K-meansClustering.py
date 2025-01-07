#Machine Learning - K-means Clustering
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Create a sample dataset
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
print(X)
print(X.shape)
print(f"X[:,0]: {X[:,0]}")
print(f"X[:,1]: {X[:,1]}")
# Fit the KMeans model
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

inertias = []
for i in range(1,11):
    model = KMeans(n_clusters=i)
    model.fit(X)
    print(f"Model inertia for {i} clusters: {model.inertia_}")
    inertias.append(model.inertia_)
plt.plot(range(1,11),inertias,marker='o')    
plt.title("Elbow method")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()


# Get the cluster centroids
centroids = kmeans.cluster_centers_
print("Cluster centroids:\n", centroids)

# Plot the data points
plt.scatter(X[:, 0], X[:, 1], s=50, c=kmeans.labels_, cmap='viridis')

# Plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X')
plt.title('K-means Clustering with Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

