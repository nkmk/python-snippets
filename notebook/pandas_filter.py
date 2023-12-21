import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                  index=['apple', 'banana', 'pineapple'],
                  columns=['A', 'B', 'C'])
print(df)
#            A  B  C
# apple      0  1  2
# banana     3  4  5
# pineapple  6  7  8

print(df.filter(items=['A', 'C']))
#            A  C
# apple      0  2
# banana     3  5
# pineapple  6  8

# print(df.filter(items=['A', 'C'], like='A'))
# TypeError: Keyword arguments `items`, `like`, or `regex` are mutually exclusive

print(df.filter(items=['X']))
# Empty DataFrame
# Columns: []
# Index: [apple, banana, pineapple]

print(df.filter(items=['apple', 'pineapple'], axis=0))
#            A  B  C
# apple      0  1  2
# pineapple  6  7  8

print(df.filter(items=['apple', 'pineapple'], axis='index'))
#            A  B  C
# apple      0  1  2
# pineapple  6  7  8

print(df.filter(items=['A', 'C'], axis=1))
#            A  C
# apple      0  2
# banana     3  5
# pineapple  6  8

print(df.filter(items=['A', 'C'], axis='columns'))
#            A  C
# apple      0  2
# banana     3  5
# pineapple  6  8

print(df.filter(items=['A', 'C']).filter(items=['apple', 'pineapple'], axis=0))
#            A  C
# apple      0  2
# pineapple  6  8

print(df.filter(items=['A', 'C']))
#            A  C
# apple      0  2
# banana     3  5
# pineapple  6  8

print(df.filter(items=['C', 'A']))
#            C  A
# apple      2  0
# banana     5  3
# pineapple  8  6

print(df[['C', 'A']])
#            C  A
# apple      2  0
# banana     5  3
# pineapple  8  6

print(df.loc[:, ['C', 'A']])
#            C  A
# apple      2  0
# banana     5  3
# pineapple  8  6

print(df.loc[['pineapple', 'apple']])
#            A  B  C
# pineapple  6  7  8
# apple      0  1  2

print(df.filter(like='apple', axis=0))
#            A  B  C
# apple      0  1  2
# pineapple  6  7  8

print(df.filter(regex='e$', axis=0))
#            A  B  C
# apple      0  1  2
# pineapple  6  7  8

print(df.filter(regex='^(a|b)', axis=0))
#         A  B  C
# apple   0  1  2
# banana  3  4  5

print(df.filter(regex='(na|ne)', axis=0))
#            A  B  C
# banana     3  4  5
# pineapple  6  7  8

s = pd.Series([0, 1, 2], index=['apple', 'banana', 'pineapple'])
print(s)
# apple        0
# banana       1
# pineapple    2
# dtype: int64

print(s.filter(items=['pineapple', 'banana']))
# pineapple    2
# banana       1
# dtype: int64

print(s.filter(like='apple'))
# apple        0
# pineapple    2
# dtype: int64

print(s.filter(regex='^(a|b)'))
# apple     0
# banana    1
# dtype: int64
