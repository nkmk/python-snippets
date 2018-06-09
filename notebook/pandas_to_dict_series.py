import pandas as pd
from collections import OrderedDict

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'x', 'あ']},
                  index=['row1', 'row2', 'row3'])

print(df)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

s = df['col1']
print(s)
# row1    1
# row2    2
# row3    3
# Name: col1, dtype: int64

print(type(s))
# <class 'pandas.core.series.Series'>

d = s.to_dict()
print(d)
# {'row1': 1, 'row2': 2, 'row3': 3}

print(type(d))
# <class 'dict'>

s = df.set_index('col2')['col1']
print(s)
# col2
# a    1
# x    2
# あ    3
# Name: col1, dtype: int64

d = s.to_dict()
print(d)
# {'a': 1, 'x': 2, 'あ': 3}

od = df['col1'].to_dict(OrderedDict)
print(od)
# OrderedDict([('row1', 1), ('row2', 2), ('row3', 3)])

print(type(od))
# <class 'collections.OrderedDict'>
