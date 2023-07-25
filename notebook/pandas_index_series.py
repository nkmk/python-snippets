import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.DataFrame({'col_0': ['00', '10', '20', '30', '40'],
                   'col_1': ['01', '11', '21', '31', '41'],
                   'col_2': ['02', '12', '22', '32', '42'],
                   'col_3': ['03', '13', '23', '33', '43']},
                  index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4'])
print(df)
#       col_0 col_1 col_2 col_3
# row_0    00    01    02    03
# row_1    10    11    12    13
# row_2    20    21    22    23
# row_3    30    31    32    33
# row_4    40    41    42    43

s = df['col_0']
print(s)
# row_0    00
# row_1    10
# row_2    20
# row_3    30
# row_4    40
# Name: col_0, dtype: object

print(s[3])
print(type(s[3]))
# 30
# <class 'str'>

print(s[-1])
# 40

print(s['row_0'])
# 00

print(s.row_0)
# 00

print(s[[3, 1]])
print(type(s[[3, 1]]))
# row_3    30
# row_1    10
# Name: col_0, dtype: object
# <class 'pandas.core.series.Series'>

print(s[[1]])
print(type(s[[1]]))
# row_1    10
# Name: col_0, dtype: object
# <class 'pandas.core.series.Series'>

print(s[['row_3', 'row_1']])
# row_3    30
# row_1    10
# Name: col_0, dtype: object

print(s[['row_1']])
# row_1    10
# Name: col_0, dtype: object

print(s[1:3])
print(type(s[1:3]))
# row_1    10
# row_2    20
# Name: col_0, dtype: object
# <class 'pandas.core.series.Series'>

print(s[1:2])
print(type(s[1:2]))
# row_1    10
# Name: col_0, dtype: object
# <class 'pandas.core.series.Series'>

print(s['row_1':'row_3'])
# row_1    10
# row_2    20
# row_3    30
# Name: col_0, dtype: object

print(s['row_1':'row_1'])
# row_1    10
# Name: col_0, dtype: object
