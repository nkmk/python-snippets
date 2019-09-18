import numpy as np

a = np.array([0, 1, 2])
b = np.array([3, 0, 6])
c = np.array([1, 2, 3])

print(np.maximum.reduce([a, b, c]))
# [3 2 6]

print(np.maximum(np.maximum(a, b), c))
# [3 2 6]

print(np.fmax.reduce([a, b, c]))
# [3 2 6]

print(np.minimum.reduce([a, b, c]))
# [0 0 2]

print(np.fmin.reduce([a, b, c]))
# [0 0 2]

print(np.maximum.reduce((a, b, c)))
# [3 2 6]

# print(np.maximum.reduce(a, b, c))
# TypeError: data type not understood

a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

# print(np.maximum.reduce([a_2d, b, c]))
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(np.maximum(np.maximum(a_2d, b), c))
# [[3 2 6]
#  [3 4 6]]

# print(np.maximum.reduce([4, b, c]))
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(np.maximum(np.maximum(4, b), c))
# [4 4 6]

print(a)
# [0 1 2]

print(np.maximum.reduce(a))
# 2

print(a.max())
# 2

print(max(a))
# 2

a_2d = np.array([[0, 1, 2], [3, 0, 6], [1, 2, 3]])
print(a_2d)
# [[0 1 2]
#  [3 0 6]
#  [1 2 3]]

print(np.maximum.reduce(a_2d))
# [3 2 6]

print(np.maximum(np.maximum(a_2d[0], a_2d[1]), a_2d[2]))
# [3 2 6]

print(a_2d.max(axis=0))
# [3 2 6]
