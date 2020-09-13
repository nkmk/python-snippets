import pprint

print([100] > [-100])
# True

print([1, 2, 100] > [1, 2, -100])
# True

print([1, 2, 100] > [1, 100])
# False

l_2d = [[20, 3, 100], [1, 200, 30], [300, 10, 2]]
pprint.pprint(l_2d, width=20)
# [[20, 3, 100],
#  [1, 200, 30],
#  [300, 10, 2]]

pprint.pprint(sorted(l_2d), width=20)
# [[1, 200, 30],
#  [20, 3, 100],
#  [300, 10, 2]]

pprint.pprint(l_2d, width=20)
# [[20, 3, 100],
#  [1, 200, 30],
#  [300, 10, 2]]

pprint.pprint([sorted(l) for l in l_2d], width=20)
# [[3, 20, 100],
#  [1, 30, 200],
#  [2, 10, 300]]

pprint.pprint(
    [list(x) for x in zip(*[sorted(l) for l in zip(*l_2d)])],
    width=20
)
# [[1, 3, 2],
#  [20, 10, 30],
#  [300, 200, 100]]

import numpy as np

print(np.sort(l_2d))
# [[  3  20 100]
#  [  1  30 200]
#  [  2  10 300]]

print(np.sort(l_2d, axis=0))
# [[  1   3   2]
#  [ 20  10  30]
#  [300 200 100]]

print(type(np.sort(l_2d)))
# <class 'numpy.ndarray'>

print(np.sort(l_2d).tolist())
# [[3, 20, 100], [1, 30, 200], [2, 10, 300]]

print(type(np.sort(l_2d).tolist()))
# <class 'list'>

l_2d_error = [[1, 2], [3, 4, 5]]

print(np.sort(l_2d_error))
# [list([1, 2]) list([3, 4, 5])]
# 
# /usr/local/lib/python3.8/site-packages/numpy/core/_asarray.py:136: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray
#   return array(a, dtype, copy=False, order=order, subok=True)

pprint.pprint(sorted(l_2d, key=lambda x: x[1]), width=20)
# [[20, 3, 100],
#  [300, 10, 2],
#  [1, 200, 30]]

pprint.pprint(sorted(l_2d, key=lambda x: x[2]), width=20)
# [[300, 10, 2],
#  [1, 200, 30],
#  [20, 3, 100]]

import operator

pprint.pprint(sorted(l_2d, key=operator.itemgetter(1)), width=20)
# [[20, 3, 100],
#  [300, 10, 2],
#  [1, 200, 30]]

l_2d_dup = [[20, 3, 100], [1, 200, 30], [1, 10, 2]]
pprint.pprint(l_2d_dup, width=20)
# [[20, 3, 100],
#  [1, 200, 30],
#  [1, 10, 2]]

pprint.pprint(sorted(l_2d_dup), width=20)
# [[1, 10, 2],
#  [1, 200, 30],
#  [20, 3, 100]]

pprint.pprint(sorted(l_2d_dup, key=operator.itemgetter(0)), width=20)
# [[1, 200, 30],
#  [1, 10, 2],
#  [20, 3, 100]]

pprint.pprint(sorted(l_2d_dup, key=operator.itemgetter(0, 1)), width=20)
# [[1, 10, 2],
#  [1, 200, 30],
#  [20, 3, 100]]

pprint.pprint(sorted(l_2d_dup, key=lambda x: (x[0], x[1])), width=20)
# [[1, 10, 2],
#  [1, 200, 30],
#  [20, 3, 100]]

import pandas as pd

df = pd.DataFrame(l_2d_dup, columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])
print(df)
#     A    B    C
# X  20    3  100
# Y   1  200   30
# Z   1   10    2

print(df.sort_values('A'))
#     A    B    C
# Y   1  200   30
# Z   1   10    2
# X  20    3  100

print(df.sort_values('X', axis=1))
#      B   A    C
# X    3  20  100
# Y  200   1   30
# Z   10   1    2

print(df.sort_values(['A', 'B']))
#     A    B    C
# Z   1   10    2
# Y   1  200   30
# X  20    3  100
