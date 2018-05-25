import pandas as pd

df = pd.DataFrame({'A': ['a', 'a', 'a', 'b', 'b', 'b'],
                   'B': ['x', 'y', 'z', 'x', 'y', 'z'],
                   'C': [1, 2, 3, 4, 5, 6],
                   'D': [10, 20, 30, 40, 50, 60]})

print(df)
#    A  B  C   D
# 0  a  x  1  10
# 1  a  y  2  20
# 2  a  z  3  30
# 3  b  x  4  40
# 4  b  y  5  50
# 5  b  z  6  60

s = df.stack()
print(s)
# 0  A     a
#    B     x
#    C     1
#    D    10
# 1  A     a
#    B     y
#    C     2
#    D    20
# 2  A     a
#    B     z
#    C     3
#    D    30
# 3  A     b
#    B     x
#    C     4
#    D    40
# 4  A     b
#    B     y
#    C     5
#    D    50
# 5  A     b
#    B     z
#    C     6
#    D    60
# dtype: object

print(type(s))
# <class 'pandas.core.series.Series'>

print(s.index)
# MultiIndex(levels=[[0, 1, 2, 3, 4, 5], ['A', 'B', 'C', 'D']],
#            labels=[[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]])

print(s.unstack())
#    A  B  C   D
# 0  a  x  1  10
# 1  a  y  2  20
# 2  a  z  3  30
# 3  b  x  4  40
# 4  b  y  5  50
# 5  b  z  6  60

print(s.unstack(level=0))
#     0   1   2   3   4   5
# A   a   a   a   b   b   b
# B   x   y   z   x   y   z
# C   1   2   3   4   5   6
# D  10  20  30  40  50  60

print(df.T)
#     0   1   2   3   4   5
# A   a   a   a   b   b   b
# B   x   y   z   x   y   z
# C   1   2   3   4   5   6
# D  10  20  30  40  50  60

df_m = df.set_index(['A', 'B'])
print(df_m)
#      C   D
# A B       
# a x  1  10
#   y  2  20
#   z  3  30
# b x  4  40
#   y  5  50
#   z  6  60

print(df_m.index)
# MultiIndex(levels=[['a', 'b'], ['x', 'y', 'z']],
#            labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
#            names=['A', 'B'])

df_mu = df_m.unstack()
print(df_mu)
#    C         D        
# B  x  y  z   x   y   z
# A                     
# a  1  2  3  10  20  30
# b  4  5  6  40  50  60

print(df_mu.columns)
# MultiIndex(levels=[['C', 'D'], ['x', 'y', 'z']],
#            labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
#            names=[None, 'B'])

print(df_m.unstack(level=0))
#    C      D    
# A  a  b   a   b
# B              
# x  1  4  10  40
# y  2  5  20  50
# z  3  6  30  60

print(df_m.unstack(level='A'))
#    C      D    
# A  a  b   a   b
# B              
# x  1  4  10  40
# y  2  5  20  50
# z  3  6  30  60

print(df_mu)
#    C         D        
# B  x  y  z   x   y   z
# A                     
# a  1  2  3  10  20  30
# b  4  5  6  40  50  60

print(df_mu.swaplevel(axis=1))
# B  x  y  z   x   y   z
#    C  C  C   D   D   D
# A                     
# a  1  2  3  10  20  30
# b  4  5  6  40  50  60

print(df_mu.swaplevel(axis=1).sort_index(axis=1))
# B  x      y      z    
#    C   D  C   D  C   D
# A                     
# a  1  10  2  20  3  30
# b  4  40  5  50  6  60

print(df_mu.stack())
#      C   D
# A B       
# a x  1  10
#   y  2  20
#   z  3  30
# b x  4  40
#   y  5  50
#   z  6  60

print(df_mu.stack(level=0))
# B     x   y   z
# A              
# a C   1   2   3
#   D  10  20  30
# b C   4   5   6
#   D  40  50  60

print(df)
#    A  B  C   D
# 0  a  x  1  10
# 1  a  y  2  20
# 2  a  z  3  30
# 3  b  x  4  40
# 4  b  y  5  50
# 5  b  z  6  60

print(df.pivot(index='A', columns='B', values='C'))
# B  x  y  z
# A         
# a  1  2  3
# b  4  5  6

print(df.pivot(index='A', columns='B', values=['C', 'D']))
#    C         D        
# B  x  y  z   x   y   z
# A                     
# a  1  2  3  10  20  30
# b  4  5  6  40  50  60

print(df.pivot(index='A', columns='B'))
#    C         D        
# B  x  y  z   x   y   z
# A                     
# a  1  2  3  10  20  30
# b  4  5  6  40  50  60

print(df.set_index(['A', 'B']).unstack('B'))
#    C         D        
# B  x  y  z   x   y   z
# A                     
# a  1  2  3  10  20  30
# b  4  5  6  40  50  60

df.loc[1, 'B'] = 'x'

print(df)
#    A  B  C   D
# 0  a  x  1  10
# 1  a  x  2  20
# 2  a  z  3  30
# 3  b  x  4  40
# 4  b  y  5  50
# 5  b  z  6  60

# print(df.pivot(index='A', columns='B'))
# ValueError: Index contains duplicate entries, cannot reshape

print(df.pivot_table(index='A', columns='B'))
#      C               D            
# B    x    y    z     x     y     z
# A                                 
# a  1.5  NaN  3.0  15.0   NaN  30.0
# b  4.0  5.0  6.0  40.0  50.0  60.0

print(df.pivot_table(index='A', columns='B', aggfunc=sum))
#      C               D            
# B    x    y    z     x     y     z
# A                                 
# a  3.0  NaN  3.0  30.0   NaN  30.0
# b  4.0  5.0  6.0  40.0  50.0  60.0
