l = [0, 10, 20, 30, 40, 50, 60]

print(l[2:5])
# [20, 30, 40]

print(l[:3])
# [0, 10, 20]

print(l[3:])
# [30, 40, 50, 60]

print(l[:])
# [0, 10, 20, 30, 40, 50, 60]

print(l[2:10])
# [20, 30, 40, 50, 60]

print(l[5:2])
# []

print(l[2:2])
# []

print(l[10:20])
# []

l = [0, 10, 20, 30, 40, 50, 60]

print(l[::2])
# [0, 20, 40, 60]

print(l[1::2])
# [10, 30, 50]

print(l[::3])
# [0, 30, 60]

print(l[2:5:2])
# [20, 40]

l = [0, 10, 20, 30, 40, 50, 60]

print(l[3:-1])
# [30, 40, 50]

print(l[-2:])
# [50, 60]

print(l[-5:-2])
# [20, 30, 40]

l = [0, 10, 20, 30, 40, 50, 60]

print(l[5:2:-1])
# [50, 40, 30]

print(l[2:5:-1])
# []

print(l[-2:-5:-1])
# [50, 40, 30]

print(l[-2:2:-1])
# [50, 40, 30]

print(l[5:2:-2])
# [50, 30]

print(l[:3:-1])
# [60, 50, 40]

print(l[3::-1])
# [30, 20, 10, 0]

print(l[::-1])
# [60, 50, 40, 30, 20, 10, 0]

l = [0, 10, 20, 30, 40, 50, 60]

sl = slice(2, 5, 2)
print(sl)
# slice(2, 5, 2)

print(type(sl))
# <class 'slice'>

print(l[sl])
# [20, 40]

sl = slice(2, 5)
print(sl)
# slice(2, 5, None)

print(l[sl])
# [20, 30, 40]

sl = slice(2)
print(sl)
# slice(None, 2, None)

print(l[sl])
# [0, 10]

# sl = slice()
# TypeError: slice expected at least 1 arguments, got 0

sl = slice(None)
print(sl)
# slice(None, None, None)

print(l[sl])
# [0, 10, 20, 30, 40, 50, 60]

l = [0, 10, 20, 30, 40, 50, 60]

l[2:5] = [200, 300, 400]
print(l)
# [0, 10, 200, 300, 400, 50, 60]

l[2:5] = [-2, -3]
print(l)
# [0, 10, -2, -3, 50, 60]

l[2:4] = [2000, 3000, 4000, 5000]
print(l)
# [0, 10, 2000, 3000, 4000, 5000, 50, 60]

l[2:6] = [20000]
print(l)
# [0, 10, 20000, 50, 60]

# l[2:3] = 200
# TypeError: can only assign an iterable

l[2:3] = [200]
print(l)
# [0, 10, 200, 50, 60]

l[1:4] = []
print(l)
# [0, 60]

l = [0, 10, 20, 30, 40, 50, 60]

l[100:200] = [-1, -2, -3]
print(l)
# [0, 10, 20, 30, 40, 50, 60, -1, -2, -3]

l[2:2] = [-100]
print(l)
# [0, 10, -100, 20, 30, 40, 50, 60, -1, -2, -3]

l = [0, 10, 20, 30, 40, 50, 60]

l[1::2] = [100, 200, 300]
print(l)
# [0, 100, 20, 200, 40, 300, 60]

# l[1::2] = [100, 200]
# ValueError: attempt to assign sequence of size 2 to extended slice of size 3

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

print(l_2d[1:3])
# [[3, 4, 5], [6, 7, 8]]

print([l[:2] for l in l_2d[1:3]])
# [[3, 4], [6, 7]]

l_2d_t = [list(x) for x in zip(*l_2d)]
print(l_2d_t)
# [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]]

print(l_2d_t[1])
# [1, 4, 7, 10]

l = [0, 10, 20, 30, 40, 50, 60]

l_slice = l[2:5]
print(l_slice)
# [20, 30, 40]

l_slice[1] = 300
print(l_slice)
# [20, 300, 40]

print(l)
# [0, 10, 20, 30, 40, 50, 60]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

l_2d_slice = l_2d[1:3]
print(l_2d_slice)
# [[3, 4, 5], [6, 7, 8]]

l_2d_slice[0][1] = 400
print(l_2d_slice)
# [[3, 400, 5], [6, 7, 8]]

print(l_2d)
# [[0, 1, 2], [3, 400, 5], [6, 7, 8], [9, 10, 11]]

import copy

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

l_2d_slice_deepcopy = copy.deepcopy(l_2d[1:3])
print(l_2d_slice_deepcopy)
# [[3, 4, 5], [6, 7, 8]]

l_2d_slice_deepcopy[0][1] = 400
print(l_2d_slice_deepcopy)
# [[3, 400, 5], [6, 7, 8]]

print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

s = 'abcdefg'

print(s[2:5])
# cde

print(s[::-1])
# gfedcba

# s[2:5] = 'CDE'
# TypeError: 'str' object does not support item assignment

t = (0, 10, 20, 30, 40, 50, 60)

print(t[2:5])
# (20, 30, 40)

# t[2:5] = (200, 300, 400)
# TypeError: 'tuple' object does not support item assignment
