#Scipy SparseData
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix

arr = np.array([0,0,0,0,0,1,1,0,2])
print("CSR matrix")
print(csr_matrix(arr))

print("CSC matrix")
print(csc_matrix(arr))

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
print("CSR matrix")
csrm = csr_matrix(arr)
print(csr_matrix(arr))
print("csr matrix data")
print(csrm.data)
print("count nonzero items")
print(csrm.count_nonzero())
print("eliminate zeros")
csrm.eliminate_zeros()
print(csrm)
print("sum duplicates")
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
csrm = csr_matrix(arr)
csrm.sum_duplicates()
print(csrm)
print("csr to csm")
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)
