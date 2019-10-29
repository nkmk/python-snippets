import numpy as np

a_2d = np.array([[10, 20, 30], [30, 20, 10]])
print(a_2d)
# [[10 20 30]
#  [30 20 10]]

print(np.max(a_2d))
# 30

print(np.min(a_2d))
# 10

print(np.unravel_index(np.argmax(a_2d), a_2d.shape))
# (0, 2)

print(np.unravel_index(np.argmin(a_2d), a_2d.shape))
# (0, 0)

print(np.where(a_2d == np.max(a_2d)))
# (array([0, 1]), array([2, 0]))

print(list(zip(*np.where(a_2d == np.max(a_2d)))))
# [(0, 2), (1, 0)]

print(np.where(a_2d == np.min(a_2d)))
# (array([0, 1]), array([0, 2]))

print(list(zip(*np.where(a_2d == np.min(a_2d)))))
# [(0, 0), (1, 2)]
