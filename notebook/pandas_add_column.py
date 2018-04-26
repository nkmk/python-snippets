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

df['A'] = 0
print(df)
#        A   B   C
# ONE    0  B1  C1
# TWO    0  B2  C2
# THREE  0  B3  C3

df['D'] = 0
print(df)
#        A   B   C  D
# ONE    0  B1  C1  0
# TWO    0  B2  C2  0
# THREE  0  B3  C3  0

df['E'] = [0, 1, 2]
print(df)
#        A   B   C  D  E
# ONE    0  B1  C1  0  0
# TWO    0  B2  C2  0  1
# THREE  0  B3  C3  0  2

# df['F'] = [0, 1, 2, 3]
# ValueError: Length of values does not match length of index

df['F'] = df['B'] + df['C']
print(df)
#        A   B   C  D  E     F
# ONE    0  B1  C1  0  0  B1C1
# TWO    0  B2  C2  0  1  B2C2
# THREE  0  B3  C3  0  2  B3C3

df['G'] = df['B'].str.lower()
print(df)
#        A   B   C  D  E     F   G
# ONE    0  B1  C1  0  0  B1C1  b1
# TWO    0  B2  C2  0  1  B2C2  b2
# THREE  0  B3  C3  0  2  B3C3  b3

s = pd.Series(['X2', 'X3', 'X4'], index=['TWO', 'THREE', 'FOUR'], name='X')
print(s)
# TWO      X2
# THREE    X3
# FOUR     X4
# Name: X, dtype: object

df['H'] = s
print(df)
#        A   B   C  D  E     F   G    H
# ONE    0  B1  C1  0  0  B1C1  b1  NaN
# TWO    0  B2  C2  0  1  B2C2  b2   X2
# THREE  0  B3  C3  0  2  B3C3  b3   X3

print(s.values)
# ['X2' 'X3' 'X4']

df['I'] = s.values
print(df)
#        A   B   C  D  E     F   G    H   I
# ONE    0  B1  C1  0  0  B1C1  b1  NaN  X2
# TWO    0  B2  C2  0  1  B2C2  b2   X2  X3
# THREE  0  B3  C3  0  2  B3C3  b3   X3  X4

df = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                   'B': ['B1', 'B2', 'B3'],
                   'C': ['C1', 'C2', 'C3']},
                  index=['ONE', 'TWO', 'THREE'])
print(df)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df_new = df.assign(A=0)
print(df_new)
#        A   B   C
# ONE    0  B1  C1
# TWO    0  B2  C2
# THREE  0  B3  C3

df_new = df.assign(D=0)
print(df_new)
#         A   B   C  D
# ONE    A1  B1  C1  0
# TWO    A2  B2  C2  0
# THREE  A3  B3  C3  0

print(df)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

s = pd.Series(['X2', 'X3', 'X4'], index=['TWO', 'THREE', 'FOUR'], name='X')
print(s)
# TWO      X2
# THREE    X3
# FOUR     X4
# Name: X, dtype: object

df_new = df.assign(C='XXX',
                   D=0, E=[0, 1, 2],
                   F=s, G=s.values,
                   H=df['A'] + df['B'])
print(df_new)
#         A   B    C  D  E    F   G     H
# ONE    A1  B1  XXX  0  0  NaN  X2  A1B1
# TWO    A2  B2  XXX  0  1   X2  X3  A2B2
# THREE  A3  B3  XXX  0  2   X3  X4  A3B3

df = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                   'B': ['B1', 'B2', 'B3'],
                   'C': ['C1', 'C2', 'C3']},
                  index=['ONE', 'TWO', 'THREE'])
print(df)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

s = pd.Series(['X2', 'X3', 'X4'], index=['TWO', 'THREE', 'FOUR'], name='X')
print(s)
# TWO      X2
# THREE    X3
# FOUR     X4
# Name: X, dtype: object

df_concat = pd.concat([df, s], axis=1)
print(df_concat)
#          A    B    C    X
# FOUR   NaN  NaN  NaN   X4
# ONE     A1   B1   C1  NaN
# THREE   A3   B3   C3   X3
# TWO     A2   B2   C2   X2

df_concat_in = pd.concat([df, s], axis=1, join='inner')
print(df_concat_in)
#         A   B   C   X
# TWO    A2  B2  C2  X2
# THREE  A3  B3  C3  X3

s1 = pd.Series(['X1', 'X2', 'X3'], index=df.index, name='X')
s2 = pd.Series(['Y1', 'Y2', 'Y3'], index=df.index, name='Y')

df_concat = pd.concat([df, s1, s2], axis=1)
print(df_concat)
#         A   B   C   X   Y
# ONE    A1  B1  C1  X1  Y1
# TWO    A2  B2  C2  X2  Y2
# THREE  A3  B3  C3  X3  Y3

df2 = pd.DataFrame({'df_col1': 0, 'df_col2': range(3)}, index=df.index)
print(df2)
#        df_col1  df_col2
# ONE          0        0
# TWO          0        1
# THREE        0        2

df_concat2 = pd.concat([df, df2], axis=1)
print(df_concat2)
#         A   B   C  df_col1  df_col2
# ONE    A1  B1  C1        0        0
# TWO    A2  B2  C2        0        1
# THREE  A3  B3  C3        0        2
