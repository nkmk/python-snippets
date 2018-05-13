import pandas as pd
import pprint
from collections import OrderedDict

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'x', 'あ']},
                  index=['row1', 'row2', 'row3'])

print(df)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

d = df.to_dict()

pprint.pprint(d)
# {'col1': {'row1': 1, 'row2': 2, 'row3': 3},
#  'col2': {'row1': 'a', 'row2': 'x', 'row3': 'あ'}}

print(type(d))
# <class 'dict'>

d_dict = df.to_dict(orient='dict')

pprint.pprint(d_dict)
# {'col1': {'row1': 1, 'row2': 2, 'row3': 3},
#  'col2': {'row1': 'a', 'row2': 'x', 'row3': 'あ'}}

print(d_dict['col1'])
# {'row1': 1, 'row2': 2, 'row3': 3}

print(type(d_dict['col1']))
# <class 'dict'>

d_list = df.to_dict(orient='list')

pprint.pprint(d_list)
# {'col1': [1, 2, 3], 'col2': ['a', 'x', 'あ']}

print(d_list['col1'])
# [1, 2, 3]

print(type(d_list['col1']))
# <class 'list'>

d_series = df.to_dict(orient='series')

pprint.pprint(d_series)
# {'col1': row1    1
# row2    2
# row3    3
# Name: col1, dtype: int64,
#  'col2': row1    a
# row2    x
# row3    あ
# Name: col2, dtype: object}

print(d_series['col1'])
# row1    1
# row2    2
# row3    3
# Name: col1, dtype: int64

print(type(d_series['col1']))
# <class 'pandas.core.series.Series'>

d_split = df.to_dict(orient='split')

pprint.pprint(d_split)
# {'columns': ['col1', 'col2'],
#  'data': [[1, 'a'], [2, 'x'], [3, 'あ']],
#  'index': ['row1', 'row2', 'row3']}

print(d_split['columns'])
# ['col1', 'col2']

print(type(d_split['columns']))
# <class 'list'>

l_records = df.to_dict(orient='records')

pprint.pprint(l_records)
# [{'col1': 1, 'col2': 'a'}, {'col1': 2, 'col2': 'x'}, {'col1': 3, 'col2': 'あ'}]

print(type(l_records))
# <class 'list'>

print(l_records[0])
# {'col1': 1, 'col2': 'a'}

print(type(l_records[0]))
# <class 'dict'>

d_index = df.to_dict(orient='index')

pprint.pprint(d_index)
# {'row1': {'col1': 1, 'col2': 'a'},
#  'row2': {'col1': 2, 'col2': 'x'},
#  'row3': {'col1': 3, 'col2': 'あ'}}

print(d_index['row1'])
# {'col1': 1, 'col2': 'a'}

print(type(d_index['row1']))
# <class 'dict'>

od = df.to_dict(into=OrderedDict)

pprint.pprint(od)
# OrderedDict([('col1', OrderedDict([('row1', 1), ('row2', 2), ('row3', 3)])),
#              ('col2',
#               OrderedDict([('row1', 'a'), ('row2', 'x'), ('row3', 'あ')]))])

print(type(od))
# <class 'collections.OrderedDict'>

print(od['col1'])
# OrderedDict([('row1', 1), ('row2', 2), ('row3', 3)])

print(type(od['col1']))
# <class 'collections.OrderedDict'>
