import numpy as np
from scipy.sparse import csr_matrix, csc_matrix
from scipy.sparse.linalg import inv, eigs

l = [[2, 5],
     [1, 3]]

csr = csr_matrix(l)
csc = csc_matrix(l)

# csr_inv = linalg.inv(csr)
# SparseEfficiencyWarning: splu requires CSC matrix format
# SparseEfficiencyWarning: spsolve is more efficient when sparse b is in the CSC matrix format

csc_inv = inv(csc)
print(csc_inv)
#   (0, 0)	3.0
#   (1, 0)	-1.0
#   (0, 1)	-5.0
#   (1, 1)	2.0

print(type(csc_inv))
# <class 'scipy.sparse.csc.csc_matrix'>

print(csc_inv.toarray())
# [[ 3. -5.]
#  [-1.  2.]]

l = [[1, 1, 2],
     [0, 2, -1],
     [0, 0, 3]]

w, v = np.linalg.eig(l)

print(w)
# [1. 2. 3.]

print(v)
# [[ 1.          0.70710678  0.33333333]
#  [ 0.          0.70710678 -0.66666667]
#  [ 0.          0.          0.66666667]]

csr_f = csr_matrix(l, dtype=float)
csr_i = csc_matrix(l, dtype=int)

w, v = eigs(csr_f, k=1)

print(w)
# [3.+0.j]

print(v)
# [[ 0.33333333+0.j]
#  [-0.66666667+0.j]
#  [ 0.66666667+0.j]]

# w, v = eigs(csr_f, k=2)
# TypeError: Cannot use scipy.linalg.eig for sparse A with k >= N - 1. Use scipy.linalg.eig(A.toarray()) or reduce k.

# w, v = eigs(csr_i, k=1)
# ValueError: matrix type must be 'f', 'd', 'F', or 'D'
