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

print(df.assign(A=0))
#        A   B   C
# ONE    0  B1  C1
# TWO    0  B2  C2
# THREE  0  B3  C3

print(df.assign(D=0))
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
s = pd.Series(['X2', 'X3', 'X4'], index=['TWO', 'THREE', 'FOUR'], name='X')

df.insert(0, 'D', 0)
print(df)
#        D   A   B   C
# ONE    0  A1  B1  C1
# TWO    0  A2  B2  C2
# THREE  0  A3  B3  C3

df.insert(len(df.columns), 'E', s)
print(df)
#        D   A   B   C    E
# ONE    0  A1  B1  C1  NaN
# TWO    0  A2  B2  C2   X2
# THREE  0  A3  B3  C3   X3

# df.insert(10, 'F', 10)
# ValueError: cannot insert F, already exists

# df.insert(-1, 'F', 10)
# ValueError: unbounded slice

# df.insert(0, 'D', 10)
# ValueError: cannot insert D, already exists

df.insert(0, 'D', 10, allow_duplicates=True)
print(df)
#         D  D   A   B   C    E
# ONE    10  0  A1  B1  C1  NaN
# TWO    10  0  A2  B2  C2   X2
# THREE  10  0  A3  B3  C3   X3

df = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                   'B': ['B1', 'B2', 'B3'],
                   'C': ['C1', 'C2', 'C3']},
                  index=['ONE', 'TWO', 'THREE'])
s = pd.Series(['X2', 'X3', 'X4'], index=['TWO', 'THREE', 'FOUR'], name='X')

print(pd.concat([df, s], axis=1))
#          A    B    C    X
# ONE     A1   B1   C1  NaN
# TWO     A2   B2   C2   X2
# THREE   A3   B3   C3   X3
# FOUR   NaN  NaN  NaN   X4

print(pd.concat([df, s], axis=1, join='inner'))
#         A   B   C   X
# TWO    A2  B2  C2  X2
# THREE  A3  B3  C3  X3

s1 = pd.Series(['X1', 'X2', 'X3'], index=df.index, name='X')
s2 = pd.Series(['Y1', 'Y2', 'Y3'], index=df.index, name='Y')

print(pd.concat([df, s1, s2], axis=1))
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

print(pd.concat([df, df2], axis=1))
#         A   B   C  df_col1  df_col2
# ONE    A1  B1  C1        0        0
# TWO    A2  B2  C2        0        1
# THREE  A3  B3  C3        0        2
