import pandas as pd

l_simple = [{'name': 'Alice', 'age': 25},
            {'name': 'Bob'}]

print(pd.DataFrame(l_simple))
#     name   age
# 0  Alice  25.0
# 1    Bob   NaN

print(pd.json_normalize(l_simple))
#     name   age
# 0  Alice  25.0
# 1    Bob   NaN

l_nested = [{'name': 'Alice', 'age': 25, 'id': {'x': 2, 'y': 8}},
            {'name': 'Bob', 'id': {'x': 10, 'y': 4}}]

print(pd.DataFrame(l_nested))
#     name   age                 id
# 0  Alice  25.0   {'x': 2, 'y': 8}
# 1    Bob   NaN  {'x': 10, 'y': 4}

print(pd.json_normalize(l_nested))
#     name   age  id.x  id.y
# 0  Alice  25.0     2     8
# 1    Bob   NaN    10     4

print(pd.json_normalize(l_nested, sep='_'))
#     name   age  id_x  id_y
# 0  Alice  25.0     2     8
# 1    Bob   NaN    10     4

l_complex = [{'label': 'X',
              'info' : {'n': 'nx', 'm': 'mx'},
              'data': [{'a': 1, 'b': 2},
                       {'a': 3, 'b': 4}]},
             {'label': 'Y',
              'info' : {'n': 'ny', 'm': 'my'},
              'data': [{'a': 10, 'b': 20},
                       {'a': 30, 'b': 40}]}]

print(pd.json_normalize(l_complex))
#   label                                      data info.n info.m
# 0     X      [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]     nx     mx
# 1     Y  [{'a': 10, 'b': 20}, {'a': 30, 'b': 40}]     ny     my

print(pd.json_normalize(l_complex, record_path='data'))
#     a   b
# 0   1   2
# 1   3   4
# 2  10  20
# 3  30  40

print(pd.json_normalize(l_complex, record_path='data', record_prefix='data_'))
#    data_a  data_b
# 0       1       2
# 1       3       4
# 2      10      20
# 3      30      40

print(pd.json_normalize(l_complex, record_path='data',
                        meta='label'))
#     a   b label
# 0   1   2     X
# 1   3   4     X
# 2  10  20     Y
# 3  30  40     Y

print(pd.json_normalize(l_complex, record_path='data',
                        meta='label', meta_prefix='meta_'))
#     a   b meta_label
# 0   1   2          X
# 1   3   4          X
# 2  10  20          Y
# 3  30  40          Y

print(pd.json_normalize(l_complex, record_path='data',
                        meta='info'))
#     a   b                    info
# 0   1   2  {'n': 'nx', 'm': 'mx'}
# 1   3   4  {'n': 'nx', 'm': 'mx'}
# 2  10  20  {'n': 'ny', 'm': 'my'}
# 3  30  40  {'n': 'ny', 'm': 'my'}

print(pd.json_normalize(l_complex, record_path='data',
                        meta=[['info', 'n'], ['info', 'm']]))
#     a   b info.n info.m
# 0   1   2     nx     mx
# 1   3   4     nx     mx
# 2  10  20     ny     my
# 3  30  40     ny     my

print(pd.json_normalize(l_complex, record_path='data',
                        meta=[['info', 'n'], ['info', 'm']],
                        sep='_'))
#     a   b info_n info_m
# 0   1   2     nx     mx
# 1   3   4     nx     mx
# 2  10  20     ny     my
# 3  30  40     ny     my

print(pd.json_normalize(l_complex, record_path='data',
                        meta=['label', ['info', 'n'], ['info', 'm']],
                        sep='_'))
#     a   b label info_n info_m
# 0   1   2     X     nx     mx
# 1   3   4     X     nx     mx
# 2  10  20     Y     ny     my
# 3  30  40     Y     ny     my

print(pd.json_normalize(l_complex, record_path='data',
                        meta=[['info', 'n']]))
#     a   b info.n
# 0   1   2     nx
# 1   3   4     nx
# 2  10  20     ny
# 3  30  40     ny

# print(pd.json_normalize(l_complex, record_path='data',
#                         meta=['info', 'n']))
# KeyError: "Try running with errors='ignore' as key 'n' is not always present"
