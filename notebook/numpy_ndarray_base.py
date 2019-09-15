import numpy as np

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

a_0 = a[:6]
print(a_0)
# [0 1 2 3 4 5]

a_1 = a_0.reshape(2, 3)
print(a_1)
# [[0 1 2]
#  [3 4 5]]

print(a_0.base)
# [0 1 2 3 4 5 6 7 8 9]

print(a_1.base)
# [0 1 2 3 4 5 6 7 8 9]

a_copy = a.copy()
print(a_copy)
# [0 1 2 3 4 5 6 7 8 9]

print(a_copy.base)
# None

print(a.base)
# None

print(a_0.base is None)
# False

print(a_copy.base is None)
# True

print(a.base is None)
# True

print(a_0.base is a)
# True

print(a_0.base is a_1.base)
# True
