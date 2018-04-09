import pandas as pd

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.com', 'ddd'], index=['A', 'B', 'C', 'D'])
print(s_org)
print(type(s_org))
# A    aaa@xxx.com
# B    bbb@yyy.com
# C    ccc@zzz.com
# D            ddd
# dtype: object
# <class 'pandas.core.series.Series'>

s = s_org.str.split('@')
print(s)
print(type(s))
# A    [aaa, xxx.com]
# B    [bbb, yyy.com]
# C    [ccc, zzz.com]
# D             [ddd]
# dtype: object
# <class 'pandas.core.series.Series'>

df = s_org.str.split('@', expand=True)
print(df)
print(type(df))
#      0        1
# A  aaa  xxx.com
# B  bbb  yyy.com
# C  ccc  zzz.com
# D  ddd     None
# <class 'pandas.core.frame.DataFrame'>

df.columns = ['local', 'domain']
print(df)
#   local   domain
# A   aaa  xxx.com
# B   bbb  yyy.com
# C   ccc  zzz.com
# D   ddd     None

print(df['domain'].str.split('.', expand=True))
#       0     1
# A   xxx   com
# B   yyy   com
# C   zzz   com
# D  None  None

df2 = pd.concat([df, df['domain'].str.split('.', expand=True)], axis=1).drop('domain', axis=1)
print(df2)
#   local     0     1
# A   aaa   xxx   com
# B   bbb   yyy   com
# C   ccc   zzz   com
# D   ddd  None  None

df3 = pd.concat([df['local'], df['domain'].str.split('.', expand=True)], axis=1)
print(df3)
#   local     0     1
# A   aaa   xxx   com
# B   bbb   yyy   com
# C   ccc   zzz   com
# D   ddd  None  None

df3.rename(columns={0: 'second_LD', 1: 'TLD'}, inplace=True)
print(df3)
#   local second_LD   TLD
# A   aaa       xxx   com
# B   bbb       yyy   com
# C   ccc       zzz   com
# D   ddd      None  None
