import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

l = [[0, 1, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

# n, labels = connected_components(l)
# AttributeError: 'list' object has no attribute 'dtype'

a = np.array(l)
print(type(a))
# <class 'numpy.ndarray'>

n, labels = connected_components(a)

print(n)
# 2

print(labels)
# [0 0 0 1 1]

csr = csr_matrix(l)
print(csr)
#   (0, 1)	1
#   (0, 2)	1
#   (1, 2)	1
#   (3, 4)	1

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

n, labels = connected_components(csr)

print(n)
# 2

print(labels)
# [0 0 0 1 1]

n = 5
d = [1, 1, 1, 1]
i = [0, 0, 1, 3]
j = [1, 2, 2, 4]

csr = csr_matrix((d, (i, j)), (n, n))
print(csr)
#   (0, 1)	1
#   (0, 2)	1
#   (1, 2)	1
#   (3, 4)	1

print(connected_components(csr, return_labels=False))
# 2

ld = [[0, 1, 1, 0, 0],
      [1, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1],
      [0, 0, 0, 1, 0]]

n, labels = connected_components(csr_matrix(ld))

print(n)
# 2

print(labels)
# [0 0 0 1 1]

n, labels = connected_components(csr_matrix(ld), connection='strong')

print(n)
# 3

print(labels)
# [1 1 0 2 2]

ld2 = [[0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0]]

n, labels = connected_components(csr_matrix(ld2), connection='strong')

print(n)
# 2

print(labels)
# [0 0 0 1 1]

n, labels = connected_components(csr_matrix(ld), directed=False, connection='strong')

print(n)
# 2

print(labels)
# [0 0 0 1 1]

lw = [[0, 8, 5.2, 0, 0],
      [0, 0, 3, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, -2],
      [0, 0, 0, 0, 0]]

n, labels = connected_components(csr_matrix(lw))

print(n)
# 2

print(labels)
# [0 0 0 1 1]
