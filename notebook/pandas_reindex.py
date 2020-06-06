import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [100, 200, 300]},
                  index=['One', 'Two', 'Three'])
print(df)
#        A   B    C
# One    1  10  100
# Two    2  20  200
# Three  3  30  300

print(df.reindex(index=['Two', 'Three', 'One']))
#        A   B    C
# Two    2  20  200
# Three  3  30  300
# One    1  10  100

print(df.reindex(columns=['B', 'C', 'A']))
#         B    C  A
# One    10  100  1
# Two    20  200  2
# Three  30  300  3

print(df.reindex(index=['Two', 'Three', 'One'], columns=['B', 'C', 'A']))
#         B    C  A
# Two    20  200  2
# Three  30  300  3
# One    10  100  1

print(df.reindex(columns=['B', 'A'], index=['Three', 'One']))
#         B  A
# Three  30  3
# One    10  1

print(df.reindex(['Two', 'Three', 'One'], axis=0))
#        A   B    C
# Two    2  20  200
# Three  3  30  300
# One    1  10  100

print(df.reindex(['B', 'C', 'A'], axis='columns'))
#         B    C  A
# One    10  100  1
# Two    20  200  2
# Three  30  300  3

print(df[['B', 'C', 'A']])
#         B    C  A
# One    10  100  1
# Two    20  200  2
# Three  30  300  3

print(df.reindex(columns=['B', 'X', 'C'], index=['Two', 'One', 'Four']))
#          B   X      C
# Two   20.0 NaN  200.0
# One   10.0 NaN  100.0
# Four   NaN NaN    NaN

print(df.reindex(columns=['B', 'X', 'C'], index=['Two', 'One', 'Four'],
                 fill_value=0))
#        B  X    C
# Two   20  0  200
# One   10  0  100
# Four   0  0    0

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20], 'C': [100, 200]},
                  index=[10, 20])
print(df)
#     A   B    C
# 10  1  10  100
# 20  2  20  200

print(df.reindex(index=[5, 10, 15, 20, 25]))
#       A     B      C
# 5   NaN   NaN    NaN
# 10  1.0  10.0  100.0
# 15  NaN   NaN    NaN
# 20  2.0  20.0  200.0
# 25  NaN   NaN    NaN

print(df.reindex(index=[5, 10, 15, 20, 25], method='bfill'))
#       A     B      C
# 5   1.0  10.0  100.0
# 10  1.0  10.0  100.0
# 15  2.0  20.0  200.0
# 20  2.0  20.0  200.0
# 25  NaN   NaN    NaN

print(df.reindex(index=[5, 10, 15, 20, 25], method='ffill'))
#       A     B      C
# 5   NaN   NaN    NaN
# 10  1.0  10.0  100.0
# 15  1.0  10.0  100.0
# 20  2.0  20.0  200.0
# 25  2.0  20.0  200.0

print(df.reindex(index=[5, 10, 15, 20, 25], method='nearest'))
#     A   B    C
# 5   1  10  100
# 10  1  10  100
# 15  2  20  200
# 20  2  20  200
# 25  2  20  200

print(df.reindex(index=[10, 12, 14, 16, 18, 20]))
#       A     B      C
# 10  1.0  10.0  100.0
# 12  NaN   NaN    NaN
# 14  NaN   NaN    NaN
# 16  NaN   NaN    NaN
# 18  NaN   NaN    NaN
# 20  2.0  20.0  200.0

print(df.reindex(index=[10, 12, 14, 16, 18, 20], method='bfill', limit=2))
#       A     B      C
# 10  1.0  10.0  100.0
# 12  NaN   NaN    NaN
# 14  NaN   NaN    NaN
# 16  2.0  20.0  200.0
# 18  2.0  20.0  200.0
# 20  2.0  20.0  200.0

print(df.reindex(index=[25, 5, 15], method='bfill'))
#       A     B      C
# 25  NaN   NaN    NaN
# 5   1.0  10.0  100.0
# 15  2.0  20.0  200.0

print(df.reindex(index=[5, 15, 25], method='bfill'))
#       A     B      C
# 5   1.0  10.0  100.0
# 15  2.0  20.0  200.0
# 25  NaN   NaN    NaN

print(df.reindex(index=[5, 10, 15, 20, 25]).fillna(method='bfill'))
#       A     B      C
# 5   1.0  10.0  100.0
# 10  1.0  10.0  100.0
# 15  2.0  20.0  200.0
# 20  2.0  20.0  200.0
# 25  NaN   NaN    NaN

print(df.reindex(index=[5, 10, 15, 20, 25]).interpolate())
#       A     B      C
# 5   NaN   NaN    NaN
# 10  1.0  10.0  100.0
# 15  1.5  15.0  150.0
# 20  2.0  20.0  200.0
# 25  2.0  20.0  200.0

print(df.reindex(columns=['A', 'X', 'C'], method='bfill'))
#     A   X    C
# 10  1 NaN  100
# 20  2 NaN  200

print(df.reindex(columns=['A', 'X', 'C']).fillna(method='bfill', axis=1))
#       A      X      C
# 10  1.0  100.0  100.0
# 20  2.0  200.0  200.0

print(df.reindex(columns=['A', 'X', 'C']).interpolate(axis=1))
#       A      X      C
# 10  1.0   50.5  100.0
# 20  2.0  101.0  200.0

df = pd.DataFrame({'A': [1, 2, 3], 'B': [10, 20, 30], 'C': [100, 200, 300]},
                  index=[20, 10, 30])
print(df)
#     A   B    C
# 20  1  10  100
# 10  2  20  200
# 30  3  30  300

# print(df.reindex(index=[10, 15, 20], method='ffill'))
# ValueError: index must be monotonic increasing or decreasing

print(df.reindex(index=[10, 15, 20]))
#       A     B      C
# 10  2.0  20.0  200.0
# 15  NaN   NaN    NaN
# 20  1.0  10.0  100.0

print(df.reindex(index=[10, 15, 20]).fillna(method='bfill'))
#       A     B      C
# 10  2.0  20.0  200.0
# 15  1.0  10.0  100.0
# 20  1.0  10.0  100.0
