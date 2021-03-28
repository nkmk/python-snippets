l = [-2, -1, 0]
print(map(abs, l))
# <map object at 0x10651a400>

print(type(map(abs, l)))
# <class 'map'>

for i in map(abs, l):
    print(i)
# 2
# 1
# 0

for i in l:
    print(abs(i))
# 2
# 1
# 0

print(list(map(abs, l)))
# [2, 1, 0]

l_s = ['apple', 'orange', 'strawberry']
print(list(map(len, l_s)))
# [5, 6, 10]

print(list(map(abs, range(-2, 1))))
# [2, 1, 0]

l = [-2, -1, 0]
print(list(map(lambda x: x**2, l)))
# [4, 1, 0]

def square(x):
    return x**2

print(list(map(square, l)))
# [4, 1, 0]

l_1 = [1, 2, 3]
l_2 = [10, 20, 30]
print(list(map(lambda x, y: x * y, l_1, l_2)))
# [10, 40, 90]

# print(list(map(abs, l_1, l_2)))
# TypeError: abs() takes exactly one argument (2 given)

l_3 = [100, 200, 300, 400]
print(list(map(lambda x, y, z: x * y * z, l_1, l_2, l_3)))
# [1000, 8000, 27000]

l = [-2, -1, 0]
print([abs(x) for x in l])
# [2, 1, 0]

print([x**2 for x in l])
# [4, 1, 0]

l_1 = [1, 2, 3]
l_2 = [10, 20, 30]
print([x * y for x, y in zip(l_1, l_2)])
# [10, 40, 90]

import numpy as np

a = np.array([-2, -1, 0])
print(np.abs(a))
# [2 1 0]

print(a**2)
# [4 1 0]

a_1 = np.array([1, 2, 3])
a_2 = np.array([10, 20, 30])
print(a_1 * a_2)
# [10 40 90]
