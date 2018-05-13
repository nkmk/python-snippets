import pandas as pd
import json

s = '{"OTHER": "x", "DATA": [{"name":"Alice","age":25},{"name":"Bob","age":42}]}'

d = json.loads(s)

print(d)
# {'OTHER': 'x', 'DATA': [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 42}]}

print(type(d))
# <class 'dict'>

l_target = d['DATA']

print(l_target)
# [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 42}]

print(type(l_target))
# <class 'list'>

df = pd.io.json.json_normalize(l_target)

print(df)
#    age   name
# 0   25  Alice
# 1   42    Bob

df2 = pd.io.json.json_normalize(json.loads(s)['DATA'])

print(df2)
#    age   name
# 0   25  Alice
# 1   42    Bob
