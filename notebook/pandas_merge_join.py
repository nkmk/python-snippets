import pandas as pd

print(pd.__version__)
# 2.0.3

df_ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'], 'b': ['b_1', 'b_2', 'b_3']})
df_ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'], 'c': ['c_1', 'c_2', 'c_4']})

print(df_ab)
#      a    b
# 0  a_1  b_1
# 1  a_2  b_2
# 2  a_3  b_3

print(df_ac)
#      a    c
# 0  a_1  c_1
# 1  a_2  c_2
# 2  a_4  c_4

print(pd.merge(df_ab, df_ac))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

print(df_ab.merge(df_ac))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

print(pd.merge(df_ab, df_ac, on='a'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

df_ac_ = df_ac.rename(columns={'a': 'a_'})
print(df_ac_)
#     a_    c
# 0  a_1  c_1
# 1  a_2  c_2
# 2  a_4  c_4

print(pd.merge(df_ab, df_ac_, left_on='a', right_on='a_'))
#      a    b   a_    c
# 0  a_1  b_1  a_1  c_1
# 1  a_2  b_2  a_2  c_2

print(pd.merge(df_ab, df_ac_, left_on='a', right_on='a_').drop(columns='a_'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

print(pd.merge(df_ab, df_ac, on='a', how='inner'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

print(pd.merge(df_ab, df_ac, on='a', how='left'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2
# 2  a_3  b_3  NaN

print(pd.merge(df_ab, df_ac, on='a', how='right'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2
# 2  a_4  NaN  c_4

print(pd.merge(df_ab, df_ac, on='a', how='outer'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2
# 2  a_3  b_3  NaN
# 3  a_4  NaN  c_4

print(pd.merge(df_ab, df_ac, how='cross'))
#    a_x    b  a_y    c
# 0  a_1  b_1  a_1  c_1
# 1  a_1  b_1  a_2  c_2
# 2  a_1  b_1  a_4  c_4
# 3  a_2  b_2  a_1  c_1
# 4  a_2  b_2  a_2  c_2
# 5  a_2  b_2  a_4  c_4
# 6  a_3  b_3  a_1  c_1
# 7  a_3  b_3  a_2  c_2
# 8  a_3  b_3  a_4  c_4

# print(pd.merge(df_ab, df_ac, on='a', how='cross'))
# MergeError: Can not pass on, right_on, left_on or set right_index=True or left_index=True

print(pd.merge(df_ab, df_ac, on='a', how='inner', indicator=True))
#      a    b    c _merge
# 0  a_1  b_1  c_1   both
# 1  a_2  b_2  c_2   both

print(pd.merge(df_ab, df_ac, on='a', how='outer', indicator=True))
#      a    b    c      _merge
# 0  a_1  b_1  c_1        both
# 1  a_2  b_2  c_2        both
# 2  a_3  b_3  NaN   left_only
# 3  a_4  NaN  c_4  right_only

print(pd.merge(df_ab, df_ac, on='a', how='outer', indicator='indicator'))
#      a    b    c   indicator
# 0  a_1  b_1  c_1        both
# 1  a_2  b_2  c_2        both
# 2  a_3  b_3  NaN   left_only
# 3  a_4  NaN  c_4  right_only

df_ac_b = df_ac.rename(columns={'c': 'b'})
print(df_ac_b)
#      a    b
# 0  a_1  c_1
# 1  a_2  c_2
# 2  a_4  c_4

print(pd.merge(df_ab, df_ac_b, on='a'))
#      a  b_x  b_y
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

print(pd.merge(df_ab, df_ac_b, on='a', suffixes=['_left', '_right']))
#      a b_left b_right
# 0  a_1    b_1     c_1
# 1  a_2    b_2     c_2

df_abx = df_ab.assign(x=['x_2', 'x_2', 'x_3'])
df_acx = df_ac.assign(x=['x_1', 'x_2', 'x_2'])

print(df_abx)
#      a    b    x
# 0  a_1  b_1  x_2
# 1  a_2  b_2  x_2
# 2  a_3  b_3  x_3

print(df_acx)
#      a    c    x
# 0  a_1  c_1  x_1
# 1  a_2  c_2  x_2
# 2  a_4  c_4  x_2

print(pd.merge(df_abx, df_acx))
#      a    b    x    c
# 0  a_2  b_2  x_2  c_2

print(pd.merge(df_abx, df_acx, on=['a', 'x']))
#      a    b    x    c
# 0  a_2  b_2  x_2  c_2

print(pd.merge(df_abx, df_acx, on='a'))
#      a    b  x_x    c  x_y
# 0  a_1  b_1  x_2  c_1  x_1
# 1  a_2  b_2  x_2  c_2  x_2

df_acx_ = df_acx.rename(columns={'x': 'x_'})
print(df_acx_)
#      a    c   x_
# 0  a_1  c_1  x_1
# 1  a_2  c_2  x_2
# 2  a_4  c_4  x_2

print(pd.merge(df_abx, df_acx_, left_on=['a', 'x'], right_on=['a', 'x_']))
#      a    b    x    c   x_
# 0  a_2  b_2  x_2  c_2  x_2

print(pd.merge(df_abx, df_acx, on=['a', 'x'], how='inner'))
#      a    b    x    c
# 0  a_2  b_2  x_2  c_2

print(pd.merge(df_abx, df_acx, on=['a', 'x'], how='left'))
#      a    b    x    c
# 0  a_1  b_1  x_2  NaN
# 1  a_2  b_2  x_2  c_2
# 2  a_3  b_3  x_3  NaN

print(pd.merge(df_abx, df_acx, on=['a', 'x'], how='right'))
#      a    b    x    c
# 0  a_1  NaN  x_1  c_1
# 1  a_2  b_2  x_2  c_2
# 2  a_4  NaN  x_2  c_4

print(pd.merge(df_abx, df_acx, on=['a', 'x'], how='outer'))
#      a    b    x    c
# 0  a_1  b_1  x_2  NaN
# 1  a_2  b_2  x_2  c_2
# 2  a_3  b_3  x_3  NaN
# 3  a_1  NaN  x_1  c_1
# 4  a_4  NaN  x_2  c_4

print(pd.merge(df_abx, df_acx, how='cross'))
#    a_x    b  x_x  a_y    c  x_y
# 0  a_1  b_1  x_2  a_1  c_1  x_1
# 1  a_1  b_1  x_2  a_2  c_2  x_2
# 2  a_1  b_1  x_2  a_4  c_4  x_2
# 3  a_2  b_2  x_2  a_1  c_1  x_1
# 4  a_2  b_2  x_2  a_2  c_2  x_2
# 5  a_2  b_2  x_2  a_4  c_4  x_2
# 6  a_3  b_3  x_3  a_1  c_1  x_1
# 7  a_3  b_3  x_3  a_2  c_2  x_2
# 8  a_3  b_3  x_3  a_4  c_4  x_2

df_ac_i = df_ac.set_index('a')
print(df_ac_i)
#        c
# a       
# a_1  c_1
# a_2  c_2
# a_4  c_4

print(pd.merge(df_ab, df_ac_i, left_on='a', right_index=True))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2

df_ab_i = df_ab.set_index('a')
print(df_ab_i)
#        b
# a       
# a_1  b_1
# a_2  b_2
# a_3  b_3

print(pd.merge(df_ab_i, df_ac_i, left_index=True, right_index=True))
#        b    c
# a            
# a_1  b_1  c_1
# a_2  b_2  c_2

print(df_ab_i)
#        b
# a       
# a_1  b_1
# a_2  b_2
# a_3  b_3

print(df_ac_i)
#        c
# a       
# a_1  c_1
# a_2  c_2
# a_4  c_4

print(df_ab_i.join(df_ac_i))
#        b    c
# a            
# a_1  b_1  c_1
# a_2  b_2  c_2
# a_3  b_3  NaN

print(df_ab_i.join(df_ac_i, how='inner'))
#        b    c
# a            
# a_1  b_1  c_1
# a_2  b_2  c_2

print(df_ab_i.join(df_ac_i, how='left'))
#        b    c
# a            
# a_1  b_1  c_1
# a_2  b_2  c_2
# a_3  b_3  NaN

print(df_ab_i.join(df_ac_i, how='right'))
#        b    c
# a            
# a_1  b_1  c_1
# a_2  b_2  c_2
# a_4  NaN  c_4

print(df_ab_i.join(df_ac_i, how='outer'))
#        b    c
# a            
# a_1  b_1  c_1
# a_2  b_2  c_2
# a_3  b_3  NaN
# a_4  NaN  c_4

print(df_ab_i.join(df_ac_i, how='cross'))
#      b    c
# 0  b_1  c_1
# 1  b_1  c_2
# 2  b_1  c_4
# 3  b_2  c_1
# 4  b_2  c_2
# 5  b_2  c_4
# 6  b_3  c_1
# 7  b_3  c_2
# 8  b_3  c_4

print(df_ab)
#      a    b
# 0  a_1  b_1
# 1  a_2  b_2
# 2  a_3  b_3

print(df_ab.join(df_ac_i, on='a'))
#      a    b    c
# 0  a_1  b_1  c_1
# 1  a_2  b_2  c_2
# 2  a_3  b_3  NaN

df_ab_i2 = df_ac_i.rename(columns={'c': 'b'})
print(df_ab_i2)
#        b
# a       
# a_1  c_1
# a_2  c_2
# a_4  c_4

# print(df_ab_i.join(df_ab_i2))
# ValueError: columns overlap but no suffix specified: Index(['b'], dtype='object')

print(df_ab_i.join(df_ab_i2, lsuffix='_left', rsuffix='_right'))
#     b_left b_right
# a                 
# a_1    b_1     c_1
# a_2    b_2     c_2
# a_3    b_3     NaN

df_ad_i = pd.DataFrame({'a': ['a_1', 'a_4', 'a_5'], 'd': ['d_1', 'd_4', 'd_5']}).set_index('a')
print(df_ad_i)
#        d
# a       
# a_1  d_1
# a_4  d_4
# a_5  d_5

print(df_ab_i.join([df_ac_i, df_ad_i]))
#        b    c    d
# a                 
# a_1  b_1  c_1  d_1
# a_2  b_2  c_2  NaN
# a_3  b_3  NaN  NaN

print(df_ac_i.join([df_ad_i, df_ab_i]))
#        c    d    b
# a                 
# a_1  c_1  d_1  b_1
# a_2  c_2  NaN  b_2
# a_4  c_4  d_4  NaN
