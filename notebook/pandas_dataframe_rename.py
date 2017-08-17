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

print(df)
#         A   B   C
# ONE    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(df_new)
#         a   B   C
# one    11  12  13
# TWO    21  22  23
# THREE  31  32  33

df_new = df.rename(columns={'A': 'a'}, index={'ONE': 'one'}, inplace=True)

print(df)
#         a   B   C
# one    11  12  13
# TWO    21  22  23
# THREE  31  32  33

print(df_new)
# None

df_new = df.rename(columns=lambda s: s.upper(), index=lambda s: s.lower())

print(df_new)
#         A   B   C
# one    11  12  13
# two    21  22  23
# three  31  32  33

df_new = df_new.rename(columns=lambda s: s*3, index=lambda s: s + '!!')

print(df_new)
#          AAA  BBB  CCC
# one!!     11   12   13
# two!!     21   22   23
# three!!   31   32   33

df.index = [1, 2, 3]
df.columns = ['a', 'b', 'c']

print(df)
#     a   b   c
# 1  11  12  13
# 2  21  22  23
# 3  31  32  33
