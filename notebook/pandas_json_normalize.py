import pandas as pd

l = [{'name': 'Alice', 'age': 25, 'id': {'x': 2, 'y': 8}},
     {'name': 'Bob', 'id': {'x': 10, 'y': 4}}]

df = pd.io.json.json_normalize(l)

print(df)
#     age  id.x  id.y   name
# 0  25.0     2     8  Alice
# 1   NaN    10     4    Bob

df_sep = pd.io.json.json_normalize(l, sep='-')

print(df_sep)
#     age  id-x  id-y   name
# 0  25.0     2     8  Alice
# 1   NaN    10     4    Bob
