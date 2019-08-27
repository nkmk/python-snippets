l_empty = []
print(l_empty)
# []

print(len(l_empty))
# 0

l_empty.append(100)
l_empty.append(200)
print(l_empty)
# [100, 200]

l_empty.remove(100)
print(l_empty)
# [200]

l = [0] * 10
print(l)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(len(l))
# 10

print([0, 1, 2] * 3)
# [0, 1, 2, 0, 1, 2, 0, 1, 2]

l_2d_ng = [[0] * 4] * 3
print(l_2d_ng)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

l_2d_ng[0][0] = 5
print(l_2d_ng)
# [[5, 0, 0, 0], [5, 0, 0, 0], [5, 0, 0, 0]]

l_2d_ng[0].append(100)
print(l_2d_ng)
# [[5, 0, 0, 0, 100], [5, 0, 0, 0, 100], [5, 0, 0, 0, 100]]

print(id(l_2d_ng[0]) == id(l_2d_ng[1]) == id(l_2d_ng[2]))
# True

l_2d_ok = [[0] * 4 for i in range(3)]
print(l_2d_ok)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

l_2d_ok[0][0] = 100
print(l_2d_ok)
# [[100, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print(id(l_2d_ok[0]) == id(l_2d_ok[1]) == id(l_2d_ok[2]))
# False

l_2d_ok_2 = [[0] * 4 for i in [1] * 3]
print(l_2d_ok_2)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

l_2d_ok_2[0][0] = 100
print(l_2d_ok_2)
# [[100, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print(id(l_2d_ok_2[0]) == id(l_2d_ok_2[1]) == id(l_2d_ok_2[2]))
# False

l_3d = [[[0] * 2 for i in range(3)] for j in range(4)]
print(l_3d)
# [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

l_3d[0][0][0] = 100
print(l_3d)
# [[[100, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

t = (0,) * 5
print(t)
# (0, 0, 0, 0, 0)

import array

a = array.array('i', [0] * 5)
print(a)
# array('i', [0, 0, 0, 0, 0])
