import pandas as pd

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

df_object = pd.read_csv('data/src/sample_header_index_dtype.csv',
                        index_col=0, dtype=object)
print(df_object)
#        a    b    c  d
# ONE    1  001  100  x
# TWO    2  020  NaN  y
# THREE  3  300  300  z

print(df_object.dtypes)
# a    object
# b    object
# c    object
# d    object
# dtype: object

print(df_object.applymap(type))
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
                     index_col=0, dtype={'a': float, 'b': str})
print(df_col)
#          a    b      c  d
# ONE    1.0  001  100.0  x
# TWO    2.0  020    NaN  y
# THREE  3.0  300  300.0  z

print(df_col.dtypes)
# a    float64
# b     object
# c    float64
# d     object
# dtype: object

df_col = pd.read_csv('data/src/sample_header_index_dtype.csv',
                     index_col=0, dtype={1: float, 2: str})
print(df_col)
#          a    b      c  d
# ONE    1.0  001  100.0  x
# TWO    2.0  020    NaN  y
# THREE  3.0  300  300.0  z

print(df_col.dtypes)
# a    float64
# b     object
# c    float64
# d     object
# dtype: object
