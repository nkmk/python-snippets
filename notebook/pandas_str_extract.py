import pandas as pd

s = pd.Series(['a1A', 'bb22BB', 'ccc333CCC'], index=['A', 'B', 'C'])
print(s)
# A          a1A
# B       bb22BB
# C    ccc333CCC
# dtype: object

df = s.str.extract('(\D*)(.*)', expand=True)
print(df)
#      0       1
# A    a      1A
# B   bb    22BB
# C  ccc  333CCC

df_name = s.str.extract('(?P<col_1>\D*)(?P<col_2>.*)', expand=True)
print(df)
#      0       1
# A    a      1A
# B   bb    22BB
# C  ccc  333CCC

df2 = pd.concat([df_name['col_1'],
                 df_name['col_2'].str.extract('(\d*)(\D*)', expand=True)],
                axis=1)
print(df2)
#   col_1    0    1
# A     a    1    A
# B    bb   22   BB
# C   ccc  333  CCC

df2_name = pd.concat([df_name['col_1'],
                      df_name['col_2'].str.extract('(?P<col_2>\d*)(?P<col_3>\D*)', expand=True)],
                     axis=1)
print(df2_name)
#   col_1 col_2 col_3
# A     a     1     A
# B    bb    22    BB
# C   ccc   333   CCC
