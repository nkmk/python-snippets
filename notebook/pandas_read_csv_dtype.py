import pandas as pd

print(pd.__version__)
# 1.4.1

df = pd.read_csv('data/src/sample_header_index_dtype.csv', index_col=0)
print(df)
#        a    b      c  d
# ONE    1    1  100.0  x
# TWO    2   20    NaN  y
# THREE  3  300  300.0  z

print(df.dtypes)
# a      int64
# b      int64
# c    float64
# d     object
# dtype: object

print(df.applymap(type))
#                    a              b                c              d
# ONE    <class 'int'>  <class 'int'>  <class 'float'>  <class 'str'>
# TWO    <class 'int'>  <class 'int'>  <class 'float'>  <class 'str'>
# THREE  <class 'int'>  <class 'int'>  <class 'float'>  <class 'str'>

# pd.read_csv('data/src/sample_header_index_dtype.csv',
#             index_col=0, dtype=float)
# ValueError: could not convert string to float: 'ONE'

df_str = pd.read_csv('data/src/sample_header_index_dtype.csv',
                     index_col=0, dtype=str)
print(df_str)
#        a    b    c  d
# ONE    1  001  100  x
# TWO    2  020  NaN  y
# THREE  3  300  300  z

print(df_str.dtypes)
# a    object
# b    object
# c    object
# d    object
# dtype: object

print(df_str.applymap(type))
#                    a              b                c              d
# ONE    <class 'str'>  <class 'str'>    <class 'str'>  <class 'str'>
# TWO    <class 'str'>  <class 'str'>  <class 'float'>  <class 'str'>
# THREE  <class 'str'>  <class 'str'>    <class 'str'>  <class 'str'>

print(df.astype(str).applymap(type))
#                    a              b              c              d
# ONE    <class 'str'>  <class 'str'>  <class 'str'>  <class 'str'>
# TWO    <class 'str'>  <class 'str'>  <class 'str'>  <class 'str'>
# THREE  <class 'str'>  <class 'str'>  <class 'str'>  <class 'str'>

df_col = pd.read_csv('data/src/sample_header_index_dtype.csv',
                     index_col=0, dtype={'a': str, 'b': float})
print(df_col)
#        a      b      c  d
# ONE    1    1.0  100.0  x
# TWO    2   20.0    NaN  y
# THREE  3  300.0  300.0  z

print(df_col.dtypes)
# a     object
# b    float64
# c    float64
# d     object
# dtype: object

df_col = pd.read_csv('data/src/sample_header_index_dtype.csv',
                     index_col=0, dtype={1: str, 2: float})
print(df_col)
#        a      b      c  d
# ONE    1    1.0  100.0  x
# TWO    2   20.0    NaN  y
# THREE  3  300.0  300.0  z

print(df_col.dtypes)
# a     object
# b    float64
# c    float64
# d     object
# dtype: object
