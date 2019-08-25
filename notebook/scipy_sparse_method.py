import numpy as np
from scipy.sparse import csr_matrix, lil_matrix

l = [[0, 1, 2],
     [3, 0, 4],
     [0, 0, 0]]

csr = csr_matrix(l)
lil = lil_matrix(l)

print(csr.sum())
# 10

print(csr.mean())
# 1.111111111111111

print(csr.max())
# 4

print(csr.min())
# 0

# print(lil.max())
# AttributeError: max not found

print(csr.sqrt().toarray())
# [[0.         1.         1.41421356]
#  [1.73205081 0.         2.        ]
#  [0.         0.         0.        ]]

print(csr.sin().toarray())
# [[ 0.          0.84147098  0.90929743]
#  [ 0.14112001  0.         -0.7568025 ]
#  [ 0.          0.          0.        ]]

print(csr.tan().toarray())
# [[ 0.          1.55740772 -2.18503986]
#  [-0.14254654  0.          1.15782128]
#  [ 0.          0.          0.        ]]

# print(lil.sqrt())
# AttributeError: sqrt not found

csr_ = csr.copy()

print(csr_.data)
# [1 2 3 4]

print(type(csr_.data))
# <class 'numpy.ndarray'>

csr_.data = np.cos(csr_.data)

print(csr_.toarray())
# [[ 0.          0.54030231 -0.41614684]
#  [-0.9899925   0.         -0.65364362]
#  [ 0.          0.          0.        ]]

csr_ = csr.copy()
csr_.data = csr_.data ** 2
print(csr_.toarray())
# [[ 0  1  4]
#  [ 9  0 16]
#  [ 0  0  0]]

print(lil.data)
# [list([1, 2]) list([3, 4]) list([])]

print(csr)
#   (0, 1)	1
#   (0, 2)	2
#   (1, 0)	3
#   (1, 2)	4

r, c = csr.nonzero()
print(r, c)
# [0 0 1 1] [1 2 0 2]

print(csr.count_nonzero())
# 4

print(csr.nnz)
# 4

csr[0, 1] = 0
print(csr)
#   (0, 1)	0
#   (0, 2)	2
#   (1, 0)	3
#   (1, 2)	4

print(csr.count_nonzero())
# 3

print(csr.nnz)
# 4

r, c = csr.nonzero()
print(r, c)
# [0 1 1] [2 0 2]

print(lil)
#   (0, 1)	1
#   (0, 2)	2
#   (1, 0)	3
#   (1, 2)	4

print(lil.nnz)
# 4

lil[0, 1] = 0

print(lil)
#   (0, 2)	2
#   (1, 0)	3
#   (1, 2)	4

print(lil.nnz)
# 3
