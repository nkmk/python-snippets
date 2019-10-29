import numpy as np

a = np.array([0, 0, 30, 10, 10, 20])
print(a)
# [ 0  0 30 10 10 20]

print(np.unique(a))
# [ 0 10 20 30]

print(type(np.unique(a)))
# <class 'numpy.ndarray'>

l = [0, 0, 30, 10, 10, 20]
print(l)
# [0, 0, 30, 10, 10, 20]

print(np.unique(l))
# [ 0 10 20 30]

print(type(np.unique(l)))
# <class 'numpy.ndarray'>

print(np.unique(a).size)
# 4

print(len(np.unique(a)))
# 4

u, counts = np.unique(a, return_counts=True)
print(u)
# [ 0 10 20 30]

print(counts)
# [2 2 1 1]

print(u[counts == 1])
# [20 30]

print(u[counts != 1])
# [ 0 10]

print(np.unique(a, return_counts=True))
# (array([ 0, 10, 20, 30]), array([2, 2, 1, 1]))

print(type(np.unique(a, return_counts=True)))
# <class 'tuple'>

u, indices = np.unique(a, return_index=True)
print(u)
# [ 0 10 20 30]

print(indices)
# [0 3 5 2]

print(a)
# [ 0  0 30 10 10 20]

print(a[indices])
# [ 0 10 20 30]

u, inverse = np.unique(a, return_inverse=True)
print(u)
# [ 0 10 20 30]

print(inverse)
# [0 0 3 1 1 2]

print(a)
# [ 0  0 30 10 10 20]

print(u[inverse])
# [ 0  0 30 10 10 20]

u, indices, inverse, counts = np.unique(a, return_index=True, return_inverse=True, return_counts=True)
print(u)
# [ 0 10 20 30]

print(indices)
# [0 3 5 2]

print(inverse)
# [0 0 3 1 1 2]

print(counts)
# [2 2 1 1]

print(np.unique(a, return_counts=True, return_index=True, return_inverse=True))
# (array([ 0, 10, 20, 30]), array([0, 3, 5, 2]), array([0, 0, 3, 1, 1, 2]), array([2, 2, 1, 1]))

a_2d = np.array([[20, 20, 10, 10], [0, 0, 10, 30], [20, 20, 10, 10]])
print(a_2d)
# [[20 20 10 10]
#  [ 0  0 10 30]
#  [20 20 10 10]]

print(np.unique(a_2d))
# [ 0 10 20 30]

print(np.unique(a_2d, axis=0))
# [[ 0  0 10 30]
#  [20 20 10 10]]

print(np.unique(a_2d, axis=1))
# [[10 10 20]
#  [10 30  0]
#  [10 10 20]]

print(a_2d[0])
# [20 20 10 10]

print(np.unique(a_2d[0]))
# [10 20]

print(a_2d[:, 2])
# [10 10 10]

print(np.unique(a_2d[:, 2]))
# [10]

print([np.unique(row) for row in a_2d])
# [array([10, 20]), array([ 0, 10, 30]), array([10, 20])]

print([np.unique(row).tolist() for row in a_2d])
# [[10, 20], [0, 10, 30], [10, 20]]

print([np.unique(row).size for row in a_2d])
# [2, 3, 2]

print(a_2d.T)
# [[20  0 20]
#  [20  0 20]
#  [10 10 10]
#  [10 30 10]]

print([np.unique(row) for row in a_2d.T])
# [array([ 0, 20]), array([ 0, 20]), array([10]), array([10, 30])]

print(a_2d.shape)
# (3, 4)

print([np.unique(a_2d[:, i]) for i in range(a_2d.shape[1])])
# [array([ 0, 20]), array([ 0, 20]), array([10]), array([10, 30])]

u, indices, inverse, counts = np.unique(a_2d, return_index=True, return_inverse=True, return_counts=True)
print(u)
# [ 0 10 20 30]

print(indices)
# [4 2 0 7]

print(a_2d.flatten())
# [20 20 10 10  0  0 10 30 20 20 10 10]

print(a_2d.flatten()[indices])
# [ 0 10 20 30]

print(inverse)
# [2 2 1 1 0 0 1 3 2 2 1 1]

print(u[inverse])
# [20 20 10 10  0  0 10 30 20 20 10 10]

print(u[inverse].reshape(a_2d.shape))
# [[20 20 10 10]
#  [ 0  0 10 30]
#  [20 20 10 10]]

print(counts)
# [2 5 4 1]

u, indices, inverse, counts = np.unique(a_2d, axis=0, return_index=True, return_inverse=True, return_counts=True)
print(u)
# [[ 0  0 10 30]
#  [20 20 10 10]]

print(indices)
# [1 0]

print(a_2d[indices])
# [[ 0  0 10 30]
#  [20 20 10 10]]

print(inverse)
# [1 0 1]

print(u[inverse])
# [[20 20 10 10]
#  [ 0  0 10 30]
#  [20 20 10 10]]

print(counts)
# [1 2]

u, indices = np.unique(a_2d, return_index=True)
print(u)
# [ 0 10 20 30]

print(a_2d.flatten())
# [20 20 10 10  0  0 10 30 20 20 10 10]

print(indices)
# [4 2 0 7]

print(list(zip(*np.where(a_2d == 0))))
# [(1, 0), (1, 1)]

d = {u: list(zip(*np.where(a_2d == u))) for u in np.unique(a_2d)}
print(d)
# {0: [(1, 0), (1, 1)], 10: [(0, 2), (0, 3), (1, 2), (2, 2), (2, 3)], 20: [(0, 0), (0, 1), (2, 0), (2, 1)], 30: [(1, 3)]}

print(d[0])
# [(1, 0), (1, 1)]

print(d[10])
# [(0, 2), (0, 3), (1, 2), (2, 2), (2, 3)]

print(d[20])
# [(0, 0), (0, 1), (2, 0), (2, 1)]

print(d[30])
# [(1, 3)]
