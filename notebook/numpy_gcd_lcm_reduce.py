import numpy as np

a = np.array([0, 2, 3, 6])
b = np.array([3, 4, 5, 15])
c = np.array([6, 8, 9, 9])

print(np.gcd.reduce([a, b, c]))
# [3 2 1 3]

print(np.gcd(np.gcd(a, b), c))
# [3 2 1 3]

print(np.lcm.reduce([a, b, c]))
# [ 0  8 45 90]

print(np.gcd.reduce([6, 9, 12, 15]))
# 3

print(np.gcd.reduce((a, b, c)))
# [3 2 1 3]

# print(np.gcd.reduce(a, b, c))
# TypeError: data type not understood

a_2d = np.array([[0, 2, 3, 6], [0, 2, 3, 6]])
print(a_2d)
# [[0 2 3 6]
#  [0 2 3 6]]

# print(np.gcd.reduce([a, b, a_2d]))
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(np.gcd(np.gcd(a, b), a_2d))
# [[3 2 1 3]
#  [3 2 1 3]]

# print(np.gcd.reduce([a, b, 9]))
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

print(np.gcd(np.gcd(a, b), 9))
# [3 1 1 3]

a_1d = np.array([4, 6, 12])

print(np.gcd.reduce(a_1d))
# 2

print(np.lcm.reduce(a_1d))
# 12

a_2d = np.array([[4, 6, 12], [2, 12, 16]])
print(a_2d)
# [[ 4  6 12]
#  [ 2 12 16]]

print(np.gcd.reduce(a_2d))
# [2 6 4]

print(np.gcd(a_2d[0], a_2d[1]))
# [2 6 4]

print(a_2d.ravel())
# [ 4  6 12  2 12 16]

print(np.gcd.reduce(a_2d.ravel()))
# 2

print(np.lcm.reduce(a_2d.ravel()))
# 48
