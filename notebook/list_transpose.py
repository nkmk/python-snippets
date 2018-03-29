import numpy as np
import pandas as pd

l_2d = [[0, 1, 2], [3, 4, 5]]

arr_t = np.array(l_2d).T

print(arr_t)
print(type(arr_t))
# [[0 3]
#  [1 4]
#  [2 5]]
# <class 'numpy.ndarray'>

l_2d_t = np.array(l_2d).T.tolist()

print(l_2d_t)
print(type(l_2d_t))
# [[0, 3], [1, 4], [2, 5]]
# <class 'list'>

df_t = pd.DataFrame(l_2d).T

print(df_t)
print(type(df_t))
#    0  1
# 0  0  3
# 1  1  4
# 2  2  5
# <class 'pandas.core.frame.DataFrame'>

l_2d_t = pd.DataFrame(l_2d).T.values.tolist()

print(l_2d_t)
print(type(l_2d_t))
# [[0, 3], [1, 4], [2, 5]]
# <class 'list'>

l_2d_t_tuple = list(zip(*l_2d))

print(l_2d_t_tuple)
print(type(l_2d_t_tuple))
# [(0, 3), (1, 4), (2, 5)]
# <class 'list'>

print(l_2d_t_tuple[0])
print(type(l_2d_t_tuple[0]))
# (0, 3)
# <class 'tuple'>

l_2d_t = [list(x) for x in zip(*l_2d)]

print(l_2d_t)
print(type(l_2d_t))
# [[0, 3], [1, 4], [2, 5]]
# <class 'list'>

print(l_2d_t[0])
print(type(l_2d_t[0]))
# [0, 3]
# <class 'list'>

print(*l_2d)
# [0, 1, 2] [3, 4, 5]

print(list(zip([0, 1, 2], [3, 4, 5])))
# [(0, 3), (1, 4), (2, 5)]

print([list(x) for x in [(0, 3), (1, 4), (2, 5)]])
# [[0, 3], [1, 4], [2, 5]]
