#Scipy Spatial Data
import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt

index = 6

if( index == 0):
    #Triangulation
    points = np.array([
        [2,4],
        [3,4],
        [3,0],
        [2,2],
        [4,1]])

    simplices = Delaunay(points).simplices

    plt.triplot(points[:,0],points[:,1],simplices)
    plt.scatter(points[:,0],points[:,1],color='r')

    plt.show()
elif (index == 1):
    #Convex hull
    points = np.array([
        [2,4],
        [3,4],
        [3,0],
        [2,2],
        [4,1],
        [1,2],
        [5,0],
        [3,1],
        [1,2],
        [0,2]
    ])

    hull = ConvexHull(points)
    hull_points = hull.simplices

    for x in points[:,0]:
        print(x)

    plt.scatter(points[:,0],points[:,1])
    for simplex in hull_points:
        plt.plot(points[simplex,0],points[simplex,1],'k-')

    plt.show()

elif(index==2):

    #KDTrees
    points = np.array([
        (1,-1),
        (2,3),
        (-2,3),
        (2,-3)
    ])

    kdtree = KDTree(points)

    res = kdtree.query((1,1))

    print(res)
elif(index==3):
    #euclidean distance

    p1 = (1,0)
    p2 = (10,2)

    res = euclidean(p1,p2)

    print(res)

elif(index == 4):

    p1 = (1,0)
    p2 = (10,2)

    res = cityblock(p1, p2)

    print(res)

elif(index == 5):
    p1 = (1,0)
    p2 = (10,2)

    res = cosine(p1,p2)

    print(res)
elif(index == 6):
    p1 = (True,False,True)
    p2 = (False,True,True)

    res = hamming(p1,p2)

    print(res)