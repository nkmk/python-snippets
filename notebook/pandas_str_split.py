import pandas as pd

s = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.com'], index=['A', 'B', 'C'])
print(s)
print(type(s))
# A    aaa@xxx.com
# B    bbb@yyy.com
# C    ccc@zzz.com
# dtype: object
# <class 'pandas.core.series.Series'>

s2 = s.str.split('@')
print(s2)
print(type(s2))
# A    [aaa, xxx.com]
# B    [bbb, yyy.com]
# C    [ccc, zzz.com]
# dtype: object
# <class 'pandas.core.series.Series'>

df = s.str.split('@', expand=True)
print(df)
print(type(df))
#      0        1
# A  aaa  xxx.com
# B  bbb  yyy.com
# C  ccc  zzz.com
# <class 'pandas.core.frame.DataFrame'>

df.columns = ['local', 'domain']
print(df)
#   local   domain
# A   aaa  xxx.com
# B   bbb  yyy.com
# C   ccc  zzz.com

print(df['domain'].str.split('.', expand=True))
#      0    1
# A  xxx  com
# B  yyy  com
# C  zzz  com

df2 = pd.concat([df, df['domain'].str.split('.', expand=True)], axis=1)
print(df2)
#   local   domain    0    1
# A   aaa  xxx.com  xxx  com
# B   bbb  yyy.com  yyy  com
# C   ccc  zzz.com  zzz  com

df2_2 = df2.drop('domain', axis=1)
print(df2_2)
#   local    0    1
# A   aaa  xxx  com
# B   bbb  yyy  com
# C   ccc  zzz  com

df3 = pd.concat([df['local'], df['domain'].str.split('.', expand=True)], axis=1)
print(df3)
#   local    0    1
# A   aaa  xxx  com
# B   bbb  yyy  com
# C   ccc  zzz  com

df3.rename(columns={0: '2nd LD', 1:'TLD'}, inplace=True)
print(df3)
#   local 2nd LD  TLD
# A   aaa    xxx  com
# B   bbb    yyy  com
# C   ccc    zzz  com
