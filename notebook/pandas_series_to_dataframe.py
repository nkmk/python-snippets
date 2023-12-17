import pandas as pd

print(pd.__version__)
# 2.1.4

s = pd.Series([0, 1, 2], index=['A', 'B', 'C'])
print(s)
# A    0
# B    1
# C    2
# dtype: int64

print(s.to_frame())
#    0
# A  0
# B  1
# C  2

print(s.to_frame('X'))
#    X
# A  0
# B  1
# C  2

s_name = pd.Series([0, 1, 2], index=['A', 'B', 'C'], name='X')
print(s_name)
# A    0
# B    1
# C    2
# Name: X, dtype: int64

print(s_name.to_frame())
#    X
# A  0
# B  1
# C  2

print(s_name.to_frame('Y'))
#    Y
# A  0
# B  1
# C  2

print(pd.DataFrame(s))
#    0
# A  0
# B  1
# C  2

print(pd.DataFrame([s]))
#    A  B  C
# 0  0  1  2

print(pd.DataFrame(s_name))
#    X
# A  0
# B  1
# C  2

print(pd.DataFrame([s_name]))
#    A  B  C
# X  0  1  2

s1 = pd.Series([0, 1, 2], index=['A', 'B', 'C'])
s2 = pd.Series([0.0, 0.1, 0.2], index=['A', 'B', 'C'])

print(pd.DataFrame({'col1': s1, 'col2': s2}))
#    col1  col2
# A     0   0.0
# B     1   0.1
# C     2   0.2

print(pd.DataFrame([s1, s2]))
#      A    B    C
# 0  0.0  1.0  2.0
# 1  0.0  0.1  0.2

print(pd.concat([s1, s2], axis=1))
#    0    1
# A  0  0.0
# B  1  0.1
# C  2  0.2

s1_name = pd.Series([0, 1, 2], index=['A', 'B', 'C'], name='X')
s2_name = pd.Series([0.0, 0.1, 0.2], index=['A', 'B', 'C'], name='Y')

print(pd.DataFrame({s1_name.name: s1_name, s2_name.name: s2_name}))
#    X    Y
# A  0  0.0
# B  1  0.1
# C  2  0.2

print(pd.DataFrame([s1_name, s2_name]))
#      A    B    C
# X  0.0  1.0  2.0
# Y  0.0  0.1  0.2

print(pd.concat([s1_name, s2_name], axis=1))
#    X    Y
# A  0  0.0
# B  1  0.1
# C  2  0.2

s1 = pd.Series([0, 1, 2], index=['A', 'B', 'C'])
s3 = pd.Series([0.1, 0.2, 0.3], index=['B', 'C', 'D'])

print(pd.DataFrame({'col1': s1, 'col3': s3}))
#    col1  col3
# A   0.0   NaN
# B   1.0   0.1
# C   2.0   0.2
# D   NaN   0.3

print(pd.DataFrame([s1, s3]))
#      A    B    C    D
# 0  0.0  1.0  2.0  NaN
# 1  NaN  0.1  0.2  0.3

print(pd.concat([s1, s3], axis=1))
#      0    1
# A  0.0  NaN
# B  1.0  0.1
# C  2.0  0.2
# D  NaN  0.3

print(pd.concat([s1, s3], axis=1, join='inner'))
#    0    1
# B  1  0.1
# C  2  0.2

print(s3.set_axis(s1.index))
# A    0.1
# B    0.2
# C    0.3
# dtype: float64

print(pd.DataFrame({'col1': s1, 'col3': s3.set_axis(s1.index)}))
#    col1  col3
# A     0   0.1
# B     1   0.2
# C     2   0.3

print(s1.values)
# [0 1 2]

print(type(s1.values))
# <class 'numpy.ndarray'>

print(pd.DataFrame({'col1': s1.values, 'col3': s3.values}))
#    col1  col3
# 0     0   0.1
# 1     1   0.2
# 2     2   0.3

print(pd.DataFrame([s1.values, s3.values]))
#      0    1    2
# 0  0.0  1.0  2.0
# 1  0.1  0.2  0.3

# print(pd.concat([s1.values, s3.values], axis=1))
# TypeError: cannot concatenate object of type '<class 'numpy.ndarray'>'; only Series and DataFrame objs are valid

print(pd.DataFrame([s1.values, s3.values], index=['X', 'Y'], columns=['A', 'B', 'C']))
#      A    B    C
# X  0.0  1.0  2.0
# Y  0.1  0.2  0.3

s1 = pd.Series([0, 1, 2], index=['A', 'B', 'C'])
s4 = pd.Series([0.1, 0.3], index=['B', 'D'])

print(pd.DataFrame({'col1': s1, 'col4': s4}))
#    col1  col4
# A   0.0   NaN
# B   1.0   0.1
# C   2.0   NaN
# D   NaN   0.3

print(pd.DataFrame([s1, s4]))
#      A    B    C    D
# 0  0.0  1.0  2.0  NaN
# 1  NaN  0.1  NaN  0.3

print(pd.concat([s1, s4], axis=1))
#      0    1
# A  0.0  NaN
# B  1.0  0.1
# C  2.0  NaN
# D  NaN  0.3

print(pd.concat([s1, s4], axis=1, join='inner'))
#    0    1
# B  1  0.1

print(pd.DataFrame({'col1': s1, 'col4': s4.set_axis(['A', 'B'])}))
#    col1  col4
# A     0   0.1
# B     1   0.3
# C     2   NaN

# print(pd.DataFrame({'col1': s1.values, 'col4': s4.values}))
# ValueError: All arrays must be of the same length

print(pd.DataFrame([s1.values, s4.values]))
#      0    1    2
# 0  0.0  1.0  2.0
# 1  0.1  0.3  NaN

s = pd.Series([0, 1], index=['A', 'B'])
df = s.to_frame()

s['A'] = 100
print(df)
#      0
# A  100
# B    1

s = pd.Series([0, 1], index=['A', 'B'])
df_copy = s.copy().to_frame()

s['A'] = 100
print(df_copy)
#    0
# A  0
# B  1

s = pd.Series([0, 1], index=['A', 'B'])
df = pd.DataFrame(s)

s['A'] = 100
print(df)
#      0
# A  100
# B    1

s = pd.Series([0, 1], index=['A', 'B'])
df_copy = pd.DataFrame(s, copy=True)

s['A'] = 100
print(df_copy)
#    0
# A  0
# B  1

s1 = pd.Series([0, 1], index=['A', 'B'])
s2 = pd.Series([0.0, 0.1], index=['A', 'B'])
df = pd.concat([s1, s2], axis=1)

s1['A'] = 100
print(df)
#    0    1
# A  0  0.0
# B  1  0.1

s1 = pd.Series([0, 1], index=['A', 'B'])
s2 = pd.Series([0.0, 0.1], index=['A', 'B'])
df_copy_false = pd.concat([s1, s2], axis=1, copy=False)

s1['A'] = 100
print(df_copy_false)
#      0    1
# A  100  0.0
# B    1  0.1
