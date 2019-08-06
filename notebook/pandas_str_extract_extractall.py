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

print(s_org.str.extract('(.+)@(.+)'))
#      0          1
# A  aaa    xxx.com
# B  bbb    yyy.net
# C  ccc  zzz.co.jp

print(s_org.str.extract('(?P<local>.+)@(?P<domain>.+)'))
#   local     domain
# A   aaa    xxx.com
# B   bbb    yyy.net
# C   ccc  zzz.co.jp

print(s_org.str.extract('(a+)', expand=True))
#      0
# A  aaa
# B  NaN
# C  NaN

s_org2 = pd.Series(['aaa@xxx.com, iii@xxx.com', 'bbb@yyy.net, jjj@yyy.net', 'ccc@zzz.co.jp'],
                   index=['A', 'B', 'C'])
print(s_org2)
# A    aaa@xxx.com, iii@xxx.com
# B    bbb@yyy.net, jjj@yyy.net
# C               ccc@zzz.co.jp
# dtype: object

print(s_org2.str.extract('([a-z]+)@([a-z.]+)', expand=True))
#      0          1
# A  aaa    xxx.com
# B  bbb    yyy.net
# C  ccc  zzz.co.jp

df_all = s_org2.str.extractall('([a-z]+)@([a-z.]+)')
print(df_all)
#            0          1
#   match                
# A 0      aaa    xxx.com
#   1      iii    xxx.com
# B 0      bbb    yyy.net
#   1      jjj    yyy.net
# C 0      ccc  zzz.co.jp

print(df_all.index)
# MultiIndex(levels=[['A', 'B', 'C'], [0, 1]],
#            labels=[[0, 0, 1, 1, 2], [0, 1, 0, 1, 0]],
#            names=[None, 'match'])

print(s_org.str.extractall('([a-z]+)@([a-z.]+)'))
#            0          1
#   match                
# A 0      aaa    xxx.com
# B 0      bbb    yyy.net
# C 0      ccc  zzz.co.jp
