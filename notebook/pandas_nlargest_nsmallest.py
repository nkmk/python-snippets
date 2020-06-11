import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [2, 3, 1, 3, 3, 4],
                   'col2': [30, 10, 10, 40, 40, 20]},
                  index=['A', 'B', 'C', 'D', 'E', 'F'])
print(df)
#    col1  col2
# A     2    30
# B     3    10
# C     1    10
# D     3    40
# E     3    40
# F     4    20

s = df['col1']
print(s)
# A    2
# B    3
# C    1
# D    3
# E    3
# F    4
# Name: col1, dtype: int64

print(df.max())
# col1     4
# col2    40
# dtype: int64

print(type(df.max()))
# <class 'pandas.core.series.Series'>

print(df.min())
# col1     1
# col2    10
# dtype: int64

print(type(df.min()))
# <class 'pandas.core.series.Series'>

print(df.max(axis=1))
# A    30
# B    10
# C    10
# D    40
# E    40
# F    20
# dtype: int64

print(df.min(axis=1))
# A    2
# B    3
# C    1
# D    3
# E    3
# F    4
# dtype: int64

print(s.max())
# 4

print(type(s.max()))
# <class 'numpy.int64'>

print(s.min())
# 1

print(type(s.min()))
# <class 'numpy.int64'>

print(s.nlargest(4))
# F    4
# B    3
# D    3
# E    3
# Name: col1, dtype: int64

print(type(s.nlargest(4)))
# <class 'pandas.core.series.Series'>

print(s.nsmallest(4))
# C    1
# A    2
# B    3
# D    3
# Name: col1, dtype: int64

print(type(s.nsmallest(4)))
# <class 'pandas.core.series.Series'>

print(s.nlargest(1))
# F    4
# Name: col1, dtype: int64

print(type(s.nlargest(1)))
# <class 'pandas.core.series.Series'>

print(df.nlargest(4, 'col1'))
#    col1  col2
# F     4    20
# B     3    10
# D     3    40
# E     3    40

print(type(df.nlargest(4, 'col1')))
# <class 'pandas.core.frame.DataFrame'>

print(df.nsmallest(4, 'col1'))
#    col1  col2
# C     1    10
# A     2    30
# B     3    10
# D     3    40

print(type(df.nsmallest(4, 'col1')))
# <class 'pandas.core.frame.DataFrame'>

print(df.nlargest(1, 'col1'))
#    col1  col2
# F     4    20

print(type(df.nlargest(1, 'col1')))
# <class 'pandas.core.frame.DataFrame'>

print(df.nlargest(4, ['col1', 'col2']))
#    col1  col2
# F     4    20
# D     3    40
# E     3    40
# B     3    10

print(df.nlargest(4, ['col2', 'col1']))
#    col1  col2
# D     3    40
# E     3    40
# A     2    30
# F     4    20

print(df.nsmallest(4, 'col1'))
#    col1  col2
# C     1    10
# A     2    30
# B     3    10
# D     3    40

print(df.nsmallest(4, 'col1', keep='first'))
#    col1  col2
# C     1    10
# A     2    30
# B     3    10
# D     3    40

print(df.nsmallest(4, 'col1', keep='last'))
#    col1  col2
# C     1    10
# A     2    30
# E     3    40
# D     3    40

print(df.nsmallest(4, 'col1', keep='all'))
#    col1  col2
# C     1    10
# A     2    30
# B     3    10
# D     3    40
# E     3    40

print(df.nsmallest(3, ['col1', 'col2'], keep='all'))
#    col1  col2
# C     1    10
# A     2    30
# B     3    10

print(df.nsmallest(4, ['col1', 'col2'], keep='all'))
#    col1  col2
# C     1    10
# A     2    30
# B     3    10
# D     3    40
# E     3    40

print(df['col1'].nsmallest(4).tolist())
# [1, 2, 3, 3]

print(type(df['col1'].nsmallest(4).tolist()))
# <class 'list'>

print(df['col1'].nsmallest(4).to_numpy())
# [1 2 3 3]

print(type(df['col1'].nsmallest(4).to_numpy()))
# <class 'numpy.ndarray'>

print(df['col1'].nsmallest(4).values)
# [1 2 3 3]

print(type(df['col1'].nsmallest(4).values))
# <class 'numpy.ndarray'>

print(df['col1'].nsmallest(3))
# C    1
# A    2
# B    3
# Name: col1, dtype: int64

print(df['col2'].nsmallest(3))
# B    10
# C    10
# F    20
# Name: col2, dtype: int64

print([df[col_name].nsmallest(3).tolist() for col_name in df])
# [[1, 2, 3], [10, 10, 20]]

print({col_name: col.nsmallest(3).tolist() for col_name, col in df.iteritems()})
# {'col1': [1, 2, 3], 'col2': [10, 10, 20]}

print(np.array([df[col_name].nsmallest(3).tolist() for col_name in df]))
# [[ 1  2  3]
#  [10 10 20]]

print([df[col_name].nsmallest(3, keep='all').tolist() for col_name in df])
# [[1, 2, 3, 3, 3], [10, 10, 20]]

print({col_name: col.nsmallest(3, keep='all').tolist() for col_name, col in df.iteritems()})
# {'col1': [1, 2, 3, 3, 3], 'col2': [10, 10, 20]}

print(np.array([df[col_name].nsmallest(3, keep='all').tolist() for col_name in df]))
# [list([1, 2, 3, 3, 3]) list([10, 10, 20])]
