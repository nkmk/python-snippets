from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

l = [[1, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 3, 0],
     [0, 0, 0, 4]]

csr = csr_matrix(l)
csc = csc_matrix(l)
coo = coo_matrix(l)
lil = lil_matrix(l)

print(csr[1, 1])
# 2

print(csc[1, 1])
# 2

print(lil[1, 1])
# 2

# print(coo[1, 1])
# TypeError: 'coo_matrix' object is not subscriptable

lil[0, 0] = 10
lil[0, 1] = 100

print(lil)
#   (0, 0)	10
#   (0, 1)	100
#   (1, 1)	2
#   (2, 2)	3
#   (3, 3)	4

print(lil.toarray())
# [[ 10 100   0   0]
#  [  0   2   0   0]
#  [  0   0   3   0]
#  [  0   0   0   4]]

lil[1, 1] = 0

print(lil)
#   (0, 0)	10
#   (0, 1)	100
#   (2, 2)	3
#   (3, 3)	4

print(lil.toarray())
# [[ 10 100   0   0]
#  [  0   0   0   0]
#  [  0   0   3   0]
#  [  0   0   0   4]]

csr[0, 0] = 10

# csr[0, 1] = 100
# SparseEfficiencyWarning: Changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient.

csr[1, 1] = 0

print(csr)
#   (0, 0)	10
#   (1, 1)	0
#   (2, 2)	3
#   (3, 3)	4

print(csr.toarray())
# [[10  0  0  0]
#  [ 0  0  0  0]
#  [ 0  0  3  0]
#  [ 0  0  0  4]]
