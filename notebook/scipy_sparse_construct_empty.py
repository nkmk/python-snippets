from scipy.sparse import csr_matrix, coo_matrix, lil_matrix

lil = lil_matrix((3, 3), dtype=int)
print(lil.toarray())
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

lil[1, 0] = 10
lil[2, 2] = 30

print(lil)
#   (1, 0)	10
#   (2, 2)	30

print(lil.toarray())
# [[ 0  0  0]
#  [10  0  0]
#  [ 0  0 30]]

lil[2, 2] = 0

print(lil)
#   (1, 0)	10

print(lil.toarray())
# [[ 0  0  0]
#  [10  0  0]
#  [ 0  0  0]]

csr = csr_matrix((3, 3), dtype=int)
print(csr.toarray())
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

# csr[1, 0] = 10
# SparseEfficiencyWarning: Changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient.

coo = coo_matrix((3, 3), dtype=int)

# coo[1, 0] = 10
# TypeError: 'coo_matrix' object does not support item assignment
