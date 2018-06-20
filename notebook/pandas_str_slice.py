import pandas as pd

df = pd.DataFrame({'a': ['abcde', 'fghij', 'klmno'],
                   'b': [123, 456, 789]})

print(df)
#        a    b
# 0  abcde  123
# 1  fghij  456
# 2  klmno  789

print(df.dtypes)
# a    object
# b     int64
# dtype: object

print(df['a'].str[:2])
# 0    ab
# 1    fg
# 2    kl
# Name: a, dtype: object

print(df['a'].str[-2:])
# 0    de
# 1    ij
# 2    no
# Name: a, dtype: object

print(df['a'].str[::2])
# 0    ace
# 1    fhj
# 2    kmo
# Name: a, dtype: object

print(df['a'].str[2])
# 0    c
# 1    h
# 2    m
# Name: a, dtype: object

print(df['a'].str[0])
# 0    a
# 1    f
# 2    k
# Name: a, dtype: object

print(df['a'].str[-1])
# 0    e
# 1    j
# 2    o
# Name: a, dtype: object

df['a_head'] = df['a'].str[:2]
print(df)
#        a    b a_head
# 0  abcde  123     ab
# 1  fghij  456     fg
# 2  klmno  789     kl

# print(df['b'].str[:2])
# AttributeError: Can only use .str accessor with string values, which use np.object_ dtype in pandas

print(df['b'].astype(str).str[:2])
# 0    12
# 1    45
# 2    78
# Name: b, dtype: object

print(df['b'].astype(str).str[:2].astype(int))
# 0    12
# 1    45
# 2    78
# Name: b, dtype: int64

print((df['b'] / 10).astype(int))
# 0    12
# 1    45
# 2    78
# Name: b, dtype: int64
