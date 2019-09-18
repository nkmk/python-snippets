import numpy as np

a = np.array([0, 2, 3, 6])
b = np.array([3, 4, 5, 15])

print(np.gcd(a, b))
# [3 2 1 3]

print(type(np.gcd(a, b)))
# <class 'numpy.ndarray'>

l_a = [0, 2, 3, 6]
l_b = [3, 4, 5, 14]

print(np.gcd(l_a, l_b))
# [3 2 1 2]

print(type(np.gcd(l_a, l_b)))
# <class 'numpy.ndarray'>

print(np.gcd(6, 15))
# 3

print(type(np.gcd(6, 15)))
# <class 'numpy.int64'>

a_2d = np.array([[0, 2, 3, 6], [0, 2, 3, 6]])
print(a_2d)
# [[0 2 3 6]
#  [0 2 3 6]]

print(b)
# [ 3  4  5 15]

print(a_2d + b)
# [[ 3  6  8 21]
#  [ 3  6  8 21]]

print(np.gcd(a_2d, b))
# [[3 2 1 3]
#  [3 2 1 3]]

a_mismatch = np.array([0, 1, 2])

# print(np.gcd(a_mismatch, b))
# ValueError: operands could not be broadcast together with shapes (3,) (4,)

print(np.gcd(a, 15))
# [15  1  3  3]

print(np.gcd(15, a))
# [15  1  3  3]
