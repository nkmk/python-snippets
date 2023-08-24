l = [0, 1, 2, 3]

print(len(l))
# 4

l_length = len(l)

print(l_length)
# 4

print(type(l_length))
# <class 'int'>

l_2d = [[0, 1, 2], [3, 4, 5]]

print(len(l_2d))
# 2

print([len(v) for v in l_2d])
# [3, 3]

print(sum(len(v) for v in l_2d))
# 6

import numpy as np

l_2d = [[0, 1, 2], [3, 4, 5]]
arr_2d = np.array(l_2d)

print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

print(arr_2d.size)
# 6

print(arr_2d.shape)
# (2, 3)

l_multi = [[0, 1, 2, [10, 20, 30]], [3, 4, 5], 100]

print(len(l_multi))
# 3

# arr_multi = np.array(l_multi)
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions.
# The detected shape was (3,) + inhomogeneous part.

def my_len(l):
    count = 0
    if isinstance(l, list):
        for v in l:
            count += my_len(v)
        return count
    else:
        return 1

l_multi = [[0, 1, 2, [10, 20, 30]], [3, 4, 5], 100]
print(my_len(l_multi))
# 10

l_2d = [[0, 1, 2], [3, 4, 5]]
print(my_len(l_2d))
# 6

l = [0, 1, 2, 3]
print(my_len(l))
# 4

print(my_len(100))
# 1

def my_len_wrapper(l):
    if isinstance(l, list):
        return my_len(l)
    else:
        return None

print(my_len_wrapper(l_multi))
# 10

print(my_len_wrapper(l_2d))
# 6

print(my_len_wrapper(l))
# 4

print(my_len_wrapper(100))
# None
