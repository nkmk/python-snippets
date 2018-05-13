import pandas as pd
import json

s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"\u3042"}}'

df_s = pd.read_json(s)

print(df_s)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

s_single_quote = "{'col1':{'row1':1,'row2':2,'row3':3},'col2':{'row1':'a','row2':'x','row3':'\u3042'}}"

# df_s_single_quote = pd.read_json(s_single_quote)
# ValueError: Expected object or value

print(pd.read_json(s_single_quote.replace("'", '"')))
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

df_f = pd.read_json('data/src/sample_from_pandas_columns.json')

print(df_f)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

df_gzip = pd.read_json('data/src/sample_from_pandas_columns.gz', compression='infer')

print(df_gzip)
#       col1 col2
# row1     1    a
# row2     2    x
# row3     3    あ

df_s_index = pd.read_json(s, orient='index')

print(df_s_index)
#      row1 row2 row3
# col1    1    2    3
# col2    a    x    あ

# df_s_split = pd.read_json(s, orient='split')
# ValueError: JSON data had unexpected key(s): col2, col1

s_jsonl = '''{"col1":1,"col2":"a"}
{"col1":2,"col2":"x"}
{"col1":3,"col2":"\u3042"}'''

print(s_jsonl)
# {"col1":1,"col2":"a"}
# {"col1":2,"col2":"x"}
# {"col1":3,"col2":"あ"}

df_s_jsonl = pd.read_json(s_jsonl, orient='records', lines=True)

print(df_s_jsonl)
#    col1 col2
# 0     1    a
# 1     2    x
# 2     3    あ

s_nested = '{"OTHER": "x", "DATA": {"col1":{"row1":1,"row2":2},"col2":{"row1":"a","row2":"x"}}}'

print(pd.read_json(s_nested))
#                             DATA OTHER
# col1      {'row1': 1, 'row2': 2}     x
# col2  {'row1': 'a', 'row2': 'x'}     x

d = json.loads(s_nested)

print(d)
# {'OTHER': 'x', 'DATA': {'col1': {'row1': 1, 'row2': 2}, 'col2': {'row1': 'a', 'row2': 'x'}}}

print(type(d))
# <class 'dict'>

d_target = d['DATA']

print(d_target)
# {'col1': {'row1': 1, 'row2': 2}, 'col2': {'row1': 'a', 'row2': 'x'}}

print(type(d_target))
# <class 'dict'>

s_target = json.dumps(d_target)

print(s_target)
# {"col1": {"row1": 1, "row2": 2}, "col2": {"row1": "a", "row2": "x"}}

print(type(s_target))
# <class 'str'>

df_target = pd.read_json(s_target)

print(df_target)
#       col1 col2
# row1     1    a
# row2     2    x

df_target2 = pd.read_json(json.dumps(json.loads(s_nested)['DATA']))

print(df_target2)
#       col1 col2
# row1     1    a
# row2     2    x
