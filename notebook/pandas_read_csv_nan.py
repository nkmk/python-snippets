import pandas as pd

print(pd.__version__)
# 2.0.3

df_nan = pd.read_csv('data/src/sample_header_index_nan.csv', index_col=0)
print(df_nan)
#          a   b
# ONE    NaN NaN
# TWO      - NaN
# THREE  NaN NaN

print(df_nan.isnull())
#            a     b
# ONE     True  True
# TWO    False  True
# THREE   True  True

df_nan_set_na = pd.read_csv('data/src/sample_header_index_nan.csv',
                            index_col=0, na_values='-')
print(df_nan_set_na)
#         a   b
# ONE   NaN NaN
# TWO   NaN NaN
# THREE NaN NaN

print(df_nan_set_na.isnull())
#           a     b
# ONE    True  True
# TWO    True  True
# THREE  True  True

df_nan_no_keep = pd.read_csv('data/src/sample_header_index_nan.csv',
                             index_col=0, na_values=['-', 'NaN', 'null'],
                             keep_default_na=False)
print(df_nan_no_keep)
#          a    b
# ONE         NaN
# TWO    NaN  nan
# THREE  NaN  N/A

print(df_nan_no_keep.isnull())
#            a      b
# ONE    False   True
# TWO     True  False
# THREE   True  False

df_nan_no_filter = pd.read_csv('data/src/sample_header_index_nan.csv',
                               index_col=0, na_filter=False)
print(df_nan_no_filter)
#           a    b
# ONE          NaN
# TWO       -  nan
# THREE  null  N/A

print(df_nan_no_filter.isnull())
#            a      b
# ONE    False  False
# TWO    False  False
# THREE  False  False
