import pandas as pd
import json

s = '{"OTHER": "x", "DATA": [{"name":"Alice","age":25},{"name":"Bob","age":42}]}'

print(pd.read_json(s))
#   OTHER                          DATA
# 0     x  {'name': 'Alice', 'age': 25}
# 1     x    {'name': 'Bob', 'age': 42}

d = json.loads(s)
print(d)
# {'OTHER': 'x', 'DATA': [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 42}]}

print(type(d))
# <class 'dict'>

print(pd.json_normalize(d))
#   OTHER                                               DATA
# 0     x  [{'name': 'Alice', 'age': 25}, {'name': 'Bob',...

print(pd.json_normalize(d, record_path='DATA'))
#     name  age
# 0  Alice   25
# 1    Bob   42

print(pd.json_normalize(d, record_path='DATA', meta='OTHER'))
#     name  age OTHER
# 0  Alice   25     x
# 1    Bob   42     x

print(d['DATA'])
# [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 42}]

print(type(d['DATA']))
# <class 'list'>

print(pd.DataFrame(d['DATA']))
#     name  age
# 0  Alice   25
# 1    Bob   42

print(pd.json_normalize(d['DATA']))
#     name  age
# 0  Alice   25
# 1    Bob   42
