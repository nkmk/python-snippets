import pandas as pd
import timeit

s = pd.Series(['a', 'b', 'c', 'd', 'e'])

print(s)
# 0    a
# 1    b
# 2    c
# 3    d
# 4    e
# dtype: object

s_swap = pd.Series(s.index.values, s.values)

print(s_swap)
# a    0
# b    1
# c    2
# d    3
# e    4
# dtype: int64

print(s.values)
# ['a' 'b' 'c' 'd' 'e']

print(type(s.values))
# <class 'numpy.ndarray'>

print(s.index.values)
# [0 1 2 3 4]

print(type(s.index.values))
# <class 'numpy.ndarray'>

s_swap = pd.Series(s.index, s)

print(s_swap)
# a    0
# b    1
# c    2
# d    3
# e    4
# dtype: int64

loop = 10000

result = timeit.timeit(lambda: pd.Series(s.index.values, s.values), number=loop)
print(result / loop)
# 8.694580160081386e-05

result = timeit.timeit(lambda: pd.Series(s.index, s), number=loop)
print(result / loop)
# 0.00010916587258689105

s_large = pd.concat([s] * 100000)

print(len(s_large))
# 500000

loop = 100

result = timeit.timeit(lambda: pd.Series(s_large.index.values, s_large.values), number=loop)
print(result / loop)
# 0.005923357829451561

result = timeit.timeit(lambda: pd.Series(s_large.index, s_large), number=loop)
print(result / loop)
# 0.006492725329007953
