import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix

l = [[1, 0, 0, 0],
     [0, 2, 0, 0],
     [0, 0, 3, 0],
     [0, 0, 0, 4]]

csr = csr_matrix(l)
csc = csc_matrix(l)
lil = lil_matrix(l)

print(csr[0, :])
#   (0, 0)	1

print(csr[0, :].toarray())
# [[1 0 0 0]]

print(csr[0].toarray())
# [[1 0 0 0]]

print(csr[:, 0])
#   (0, 0)	1

print(csr[:, 0].toarray())
# [[1]
#  [0]
#  [0]
#  [0]]

print(csr[1:3, 1:3])
#   (0, 0)	2
#   (1, 1)	3

print(csr[1:3, 1:3].toarray())
# [[2 0]
#  [0 3]]

print(csr[:, ::2])
#   (0, 0)	1
#   (2, 1)	3

print(csr[:, ::2].toarray())
# [[1 0]
#  [0 0]
#  [0 3]
#  [0 0]]

print(type(csr[0]))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(csc[0]))
# <class 'scipy.sparse.csc.csc_matrix'>

print(type(lil[0]))
# <class 'scipy.sparse.lil.lil_matrix'>

print(type(csr[:, 0]))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(csc[:, 0]))
# <class 'scipy.sparse.csc.csc_matrix'>

print(type(lil[:, 0]))
# <class 'scipy.sparse.lil.lil_matrix'>

print(type(csr[1:3, 1:3]))
# <class 'scipy.sparse.csr.csr_matrix'>

print(type(csc[1:3, 1:3]))
# <class 'scipy.sparse.csc.csc_matrix'>

print(type(lil[1:3, 1:3]))
# <class 'scipy.sparse.lil.lil_matrix'>

csr_slice = csr[1:3, 1:3]
csr_slice[0, 0] = 100

print(csr.toarray())
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

print(csr_slice.toarray())
# [[100   0]
#  [  0   3]]

csc_slice = csc[1:3, 1:3]
csc_slice[0, 0] = 100

print(csc.toarray())
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

print(csc_slice.toarray())
# [[100   0]
#  [  0   3]]

lil_slice = lil[1:3, 1:3]
lil_slice[0, 0] = 100

print(lil.toarray())
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

print(lil_slice.toarray())
# [[100   0]
#  [  0   3]]

lil[0] = [10, 20, 30, 40]

print(lil)
#   (0, 0)	10
#   (0, 1)	20
#   (0, 2)	30
#   (0, 3)	40
#   (1, 1)	2
#   (2, 2)	3
#   (3, 3)	4

print(lil.toarray())
# [[10 20 30 40]
#  [ 0  2  0  0]
#  [ 0  0  3  0]
#  [ 0  0  0  4]]

lil[1:3, 1:3] = np.arange(4).reshape(2, 2) * 100

print(lil)
#   (0, 0)	10
#   (0, 1)	20
#   (0, 2)	30
#   (0, 3)	40
#   (1, 2)	100
#   (2, 1)	200
#   (2, 2)	300
#   (3, 3)	4

print(lil.toarray())
# [[ 10  20  30  40]
#  [  0   0 100   0]
#  [  0 200 300   0]
#  [  0   0   0   4]]

lil[:, 0] = csr[:, 3]

print(lil)
#   (0, 1)	20
#   (0, 2)	30
#   (0, 3)	40
#   (1, 2)	100
#   (2, 1)	200
#   (2, 2)	300
#   (3, 0)	4
#   (3, 3)	4

print(lil.toarray())
# [[  0  20  30  40]
#  [  0   0 100   0]
#  [  0 200 300   0]
#  [  4   0   0   4]]

# lil[1:3, 1:3] = [10, 20, 30, 40]
# ValueError: shape mismatch: objects cannot be broadcast to a single shape

csr[0] = [0, 0, 0, 100]
# /usr/local/lib/python3.7/site-packages/scipy/sparse/_index.py:127: SparseEfficiencyWarning: Changing the sparsity structure of a csr_matrix is expensive. lil_matrix is more efficient.
#   self._set_arrayXarray(i, j, x)

print(csr)
#   (0, 0)	0
#   (0, 1)	0
#   (0, 2)	0
#   (0, 3)	100
#   (1, 1)	2
#   (2, 2)	3
#   (3, 3)	4

print(csr.toarray())
# [[  0   0   0 100]
#  [  0   2   0   0]
#  [  0   0   3   0]
#  [  0   0   0   4]]
