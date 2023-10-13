def func(x, y):
    return x * y

print(func('abc', 3))
# abcabcabc

print(func(4, 3))
# 12

def func_annotations(x: 'for_x', y: 'for_y') -> 'for_return':
    return x * y

print(func_annotations('abc', 3))
# abcabcabc

print(func_annotations(4, 3))
# 12

def func_annotations_default(x: 'for_x', y: 'for_y' = 3) -> 'for_return':
    return x * y

print(func_annotations_default('abc'))
# abcabcabc

print(func_annotations_default(4))
# 12

def func_annotations_type(x: str, y: int) -> str:
    return x * y

print(func_annotations_type('abc', 3))
# abcabcabc

print(func_annotations_type(4, 3))
# 12

def func_annotations(x: 'for_x', y: 'for_y') -> 'for_return':
    return x * y

print(type(func_annotations.__annotations__))
# <class 'dict'>

print(func_annotations.__annotations__)
# {'x': 'for_x', 'y': 'for_y', 'return': 'for_return'}

print(func_annotations.__annotations__['x'])
# for_x
