import numpy as np
from scipy.sparse import csr_matrix

l = [[0, 10, 20],
     [30, 0, 40],
     [0, 0, 0]]

csr = csr_matrix(l)
print(csr)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30
#   (1, 2)	40

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

print(csr.shape)
# (3, 3)

a = np.array(l)
print(a)
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]

print(type(a))
# <class 'numpy.ndarray'>

csr = csr_matrix(a)
print(csr)
#   (0, 1)	10
#   (0, 2)	20
#   (1, 0)	30
#   (1, 2)	40

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

print(csr_matrix([0, 1, 2]))
#   (0, 1)	1
#   (0, 2)	2

print(csr_matrix([0, 1, 2]).shape)
# (1, 3)

# print(csr_matrix([[[0, 1, 2]]]))
# TypeError: expected dimension <= 2 array or matrix

print(csr.toarray())
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]

print(type(csr.toarray()))
# <class 'numpy.ndarray'>

print(csr.toarray().tolist())
# [[0, 10, 20], [30, 0, 40], [0, 0, 0]]

print(type(csr.toarray().tolist()))
# <class 'list'>

print(csr.todense())
# [[ 0 10 20]
#  [30  0 40]
#  [ 0  0  0]]

print(type(csr.todense()))
# <class 'numpy.matrix'>
