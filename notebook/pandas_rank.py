import pandas as pd

df = pd.DataFrame({'col1': [50, 80, 100, 80],
                   'col2': [0.3, pd.np.nan, 0.1, pd.np.nan],
                   'col3': ['h', 'j', 'i', 'k']},
                  index=['a', 'b', 'c', 'd'])

print(df)
#    col1  col2 col3
# a    50   0.3    h
# b    80   NaN    j
# c   100   0.1    i
# d    80   NaN    k

print(df.rank())
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.5   NaN   3.0
# c   4.0   1.0   2.0
# d   2.5   NaN   4.0

print(df.rank(axis=1))
#    col1  col2
# a   2.0   1.0
# b   1.0   NaN
# c   2.0   1.0
# d   1.0   NaN

print(df.rank(numeric_only=True))
#    col1  col2
# a   1.0   2.0
# b   2.5   NaN
# c   4.0   1.0
# d   2.5   NaN

# print(df.rank(axis=1, numeric_only=False))
# TypeError: '<' not supported between instances of 'str' and 'int'

print(df.rank(ascending=False))
#    col1  col2  col3
# a   4.0   1.0   4.0
# b   2.5   NaN   2.0
# c   1.0   2.0   3.0
# d   2.5   NaN   1.0

print(df.rank(method='average'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.5   NaN   3.0
# c   4.0   1.0   2.0
# d   2.5   NaN   4.0

print(df.rank(method='min'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.0   NaN   3.0
# c   4.0   1.0   2.0
# d   2.0   NaN   4.0

print(df.rank(method='max'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   3.0   NaN   3.0
# c   4.0   1.0   2.0
# d   3.0   NaN   4.0

# print(df.rank(method='first'))
# ValueError: first not supported for non-numeric data

print(df.rank(method='first', numeric_only=True))
#    col1  col2
# a   1.0   2.0
# b   2.0   NaN
# c   4.0   1.0
# d   3.0   NaN

print(df.rank(method='dense'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.0   NaN   3.0
# c   3.0   1.0   2.0
# d   2.0   NaN   4.0

print(df.rank(na_option='keep'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.5   NaN   3.0
# c   4.0   1.0   2.0
# d   2.5   NaN   4.0

print(df.rank(na_option='top'))
#    col1  col2  col3
# a   1.0   4.0   1.0
# b   2.5   1.5   3.0
# c   4.0   3.0   2.0
# d   2.5   1.5   4.0

print(df.rank(na_option='top', method='min'))
#    col1  col2  col3
# a   1.0   4.0   1.0
# b   2.0   1.0   3.0
# c   4.0   3.0   2.0
# d   2.0   1.0   4.0

print(df.rank(na_option='bottom'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.5   3.5   3.0
# c   4.0   1.0   2.0
# d   2.5   3.5   4.0

print(df.rank(na_option='bottom', method='min'))
#    col1  col2  col3
# a   1.0   2.0   1.0
# b   2.0   3.0   3.0
# c   4.0   1.0   2.0
# d   2.0   3.0   4.0

print(df.rank(pct=True))
#     col1  col2  col3
# a  0.250   1.0  0.25
# b  0.625   NaN  0.75
# c  1.000   0.5  0.50
# d  0.625   NaN  1.00

print(df.rank(pct=True, method='min', ascending=False, na_option='bottom'))
#    col1  col2  col3
# a  1.00  0.25  1.00
# b  0.50  0.75  0.50
# c  0.25  0.50  0.75
# d  0.50  0.75  0.25

print(df['col1'].rank(method='min', ascending=False))
# a    4.0
# b    2.0
# c    1.0
# d    2.0
# Name: col1, dtype: float64
