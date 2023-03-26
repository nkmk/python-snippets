import pandas as pd

print(pd.__version__)
# 1.5.3

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.com', 'ccc'], index=['A', 'B', 'C'])
print(s_org)
# A    aaa@xxx.com
# B    bbb@yyy.com
# C            ccc
# dtype: object

df = s_org.str.extract(r'(.+)@(.+)\.(.+)')
print(df)
#      0    1    2
# A  aaa  xxx  com
# B  bbb  yyy  com
# C  NaN  NaN  NaN

df = s_org.str.extract(r'(\w+)', expand=True)
print(df)
#      0
# A  aaa
# B  bbb
# C  ccc

print(type(df))
# <class 'pandas.core.frame.DataFrame'>

s = s_org.str.extract(r'(\w+)', expand=False)
print(s)
# A    aaa
# B    bbb
# C    ccc
# dtype: object

print(type(s))
# <class 'pandas.core.series.Series'>

df_name = s_org.str.extract(
    r'(?P<local>.*)@(?P<second_LD>.*)\.(?P<TLD>.*)', expand=True
)
print(df_name)
#   local second_LD  TLD
# A   aaa       xxx  com
# B   bbb       yyy  com
# C   NaN       NaN  NaN
