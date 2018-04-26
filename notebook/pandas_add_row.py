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
print(df)
#         A   B   C
# ONE     0   0   0
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR    0   0   0

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

df.loc['XXX'] = df.loc['TWO'] + df.loc['THREE']
print(df)
#           A     B     C
# ONE       0     0     0
# TWO      A2    B2    C2
# THREE    A3    B3    C3
# FOUR      0     0     0
# FIVE     A5    B5    C5
# XXX    A2A3  B2B3  C2C3

s = pd.Series(['B6', 'C6', 'D6'], index=['B', 'C', 'D'], name='SIX')
print(s)
# B    B6
# C    C6
# D    D6
# Name: SIX, dtype: object

df.loc['YYY'] = s
print(df)
#           A     B     C
# ONE       0     0     0
# TWO      A2    B2    C2
# THREE    A3    B3    C3
# FOUR      0     0     0
# FIVE     A5    B5    C5
# XXX    A2A3  B2B3  C2C3
# YYY     NaN    B6    C6

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
print(df)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

s = pd.Series(['A4', 'B4', 'C4'], index=df.columns, name='FOUR')
print(s)
# A    A4
# B    B4
# C    C4
# Name: FOUR, dtype: object

df_append = df.append(s)
print(df_append)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4

s_mismatch = pd.Series(['B5', 'C5', 'D5'], index=['B', 'C', 'D'], name='FIVE')
print(s_mismatch)
# B    B5
# C    C5
# D    D5
# Name: FIVE, dtype: object

df_append_mismatch = df.append(s_mismatch)
print(df_append_mismatch)
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

# df_append_no_name = df.append(s_no_name)
# TypeError: Can only append a Series if ignore_index=True or if the Series has a name

df_append_multi = df.append([s, s_mismatch])
print(df_append_multi)
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FOUR    A4  B4  C4  NaN
# FIVE   NaN  B5  C5   D5

df2 = pd.DataFrame([['B4', 'C4', 'D4'], ['B5', 'C5', 'D5']], 
                   index=['FOUR', 'FIVE'], columns=['B', 'C', 'D'])
print(df2)
#        B   C   D
# FOUR  B4  C4  D4
# FIVE  B5  C5  D5

df_append = df.append(df2)
print(df_append)
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FOUR   NaN  B4  C4   D4
# FIVE   NaN  B5  C5   D5

df_concat = pd.concat([df, df2])
print(df_concat)
#          A   B   C    D
# ONE     A1  B1  C1  NaN
# TWO     A2  B2  C2  NaN
# THREE   A3  B3  C3  NaN
# FOUR   NaN  B4  C4   D4
# FIVE   NaN  B5  C5   D5

df_concat_in = pd.concat([df, df2], join='inner')
print(df_concat_in)
#         B   C
# ONE    B1  C1
# TWO    B2  C2
# THREE  B3  C3
# FOUR   B4  C4
# FIVE   B5  C5

s = pd.Series(['AX', 'BX', 'CX'], index=df.columns, name='X')
print(s)
# A    AX
# B    BX
# C    CX
# Name: X, dtype: object

df_append_s = df.append(s)
print(df_append_s)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# X      AX  BX  CX

df_concat_s = pd.concat([df, s])
print(df_concat_s)
#          A    B    C    0
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# A      NaN  NaN  NaN   AX
# B      NaN  NaN  NaN   BX
# C      NaN  NaN  NaN   CX

st = pd.DataFrame(s).T
print(type(st))
print(st)
# <class 'pandas.core.frame.DataFrame'>
#     A   B   C
# X  AX  BX  CX

df_concat_st = pd.concat([df, pd.DataFrame(s).T])
print(df_concat_st)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# X      AX  BX  CX

df_assign = df.T.assign(FOUR=0, FIVE=['A5', 'B5', 'C5']).T
print(df_assign)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR    0   0   0
# FIVE   A5  B5  C5
