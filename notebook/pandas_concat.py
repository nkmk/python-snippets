import pandas as pd

print(pd.__version__)
# 2.0.3

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
# ONE     A1   B1   C1  NaN  NaN
# TWO     A2   B2   C2   C2   D2
# THREE   A3   B3   C3   C3   D3
# FOUR   NaN  NaN  NaN   C4   D4

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
# ONE     A1   B1   C1  NaN  NaN
# TWO     A2   B2   C2   C2   D2
# THREE   A3   B3   C3   C3   D3
# FOUR   NaN  NaN  NaN   C4   D4

df_h_in = pd.concat([df1, df2], axis=1, join='inner')
print(df_h_in)
#         A   B   C   C   D
# TWO    A2  B2  C2  C2  D2
# THREE  A3  B3  C3  C3  D3

df_h = pd.concat([df1, df2.rename(index={'FOUR': 'ONE'})], axis=1)
print(df_h)
#         A   B   C   C   D
# ONE    A1  B1  C1  C4  D4
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
# ONE     X1  NaN
# TWO     X2   Y2
# THREE   X3   Y3
# FOUR   NaN   Y4

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
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2   Y2
# THREE   A3   B3   C3   Y3
# FOUR   NaN  NaN  NaN   Y4

df_s_h_in = pd.concat([df1, s2], axis=1, join='inner')
print(df_s_h_in)
#         A   B   C   Y
# TWO    A2  B2  C2  Y2
# THREE  A3  B3  C3  Y3

df_s_v = pd.concat([df1, s1])
print(df_s_v)
#          A    B    C    0
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2  NaN
# THREE   A3   B3   C3  NaN
# ONE    NaN  NaN  NaN   X1
# TWO    NaN  NaN  NaN   X2
# THREE  NaN  NaN  NaN   X3

print(s1.set_axis(df1.columns).to_frame().T)
#     A   B   C
# X  X1  X2  X3

df_s_v = pd.concat([df1, s1.set_axis(df1.columns).to_frame().T])
print(df_s_v)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# X      X1  X2  X3

print(s2.values)
# ['Y2' 'Y3' 'Y4']

df1.loc[s2.name] = s2.values
print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3
# Y      Y2  Y3  Y4
