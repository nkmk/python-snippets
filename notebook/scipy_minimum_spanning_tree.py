import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix

l = [[0, 8, 0, 3],
     [0, 0, 2, 5],
     [0, 0, 0, 6],
     [0, 0, 0, 0]]

mst = minimum_spanning_tree(l)
print(mst)
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0

print(type(mst))
# <class 'scipy.sparse.csr.csr_matrix'>

print(mst.toarray())
# [[0. 0. 0. 3.]
#  [0. 0. 2. 5.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print(mst.toarray().astype(int))
# [[0 0 0 3]
#  [0 0 2 5]
#  [0 0 0 0]
#  [0 0 0 0]]

print(mst.astype(int).toarray())
# [[0 0 0 3]
#  [0 0 2 5]
#  [0 0 0 0]
#  [0 0 0 0]]

a = np.array(l)
print(a)
# [[0 8 0 3]
#  [0 0 2 5]
#  [0 0 0 6]
#  [0 0 0 0]]

print(type(a))
# <class 'numpy.ndarray'>

print(minimum_spanning_tree(a))
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0

csr = csr_matrix(l)
print(csr)
#   (0, 1)	8
#   (0, 3)	3
#   (1, 2)	2
#   (1, 3)	5
#   (2, 3)	6

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

print(minimum_spanning_tree(csr))
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0

print(minimum_spanning_tree(coo_matrix(l)))
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0

print(minimum_spanning_tree(lil_matrix(l)))
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0

n = 4
d = [8, 3, 2, 5, 6]
i = [0, 0, 1, 1, 2]
j = [1, 3, 2, 3, 3]

csr_ = csr_matrix((d, (i, j)), shape=(n, n))
print(csr_)
#   (0, 1)	8
#   (0, 3)	3
#   (1, 2)	2
#   (1, 3)	5
#   (2, 3)	6

print(csr_.toarray())
# [[0 8 0 3]
#  [0 0 2 5]
#  [0 0 0 6]
#  [0 0 0 0]]

print(minimum_spanning_tree(csr))
#   (0, 3)	3.0
#   (1, 2)	2.0
#   (1, 3)	5.0

print(mst.toarray().astype(int).tolist())
# [[0, 0, 0, 3], [0, 0, 2, 5], [0, 0, 0, 0], [0, 0, 0, 0]]

print(type(mst.toarray().astype(int).tolist()))
# <class 'list'>

print(mst.sum())
# 10.0

print(int(mst.sum()))
# 10

r, c = mst.nonzero()
print(r, c)
# [0 1 1] [3 2 3]

print(list(zip(*mst.nonzero())))
# [(0, 3), (1, 2), (1, 3)]

print(mst.data)
# [3. 2. 5.]

print(list(zip(*mst.nonzero(), mst.data.astype(int))))
# [(0, 3, 3), (1, 2, 2), (1, 3, 5)]

l = [[0, 8, 0, 3],
     [8, 0, 2, 5],
     [0, 2, 0, 6],
     [3, 5, 6, 0]]

print(minimum_spanning_tree(l).toarray().astype(int))
# [[0 0 0 3]
#  [0 0 2 5]
#  [0 0 0 0]
#  [0 0 0 0]]

l = [[0, 8, 0, 3],
     [100, 0, 2, 5],
     [100, 100, 0, 6],
     [100, 100, 100, 0]]

print(minimum_spanning_tree(l).toarray().astype(int))
# [[0 0 0 3]
#  [0 0 2 5]
#  [0 0 0 0]
#  [0 0 0 0]]

l = [[0, 8, 0, 3],
     [0, 0, 100, 5],
     [0, 2, 0, 6],
     [0, 0, 0, 0]]

print(minimum_spanning_tree(l).toarray().astype(int))
# [[0 0 0 3]
#  [0 0 0 5]
#  [0 2 0 0]
#  [0 0 0 0]]
