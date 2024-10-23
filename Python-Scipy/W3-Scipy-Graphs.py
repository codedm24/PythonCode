#Scipy Graphs
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array(
   [[0,1,2],
    [1,0,0],
    [2,0,0]]
)

newarr = csr_matrix(arr)
print("connected components")
print(connected_components(newarr))

print("find shortest path - dijkstra - from 1 to 2")
print(dijkstra(newarr,return_predecessors=True,indices=0))

print("find shortest path between all components - floyd_warshall")
newarr = csr_matrix(arr)
print(floyd_warshall(newarr,return_predecessors=True))

print("find shortest path between all components - bellman_ford")

arr = np.array([
    [0,-1,2],
    [1,0,0],
    [2,0,0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr,return_predecessors=True,indices=0))

print("depth first order")

arr = np.array([
    [0,1,0,1],
    [1,1,1,1],
    [2,1,1,0],
    [0,1,0,1]
])

newarr = csr_matrix(arr)
print(depth_first_order(newarr,1))

print("breadth first order")
print(breadth_first_order(newarr,1))