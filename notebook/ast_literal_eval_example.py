import ast

s = '["a", "b", "c"]'

l = ast.literal_eval(s)
print(l)
# ['a', 'b', 'c']

print(type(l))
# <class 'list'>

s = '["x", 1, True]'

l = ast.literal_eval(s)
print(l)
# ['x', 1, True]

print(type(l[0]))
# <class 'str'>

print(type(l[1]))
# <class 'int'>

print(type(l[2]))
# <class 'bool'>

s = '{"key1": 1, "key2": 2}'

d = ast.literal_eval(s)
print(d)
# {'key1': 1, 'key2': 2}

print(type(d))
# <class 'dict'>

s = '{1, 2, 3}'

se = ast.literal_eval(s)
print(se)
# {1, 2, 3}

print(type(se))
# <class 'set'>

s = '["x", 1 + 10]'

print(eval(s))
# ['x', 11]

# print(ast.literal_eval(s))
# ValueError: malformed node or string

a = 100
print(eval('[1, a]'))
# [1, 100]

# a = 100
# print(ast.literal_eval('[1, a]'))
# ValueError: malformed node or string

import json

s = '{"key1": [1, 2, 3], "key2": "abc"}'

print(json.loads(s))
# {'key1': [1, 2, 3], 'key2': 'abc'}

print(ast.literal_eval(s))
# {'key1': [1, 2, 3], 'key2': 'abc'}

s = '[True, False, None]'

# print(json.loads(s))
# JSONDecodeError: Expecting value:

print(ast.literal_eval(s))
# [True, False, None]

s = '[true, false, null]'

print(json.loads(s))
# [True, False, None]

# print(ast.literal_eval(s))
# ValueError: malformed node or string

s = "{'key1': 'abc', 'key2': '''xyz'''}"

# print(json.loads(s))
# JSONDecodeError: Expecting property name enclosed in double quotes

print(ast.literal_eval(s))
# {'key1': 'abc', 'key2': 'xyz'}

s = 'a, b, c'

l = s.split(', ')
print(l)
# ['a', 'b', 'c']

print(type(l))
# <class 'list'>

s = '1-2-3'

l = s.split('-')
print(l)
# ['1', '2', '3']

print(type(l[0]))
# <class 'str'>

l = [int(c) for c in s.split('-')]
print(l)
# [1, 2, 3]

print(type(l[0]))
# <class 'int'>
