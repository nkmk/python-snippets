import pandas as pd
import numpy as np

print(pd.__version__)
# 1.0.0

print(pd.DataFrame.agg is pd.DataFrame.aggregate)
# True

df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
print(df)
#    A  B
# 0  0  3
# 1  1  4
# 2  2  5

print(df.agg(['sum', 'mean', 'min', 'max']))
#         A     B
# sum   3.0  12.0
# mean  1.0   4.0
# min   0.0   3.0
# max   2.0   5.0

print(type(df.agg(['sum', 'mean', 'min', 'max'])))
# <class 'pandas.core.frame.DataFrame'>

print(df.agg(['sum']))
#      A   B
# sum  3  12

print(type(df.agg(['sum'])))
# <class 'pandas.core.frame.DataFrame'>

print(df.agg('sum'))
# A     3
# B    12
# dtype: int64

print(type(df.agg('sum')))
# <class 'pandas.core.series.Series'>

print(df.agg({'A': ['sum', 'min', 'max'],
              'B': ['mean', 'min', 'max']}))
#         A    B
# max   2.0  5.0
# mean  NaN  4.0
# min   0.0  3.0
# sum   3.0  NaN

print(df.agg({'A': 'sum', 'B': 'mean'}))
# A    3.0
# B    4.0
# dtype: float64

print(df.agg({'A': ['sum'], 'B': ['mean']}))
#         A    B
# mean  NaN  4.0
# sum   3.0  NaN

print(df.agg({'A': ['min', 'max'], 'B': 'mean'}))
#         A    B
# max   2.0  NaN
# mean  NaN  4.0
# min   0.0  NaN

print(df.agg(['sum', 'mean', 'min', 'max'], axis=1))
#    sum  mean  min  max
# 0  3.0   1.5  0.0  3.0
# 1  5.0   2.5  1.0  4.0
# 2  7.0   3.5  2.0  5.0

s = df['A']
print(s)
# 0    0
# 1    1
# 2    2
# Name: A, dtype: int64

print(s.agg(['sum', 'mean', 'min', 'max']))
# sum     3.0
# mean    1.0
# min     0.0
# max     2.0
# Name: A, dtype: float64

print(type(s.agg(['sum', 'mean', 'min', 'max'])))
# <class 'pandas.core.series.Series'>

print(s.agg(['sum']))
# sum    3
# Name: A, dtype: int64

print(type(s.agg(['sum'])))
# <class 'pandas.core.series.Series'>

print(s.agg('sum'))
# 3

print(type(s.agg('sum')))
# <class 'numpy.int64'>

print(s.agg({'Total': 'sum', 'Average': 'mean', 'Min': 'min', 'Max': 'max'}))
# Total      3.0
# Average    1.0
# Min        0.0
# Max        2.0
# Name: A, dtype: float64

# print(s.agg({'NewLabel_1': ['sum', 'max'], 'NewLabel_2': ['mean', 'min']}))
# SpecificationError: nested renamer is not supported

print(df.agg(['mad', 'amax', 'dtype']))
#               A         B
# mad    0.666667  0.666667
# amax          2         5
# dtype     int64     int64

print(df['A'].mad())
# 0.6666666666666666

print(np.amax(df['A']))
# 2

print(df['A'].dtype)
# int64

# print(df.agg(['xxx']))
# AttributeError: 'xxx' is not a valid function for 'Series' object

# print(df.agg('xxx'))
# AttributeError: 'xxx' is not a valid function for 'DataFrame' object

print(hasattr(pd.DataFrame, '__array__'))
# True

print(hasattr(pd.core.groupby.GroupBy, '__array__'))
# False

print(df.agg([np.sum, max]))
#      A   B
# sum  3  12
# max  2   5

print(np.sum(df['A']))
# 3

print(max(df['A']))
# 2

print(np.abs(df['A']))
# 0    0
# 1    1
# 2    2
# Name: A, dtype: int64

print(df.agg([np.abs]))
#          A        B
#   absolute absolute
# 0        0        3
# 1        1        4
# 2        2        5

# print(df.agg([np.abs, max]))
# ValueError: cannot combine transform and aggregation operations

def my_func(x):
    return min(x) / max(x)

print(df.agg([my_func, lambda x: min(x) / max(x)]))
#             A    B
# my_func   0.0  0.6
# <lambda>  0.0  0.6

print(df['A'].std())
# 1.0

print(df['A'].std(ddof=0))
# 0.816496580927726

print(df.agg(['std', lambda x: x.std(ddof=0)]))
#                  A         B
# std       1.000000  1.000000
# <lambda>  0.816497  0.816497

print(df.agg('std', ddof=0))
# A    0.816497
# B    0.816497
# dtype: float64

print(df.agg(['std'], ddof=0))
#        A    B
# std  1.0  1.0

df_str = df.assign(C=['X', 'Y', 'Z'])
print(df_str)
#    A  B  C
# 0  0  3  X
# 1  1  4  Y
# 2  2  5  Z

# df_str['C'].mean()
# TypeError: Could not convert XYZ to numeric

print(df_str.agg(['sum', 'mean']))
#         A     B    C
# sum   3.0  12.0  XYZ
# mean  1.0   4.0  NaN

print(df_str.agg(['mean', 'std']))
#         A    B
# mean  1.0  4.0
# std   1.0  1.0

print(df_str.agg(['sum', 'min', 'max']))
#      A   B    C
# sum  3  12  XYZ
# min  0   3    X
# max  2   5    Z

print(df_str.select_dtypes(include='number').agg(['sum', 'mean']))
#         A     B
# sum   3.0  12.0
# mean  1.0   4.0
