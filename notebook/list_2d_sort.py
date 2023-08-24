import pprint

l_2d = [[20, 3, 100], [1, 200, 30], [300, 10, 2]]
pprint.pprint(l_2d, width=20)
# [[20, 3, 100],
#  [1, 200, 30],
#  [300, 10, 2]]

pprint.pprint(sorted(l_2d), width=20)
# [[1, 200, 30],
#  [20, 3, 100],
#  [300, 10, 2]]

pprint.pprint([sorted(l) for l in l_2d], width=20)
# [[3, 20, 100],
#  [1, 30, 200],
#  [2, 10, 300]]

pprint.pprint([list(x) for x in zip(*[sorted(l) for l in zip(*l_2d)])], width=20)
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

# print(np.sort(l_2d_error))
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (2,) + inhomogeneous part.

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

pprint.pprint(sorted(l_2d, key=operator.itemgetter(2)), width=20)
# [[300, 10, 2],
#  [1, 200, 30],
#  [20, 3, 100]]

l_2d_dup = [[1, 3, 100], [1, 200, 30], [1, 3, 2]]
pprint.pprint(l_2d_dup, width=20)
# [[1, 3, 100],
#  [1, 200, 30],
#  [1, 3, 2]]

pprint.pprint(sorted(l_2d_dup), width=20)
# [[1, 3, 2],
#  [1, 3, 100],
#  [1, 200, 30]]

pprint.pprint(sorted(l_2d_dup, key=operator.itemgetter(0, 2)), width=20)
# [[1, 3, 2],
#  [1, 200, 30],
#  [1, 3, 100]]

pprint.pprint(sorted(l_2d_dup, key=lambda x: (x[0], x[2])), width=20)
# [[1, 3, 2],
#  [1, 200, 30],
#  [1, 3, 100]]

import pandas as pd

df = pd.DataFrame(l_2d_dup, columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])
print(df)
#    A    B    C
# X  1    3  100
# Y  1  200   30
# Z  1    3    2

print(df.sort_values('C'))
#    A    B    C
# Z  1    3    2
# Y  1  200   30
# X  1    3  100

print(df.sort_values('Z', axis=1))
#    A    C    B
# X  1  100    3
# Y  1   30  200
# Z  1    2    3

print(df.sort_values(['A', 'C']))
#    A    B    C
# Z  1    3    2
# Y  1  200   30
# X  1    3  100

df = pd.DataFrame(l_2d_dup)
print(df)
#    0    1    2
# 0  1    3  100
# 1  1  200   30
# 2  1    3    2

print(df.sort_values(2))
#    0    1    2
# 2  1    3    2
# 1  1  200   30
# 0  1    3  100

print(df.sort_values(2, axis=1))
#    0    2    1
# 0  1  100    3
# 1  1   30  200
# 2  1    2    3

print(df.sort_values([0, 2]))
#    0    1    2
# 2  1    3    2
# 1  1  200   30
# 0  1    3  100

print(df.sort_values([0, 2]).values.tolist())
# [[1, 3, 2], [1, 200, 30], [1, 3, 100]]

print(type(df.sort_values([0, 2]).values.tolist()))
# <class 'list'>
