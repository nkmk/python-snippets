import pandas as pd

print(pd.__version__)
# 1.5.3

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc'], index=['A', 'B', 'C'])
print(s_org)
# A    aaa@xxx.com
# B    bbb@yyy.com
# C            ccc
# dtype: object

print(type(s_org))
# <class 'pandas.core.series.Series'>

s = s_org.str.split('@')
print(s)
# A    [aaa, xxx.com]
# B    [bbb, yyy.com]
# C             [ccc]
# dtype: object

print(type(s))
# <class 'pandas.core.series.Series'>

print(s_org.str.split(r'@.+\.'))
# A    [aaa, com]
# B    [bbb, com]
# C         [ccc]
# dtype: object

import re

pat = re.compile(r'@.+\.')
print(s_org.str.split(pat))
# A    [aaa, com]
# B    [bbb, com]
# C         [ccc]
# dtype: object

df = s_org.str.split('@', expand=True)
print(df)
#      0        1
# A  aaa  xxx.com
# B  bbb  yyy.com
# C  ccc     None

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

df.columns = ['local', 'domain']
print(df)
#   local   domain
# A   aaa  xxx.com
# B   bbb  yyy.com
# C   ccc     None

s_org = pd.Series(['a-b-c-d', 'x-y-z', '1'], index=['A', 'B', 'C'])
print(s_org)
# A    a-b-c-d
# B      x-y-z
# C          1
# dtype: object

print(s_org.str.split('-'))
# A    [a, b, c, d]
# B       [x, y, z]
# C             [1]
# dtype: object

print(s_org.str.split('-', n=1))
# A    [a, b-c-d]
# B      [x, y-z]
# C           [1]
# dtype: object

print(df)
#   local   domain
# A   aaa  xxx.com
# B   bbb  yyy.com
# C   ccc     None

print(df['domain'].str.split('.', expand=True))
#       0     1
# A   xxx   com
# B   yyy   com
# C  None  None

df2 = pd.concat([df, df['domain'].str.split('.', expand=True)], axis=1).drop(
    'domain', axis=1
)
print(df2)
#   local     0     1
# A   aaa   xxx   com
# B   bbb   yyy   com
# C   ccc  None  None

df3 = pd.concat([df['local'], df['domain'].str.split('.', expand=True)], axis=1)
print(df3)
#   local     0     1
# A   aaa   xxx   com
# B   bbb   yyy   com
# C   ccc  None  None

df3.rename(columns={0: 'second_LD', 1: 'TLD'}, inplace=True)
print(df3)
#   local second_LD   TLD
# A   aaa       xxx   com
# B   bbb       yyy   com
# C   ccc      None  None
