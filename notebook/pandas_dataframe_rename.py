import pandas as pd

df = pd.DataFrame({'A': [11, 21, 31],
                   'B': [12, 22, 32],
                   'C': [13, 23, 33]},
                  index=['ONE', 'TWO', 'THREE'])

print(df)
#         A   B   C
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

df_new = df.rename(columns={'A': 'Col_1'}, index={'ONE': 'Row_1'})
print(df_new)
#        Col_1   B   C
# Row_1     11  12  13
# TWO       21  22  23
# THREE     31  32  33

print(df)
#         A   B   C
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(df.rename(columns={'A': 'Col_1', 'C': 'Col_3'}))
#        Col_1   B  Col_3
# ONE       11  12     13
# TWO       21  22     23
# THREE     31  32     33

df_copy = df.copy()
df_copy.rename(columns={'A': 'Col_1'}, index={'ONE': 'Row_1'}, inplace=True)
print(df_copy)
#        Col_1   B   C
# Row_1     11  12  13
# TWO       21  22  23
# THREE     31  32  33

print(df.rename(columns=str.lower, index=str.title))
#         a   b   c
# One    11  12  13
# Two    21  22  23
# Three  31  32  33

print(df.rename(columns=lambda s: s*3, index=lambda s: s + '!!'))
#          AAA  BBB  CCC
# ONE!!     11   12   13
# TWO!!     21   22   23
# THREE!!   31   32   33

print(df.add_prefix('X_'))
#        X_A  X_B  X_C
# ONE     11   12   13
# TWO     21   22   23
# THREE   31   32   33

print(df.add_suffix('_X'))
#        A_X  B_X  C_X
# ONE     11   12   13
# TWO     21   22   23
# THREE   31   32   33

print(df.set_axis(['Row_1', 'Row_2', 'Row_3'], axis=0))
#         A   B   C
# Row_1  11  12  13
# Row_2  21  22  23
# Row_3  31  32  33

print(df.set_axis(['Row_1', 'Row_2', 'Row_3'], axis='index'))
#         A   B   C
# Row_1  11  12  13
# Row_2  21  22  23
# Row_3  31  32  33

print(df.set_axis(['Col_1', 'Col_2', 'Col_3'], axis=1))
#        Col_1  Col_2  Col_3
# ONE       11     12     13
# TWO       21     22     23
# THREE     31     32     33

print(df.set_axis(['Col_1', 'Col_2', 'Col_3'], axis='columns'))
#        Col_1  Col_2  Col_3
# ONE       11     12     13
# TWO       21     22     23
# THREE     31     32     33

print(df.set_axis(['Row_1', 'Row_2', 'Row_3']))
#         A   B   C
# Row_1  11  12  13
# Row_2  21  22  23
# Row_3  31  32  33

# print(df.set_axis(['Row_1', 'Row_2', 'Row_3', 'Row_4']))
# ValueError: Length mismatch: Expected axis has 3 elements, new values have 4 elements

df_copy = df.copy()
df_copy.set_axis(['Row_1', 'Row_2', 'Row_3'], inplace=True)
print(df_copy)
#         A   B   C
# Row_1  11  12  13
# Row_2  21  22  23
# Row_3  31  32  33

df.index = ['Row_1', 'Row_2', 'Row_3']
df.columns = ['Col_1', 'Col_2', 'Col_3']
print(df)
#        Col_1  Col_2  Col_3
# Row_1     11     12     13
# Row_2     21     22     23
# Row_3     31     32     33

# df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']
# ValueError: Length mismatch: Expected axis has 3 elements, new values have 4 elements
