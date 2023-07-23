import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                   'B': ['B1', 'B2', 'B3'],
                   'C': ['C1', 'C2', 'C3']},
                  index=['ONE', 'TWO', 'THREE'])
print(df)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df.loc['ONE'] = 0
print(df)
#         A   B   C
# ONE     0   0   0
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df.loc['FOUR'] = 0
df.loc['FIVE'] = ['A5', 'B5', 'C5']
print(df)
#         A   B   C
# ONE     0   0   0
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR    0   0   0
# FIVE   A5  B5  C5

# df.loc['SIX'] = ['A6', 'B6']
# ValueError: cannot set a row with mismatched columns

s = pd.Series(['B6', 'C6', 'D6'], index=['B', 'C', 'D'], name='SIX')
print(s)
# B    B6
# C    C6
# D    D6
# Name: SIX, dtype: object

df.loc['XXX'] = df.loc['TWO'] + df.loc['THREE']
df.loc['YYY'] = s
df.loc['ZZZ'] = s.values
print(df)
#           A     B     C
# ONE       0     0     0
# TWO      A2    B2    C2
# THREE    A3    B3    C3
# FOUR      0     0     0
# FIVE     A5    B5    C5
# XXX    A2A3  B2B3  C2C3
# YYY     NaN    B6    C6
# ZZZ      B6    C6    D6

df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']},
                   index=['ONE', 'TWO', 'THREE'])
print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df2 = pd.DataFrame({'B': ['B4', 'B5'], 'C': ['C4', 'C5'], 'D': ['D4', 'D5']},
                   index=['FOUR', 'FIVE'])
print(df2)
#        B   C   D
# FOUR  B4  C4  D4
# FIVE  B5  C5  D5

print(pd.concat([df1, df2]))
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FOUR   NaN  B4  C4   D4
# FIVE   NaN  B5  C5   D5

print(pd.concat([df1, df2], join='inner'))
#         B   C
# ONE    B1  C1
# TWO    B2  C2
# THREE  B3  C3
# FOUR   B4  C4
# FIVE   B5  C5

s = pd.Series(['A4', 'B4', 'C4'], index=['A', 'B', 'C'], name='FOUR')
print(s)
# A    A4
# B    B4
# C    C4
# Name: FOUR, dtype: object

print(pd.concat([df1, s]))
#          A    B    C    0
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# A      NaN  NaN  NaN   A4
# B      NaN  NaN  NaN   B4
# C      NaN  NaN  NaN   C4

print(s.to_frame().T)
#        A   B   C
# FOUR  A4  B4  C4

print(pd.concat([df1, s.to_frame().T]))
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4
