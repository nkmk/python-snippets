import numpy as np

a = np.arange(3)
print(a)
# [0 1 2]

print(a.shape)
# (3,)

print(np.broadcast_to(a, (3, 3)))
# [[0 1 2]
#  [0 1 2]
#  [0 1 2]]

print(type(np.broadcast_to(a, (3, 3))))
# <class 'numpy.ndarray'>

# print(np.broadcast_to(a, (2, 2)))
# ValueError: operands could not be broadcast together with remapped shapes [original->remapped]: (3,) and requested shape (2,2)
