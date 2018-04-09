import pandas as pd

s_org = pd.Series(['aaa@xxx.com', 'bbb@yyy.net', 'ccc@zzz.co.jp'], index=['A', 'B', 'C'])
print(s_org)
# A      aaa@xxx.com
# B      bbb@yyy.net
# C    ccc@zzz.co.jp
# dtype: object

df_single = s_org.str.extract('(.+)@', expand=True)
print(df_single)
print(type(df_single))
#      0
# A  aaa
# B  bbb
# C  ccc
# <class 'pandas.core.frame.DataFrame'>

s = s_org.str.extract('(.+)@', expand=False)
print(s)
print(type(s))
# A    aaa
# B    bbb
# C    ccc
# dtype: object
# <class 'pandas.core.series.Series'>

df_name = s_org.str.extract('(?P<local>.+)@', expand=True)
print(df_name)
print(type(df_name))
#   local
# A   aaa
# B   bbb
# C   ccc
# <class 'pandas.core.frame.DataFrame'>

df_multi = s_org.str.extract('(?P<local>.+)@(?P<domain>.+)', expand=True)
print(df_multi)
#   local     domain
# A   aaa    xxx.com
# B   bbb    yyy.net
# C   ccc  zzz.co.jp

df_nan = s_org.str.extract('(a+)', expand=True)
print(df_nan)
#      0
# A  aaa
# B  NaN
# C  NaN

df_single = s_org.str.extract('(\w+)', expand=True)
print(df_single)
#      0
# A  aaa
# B  bbb
# C  ccc

df_all = s_org.str.extractall('(\w+)')
print(df_all)
#            0
#   match     
# A 0      aaa
#   1      xxx
#   2      com
# B 0      bbb
#   1      yyy
#   2      net
# C 0      ccc
#   1      zzz
#   2       co
#   3       jp

print(df_all.index)
# MultiIndex(levels=[['A', 'B', 'C'], [0, 1, 2, 3]],
#            labels=[[0, 0, 0, 1, 1, 1, 2, 2, 2, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2, 3]],
#            names=[None, 'match'])
