import pandas as pd

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.com', 'ddd'], index=['A', 'B', 'C', 'D'])
print(s_org)
# A    aaa@xxx.com
# B    bbb@yyy.com
# C    ccc@zzz.com
# D            ddd
# dtype: object

df = s_org.str.extract('(.+)@(.+)\.(.+)', expand=True)
print(df)
#      0    1    2
# A  aaa  xxx  com
# B  bbb  yyy  com
# C  ccc  zzz  com
# D  NaN  NaN  NaN

df = s_org.str.extract('(.+)@(.+)\.(.+)', expand=False)
print(df)
#      0    1    2
# A  aaa  xxx  com
# B  bbb  yyy  com
# C  ccc  zzz  com
# D  NaN  NaN  NaN

df_single = s_org.str.extract('(\w+)', expand=True)
print(df_single)
print(type(df_single))
#      0
# A  aaa
# B  bbb
# C  ccc
# D  ddd
# <class 'pandas.core.frame.DataFrame'>

s = s_org.str.extract('(\w+)', expand=False)
print(s)
print(type(s))
# A    aaa
# B    bbb
# C    ccc
# D    ddd
# dtype: object
# <class 'pandas.core.series.Series'>

df_name = s_org.str.extract('(?P<local>.*)@(?P<second_LD>.*)\.(?P<TLD>.*)', expand=True)
print(df_name)
#   local second_LD  TLD
# A   aaa       xxx  com
# B   bbb       yyy  com
# C   ccc       zzz  com
# D   NaN       NaN  NaN
