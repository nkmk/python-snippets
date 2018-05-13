import pandas as pd
import pprint
import json

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'x', 'あ']},
                  index=['row1', 'row2', 'row3'])

print(df)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

print(df.to_json())
# {"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"\u3042"}}

print(type(df.to_json()))
# <class 'str'>

path = 'data/src/sample_from_pandas_columns.json'

df.to_json(path)

with open(path) as f:
    s = f.read()
    print(s)
    print(type(s))
# {"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"\u3042"}}
# <class 'str'>

with open(path, encoding='unicode-escape') as f:
    s = f.read()
    print(s)
    print(type(s))
# {"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"あ"}}
# <class 'str'>

with open(path) as f:
    d = json.load(f)
    print(d)
    print(type(d))
# {'col1': {'row1': 1, 'row2': 2, 'row3': 3}, 'col2': {'row1': 'a', 'row2': 'x', 'row3': 'あ'}}
# <class 'dict'>

df_read = pd.read_json(path)
print(df_read)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

df.to_json('data/src/sample_from_pandas_columns.gz', compression='gzip')

print(df.to_json(orient='split'))
# {"columns":["col1","col2"],"index":["row1","row2","row3"],"data":[[1,"a"],[2,"x"],[3,"\u3042"]]}

pprint.pprint(json.loads(df.to_json(orient='split')))
# {'columns': ['col1', 'col2'],
#  'data': [[1, 'a'], [2, 'x'], [3, 'あ']],
#  'index': ['row1', 'row2', 'row3']}

print(df.to_json(orient='records'))
# [{"col1":1,"col2":"a"},{"col1":2,"col2":"x"},{"col1":3,"col2":"\u3042"}]

pprint.pprint(json.loads(df.to_json(orient='records')), width=40)
# [{'col1': 1, 'col2': 'a'},
#  {'col1': 2, 'col2': 'x'},
#  {'col1': 3, 'col2': 'あ'}]

print(df.to_json(orient='records', lines=True))
# {"col1":1,"col2":"a"}
# {"col1":2,"col2":"x"}
# {"col1":3,"col2":"\u3042"}

print(df.to_json(orient='index'))
# {"row1":{"col1":1,"col2":"a"},"row2":{"col1":2,"col2":"x"},"row3":{"col1":3,"col2":"\u3042"}}

pprint.pprint(json.loads(df.to_json(orient='index')))
# {'row1': {'col1': 1, 'col2': 'a'},
#  'row2': {'col1': 2, 'col2': 'x'},
#  'row3': {'col1': 3, 'col2': 'あ'}}

print(df.to_json(orient='columns'))
# {"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"\u3042"}}

pprint.pprint(json.loads(df.to_json(orient='columns')))
# {'col1': {'row1': 1, 'row2': 2, 'row3': 3},
#  'col2': {'row1': 'a', 'row2': 'x', 'row3': 'あ'}}

print(df.to_json(orient='values'))
# [[1,"a"],[2,"x"],[3,"\u3042"]]

pprint.pprint(json.loads(df.to_json(orient='values')))
# [[1, 'a'], [2, 'x'], [3, 'あ']]

print(df.to_json(orient='table'))
# {"schema": {"fields":[{"name":"index","type":"string"},{"name":"col1","type":"integer"},{"name":"col2","type":"string"}],"primaryKey":["index"],"pandas_version":"0.20.0"}, "data": [{"index":"row1","col1":1,"col2":"a"},{"index":"row2","col1":2,"col2":"x"},{"index":"row3","col1":3,"col2":"\u3042"}]}

pprint.pprint(json.loads(df.to_json(orient='table')))
# {'data': [{'col1': 1, 'col2': 'a', 'index': 'row1'},
#           {'col1': 2, 'col2': 'x', 'index': 'row2'},
#           {'col1': 3, 'col2': 'あ', 'index': 'row3'}],
#  'schema': {'fields': [{'name': 'index', 'type': 'string'},
#                        {'name': 'col1', 'type': 'integer'},
#                        {'name': 'col2', 'type': 'string'}],
#             'pandas_version': '0.20.0',
#             'primaryKey': ['index']}}

print(df.to_json(force_ascii=False))
# {"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"あ"}}
