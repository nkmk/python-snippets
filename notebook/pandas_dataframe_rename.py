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

df_new = df.rename(columns={'A': 'a'}, index={'ONE': 'one'})
print(df_new)
#         a   B   C
# one    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(df)
#         A   B   C
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(df.rename(columns={'A': 'a', 'C': 'c'}))
#         a   B   c
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

df_org = df.copy()
df_org.rename(columns={'A': 'a'}, index={'ONE': 'one'}, inplace=True)
print(df_org)
#         a   B   C
# one    11  12  13
# TWO    21  22  23
# THREE  31  32  33

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

df.index = [1, 2, 3]
df.columns = ['a', 'b', 'c']

print(df)
#     a   b   c
# 1  11  12  13
# 2  21  22  23
# 3  31  32  33

# df.index = [1, 2, 3, 4]
# ValueError: Length mismatch: Expected axis has 3 elements, new values have 4 elements
