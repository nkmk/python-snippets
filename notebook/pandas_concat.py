import pandas as pd

df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']},
                   index=['ONE', 'TWO', 'THREE'])
print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df2 = pd.DataFrame({'C': ['C2', 'C3', 'C4'],
                    'D': ['D2', 'D3', 'D4']},
                   index=['TWO', 'THREE', 'FOUR'])
print(df2)
#         C   D
# TWO    C2  D2
# THREE  C3  D3
# FOUR   C4  D4

s1 = pd.Series(['X1', 'X2', 'X3'], index=['ONE', 'TWO', 'THREE'], name='X')
print(s1)
# ONE      X1
# TWO      X2
# THREE    X3
# Name: X, dtype: object

s2 = pd.Series(['Y2', 'Y3', 'Y4'], index=['TWO', 'THREE', 'FOUR'], name='Y')
print(s2)
# TWO      Y2
# THREE    Y3
# FOUR     Y4
# Name: Y, dtype: object

df_concat = pd.concat([df1, df2])
print(df_concat)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4

df_concat_multi = pd.concat([df1, df2, df1])
print(df_concat_multi)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN

df_v = pd.concat([df1, df2], axis=0)
print(df_v)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4

df_h = pd.concat([df1, df2], axis=1)
print(df_h)
#          A    B    C    C    D
# FOUR   NaN  NaN  NaN   C4   D4
# ONE     A1   B1   C1  NaN  NaN
# THREE   A3   B3   C3   C3   D3
# TWO     A2   B2   C2   C2   D2

df_v_out = pd.concat([df1, df2], join='outer')
print(df_v_out)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4

df_v_in = pd.concat([df1, df2], join='inner')
print(df_v_in)
#         C
# ONE    C1
# TWO    C2
# THREE  C3
# TWO    C2
# THREE  C3
# FOUR   C4

df_h_out = pd.concat([df1, df2], axis=1, join='outer')
print(df_h_out)
#          A    B    C    C    D
# FOUR   NaN  NaN  NaN   C4   D4
# ONE     A1   B1   C1  NaN  NaN
# THREE   A3   B3   C3   C3   D3
# TWO     A2   B2   C2   C2   D2

df_h_in = pd.concat([df1, df2], axis=1, join='inner')
print(df_h_in)
#         A   B   C   C   D
# TWO    A2  B2  C2  C2  D2
# THREE  A3  B3  C3  C3  D3

df_concat = pd.concat([df1, df2])
print(df_concat)
#          A    B   C    D
# ONE     A1   B1  C1  NaN
# TWO     A2   B2  C2  NaN
# THREE   A3   B3  C3  NaN
# TWO    NaN  NaN  C2   D2
# THREE  NaN  NaN  C3   D3
# FOUR   NaN  NaN  C4   D4

print(type(df_concat))
# <class 'pandas.core.frame.DataFrame'>

s_v = pd.concat([s1, s2])
print(s_v)
# ONE      X1
# TWO      X2
# THREE    X3
# TWO      Y2
# THREE    Y3
# FOUR     Y4
# dtype: object

print(type(s_v))
# <class 'pandas.core.series.Series'>

s_h = pd.concat([s1, s2], axis=1)
print(s_h)
#          X    Y
# FOUR   NaN   Y4
# ONE     X1  NaN
# THREE   X3   Y3
# TWO     X2   Y2

print(type(s_h))
# <class 'pandas.core.frame.DataFrame'>

s_h_in = pd.concat([s1, s2], axis=1, join='inner')
print(s_h_in)
#         X   Y
# TWO    X2  Y2
# THREE  X3  Y3

df_s_h = pd.concat([df1, s2], axis=1)
print(df_s_h)
#          A    B    C    Y
# FOUR   NaN  NaN  NaN   Y4
# ONE     A1   B1   C1  NaN
# THREE   A3   B3   C3   Y3
# TWO     A2   B2   C2   Y2

df_s_h_in = pd.concat([df1, s2], axis=1, join='inner')
print(df_s_h_in)
#         A   B   C   Y
# TWO    A2  B2  C2  Y2
# THREE  A3  B3  C3  Y3

df_s_v = pd.concat([df1, s2])
print(df_s_v)
#          A    B    C    0
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# TWO    NaN  NaN  NaN   Y2
# THREE  NaN  NaN  NaN   Y3
# FOUR   NaN  NaN  NaN   Y4

df1.loc['FOUR'] = ['A4', 'B4', 'C4']
print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4

s = pd.Series(['A5', 'B5', 'C5'], index=df1.columns, name='FIVE')
print(s)
# A    A5
# B    B5
# C    C5
# Name: FIVE, dtype: object

df_append = df1.append(s)
print(df_append)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# FOUR   A4  B4  C4
# FIVE   A5  B5  C5
