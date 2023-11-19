import numpy as np
import pandas as pd

print(np.__version__)
# 1.26.1

print(pd.__version__)
# 2.1.2

with open('data/src/sample_header_index.csv') as f:
    print(f.read())
# ,a,b,c,d
# ONE,11,12,13,14
# TWO,21,22,23,24
# THREE,31,32,33,34

df = pd.read_csv('data/src/sample_header_index.csv', index_col=0)
print(df)
#         a   b   c   d
# ONE    11  12  13  14
# TWO    21  22  23  24
# THREE  31  32  33  34

a = df.values
print(a)
# [[11 12 13 14]
#  [21 22 23 24]
#  [31 32 33 34]]

print(type(a))
# <class 'numpy.ndarray'>

a = np.arange(6).reshape(2, 3)
print(a)
# [[0 1 2]
#  [3 4 5]]

df = pd.DataFrame(a, index=['ONE', 'TWO'], columns=['a', 'b', 'c'])
print(df)
#      a  b  c
# ONE  0  1  2
# TWO  3  4  5

df.to_csv('data/temp/sample_pd.csv')

with open('data/temp/sample_pd.csv') as f:
    print(f.read())
# ,a,b,c
# ONE,0,1,2
# TWO,3,4,5
# 

with open('data/src/sample_nan.csv') as f:
    print(f.read())
# 11,12,,14
# 21,,,24
# 31,32,33,34

df = pd.read_csv('data/src/sample_nan.csv', header=None)
print(df)
#     0     1     2   3
# 0  11  12.0   NaN  14
# 1  21   NaN   NaN  24
# 2  31  32.0  33.0  34

with open('data/src/sample_pandas_normal.csv') as f:
    print(f.read())
# name,age,state,point
# Alice,24,NY,64
# Bob,42,CA,92
# Charlie,18,CA,70
# Dave,68,TX,70
# Ellen,24,CA,88
# Frank,30,NY,57

df = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.dtypes)
# name     object
# age       int64
# state    object
# point     int64
# dtype: object

print(df.select_dtypes('int'))
#    age  point
# 0   24     64
# 1   42     92
# 2   18     70
# 3   68     70
# 4   24     88
# 5   30     57

a = pd.read_csv('data/src/sample_pandas_normal.csv').select_dtypes('int').values
print(a)
# [[24 64]
#  [42 92]
#  [18 70]
#  [68 70]
#  [24 88]
#  [30 57]]

print(type(a))
# <class 'numpy.ndarray'>

print(a.dtype)
# int64
