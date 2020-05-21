import pandas as pd

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

df = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                   'B': ['B1', 'B2', 'B3'],
                   'C': ['C1', 'C2', 'C3']},
                  index=['ONE', 'TWO', 'THREE'])

# print(df.append(0))
# TypeError: cannot concatenate object of type '<class 'int'>'; only Series and DataFrame objs are valid

print(df.append([0, 1, 2]))
#          A    B    C    0
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# 0      NaN  NaN  NaN  0.0
# 1      NaN  NaN  NaN  1.0
# 2      NaN  NaN  NaN  2.0

print(df.append({'A': 0, 'B': 1, 'C': 2}, ignore_index=True))
#     A   B   C
# 0  A1  B1  C1
# 1  A2  B2  C2
# 2  A3  B3  C3
# 3   0   1   2

s = pd.Series(['A4', 'B4', 'C4'], index=df.columns, name='FOUR')

print(df.append(s))
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4

s_mismatch = pd.Series(['B5', 'C5', 'D5'], index=['B', 'C', 'D'], name='FIVE')

print(df.append(s_mismatch))
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FIVE   NaN  B5  C5   D5

print(df)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

s_no_name = pd.Series(['B4', 'C4', 'D4'], index=['B', 'C', 'D'])

# print(df.append(s_no_name))
# TypeError: Can only append a Series if ignore_index=True or if the Series has a name

print(df.append(s_no_name, ignore_index=True))
#      A   B   C    D
# 0   A1  B1  C1  NaN
# 1   A2  B2  C2  NaN
# 2   A3  B3  C3  NaN
# 3  NaN  B4  C4   D4

print(df.append([s, s_mismatch]))
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FOUR    A4  B4  C4  NaN
# FIVE   NaN  B5  C5   D5

df2 = pd.DataFrame([['B6', 'C6', 'D6'], ['B7', 'C7', 'D7']], 
                   index=['SIX', 'SEVEN'], columns=['B', 'C', 'D'])
print(df2)
#         B   C   D
# SIX    B6  C6  D6
# SEVEN  B7  C7  D7

print(df.append(df2))
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# SIX    NaN  B6  C6   D6
# SEVEN  NaN  B7  C7   D7

# print(df.append([s, df2]))
# ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 5 and the array at index 1 has size 3

print(df.append(s).append(df2))
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FOUR    A4  B4  C4  NaN
# SIX    NaN  B6  C6   D6
# SEVEN  NaN  B7  C7   D7

print(pd.concat([df, df2]))
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# SIX    NaN  B6  C6   D6
# SEVEN  NaN  B7  C7   D7

print(pd.concat([df, df2], join='inner'))
#         B   C
# ONE    B1  C1
# TWO    B2  C2
# THREE  B3  C3
# SIX    B6  C6
# SEVEN  B7  C7

print(df.append(s))
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4

print(pd.concat([df, s]))
#          A    B    C    0
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# A      NaN  NaN  NaN   A4
# B      NaN  NaN  NaN   B4
# C      NaN  NaN  NaN   C4

print(pd.DataFrame(s).T)
#        A   B   C
# FOUR  A4  B4  C4

print(pd.concat([df, pd.DataFrame(s).T]))
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4

print(df.T.assign(FOUR=0, FIVE=['A5', 'B5', 'C5']).T)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR    0   0   0
# FIVE   A5  B5  C5

# df_insert = df.T.insert(0, 'FOUR', 0).T
# AttributeError: 'NoneType' object has no attribute 'T'

df_T = df.T
df_T.insert(0, 'FOUR', 0)
print(df_T.T)
#         A   B   C
# FOUR    0   0   0
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
