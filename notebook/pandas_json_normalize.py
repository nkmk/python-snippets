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

ll = [{'label': 'X',
       'info' : {'n': 'nx', 'm': 'mx'},
       'data': [{'a': 1, 'b': 2},
                {'a': 3, 'b': 4}]},
      {'label': 'Y',
       'info' : {'n': 'ny', 'm': 'my'},
       'data': [{'a': 10, 'b': 20},
                {'a': 30, 'b': 40}]}]

df_l = pd.io.json.json_normalize(ll, record_path='data')

print(df_l)
#     a   b
# 0   1   2
# 1   3   4
# 2  10  20
# 3  30  40

df_lm = pd.io.json.json_normalize(ll, record_path='data',
                                  meta=['label', ['info', 'n'], ['info', 'm']],
                                  sep='_')

print(df_lm)
#     a   b label info_n info_m
# 0   1   2     X     nx     mx
# 1   3   4     X     nx     mx
# 2  10  20     Y     ny     my
# 3  30  40     Y     ny     my
