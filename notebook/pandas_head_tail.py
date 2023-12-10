import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.DataFrame({'col_0': list('ABCDEFGHIJ'), 'col_1': range(9, -1, -1)},
                  index=[f'row_{i}' for i in range(10)])
print(df)
#       col_0  col_1
# row_0     A      9
# row_1     B      8
# row_2     C      7
# row_3     D      6
# row_4     E      5
# row_5     F      4
# row_6     G      3
# row_7     H      2
# row_8     I      1
# row_9     J      0

print(df.head())
#       col_0  col_1
# row_0     A      9
# row_1     B      8
# row_2     C      7
# row_3     D      6
# row_4     E      5

print(df.head(3))
#       col_0  col_1
# row_0     A      9
# row_1     B      8
# row_2     C      7

print(df.tail())
#       col_0  col_1
# row_5     F      4
# row_6     G      3
# row_7     H      2
# row_8     I      1
# row_9     J      0

print(df.tail(3))
#       col_0  col_1
# row_7     H      2
# row_8     I      1
# row_9     J      0

print(df[3:6])
#       col_0  col_1
# row_3     D      6
# row_4     E      5
# row_5     F      4

print(df[:5])
#       col_0  col_1
# row_0     A      9
# row_1     B      8
# row_2     C      7
# row_3     D      6
# row_4     E      5

print(df[-5:])
#       col_0  col_1
# row_5     F      4
# row_6     G      3
# row_7     H      2
# row_8     I      1
# row_9     J      0

print(df.head(1))
#       col_0  col_1
# row_0     A      9

print(type(df.head(1)))
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[0])
# col_0    A
# col_1    9
# Name: row_0, dtype: object

print(type(df.iloc[0]))
# <class 'pandas.core.series.Series'>

print(df.iloc[0]['col_0'])
# A

print(df.iloc[-1])
# col_0    J
# col_1    0
# Name: row_9, dtype: object

print(type(df.iloc[-1]))
# <class 'pandas.core.series.Series'>

print(df.iloc[-1]['col_0'])
# J

df.iloc[0]['col_0'] = 'AAA'
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_48384/183824280.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df.iloc[0]['col_0'] = 'AAA'

df.at[df.index[0], 'col_0'] = 'AAA'
df.at[df.index[-1], 'col_0'] = 'JJJ'

print(df)
#       col_0  col_1
# row_0   AAA      9
# row_1     B      8
# row_2     C      7
# row_3     D      6
# row_4     E      5
# row_5     F      4
# row_6     G      3
# row_7     H      2
# row_8     I      1
# row_9   JJJ      0
