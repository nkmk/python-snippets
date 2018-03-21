print(type('string'))
# <class 'str'>

print(type(100))
# <class 'int'>

print(type([0, 1, 2]))
# <class 'list'>

print(type(type('string')))
# <class 'type'>

print(type(str))
# <class 'type'>

print(type('string') is str)
# True

print(type('string') is int)
# False

def is_str(v):
    return type(v) is str

print(is_str('string'))
# True

print(is_str(100))
# False

print(is_str([0, 1, 2]))
# False

def is_str_or_int(v):
    return type(v) in (str, int)

print(is_str_or_int('string'))
# True

print(is_str_or_int(100))
# True

print(is_str_or_int([0, 1, 2]))
# False

def type_condition(v):
    if type(v) is str:
        print('type is str')
    elif type(v) is int:
        print('type is int')
    else:
        print('type is not str or int')

type_condition('string')
# type is str

type_condition(100)
# type is int

type_condition([0, 1, 2])
# type is not str or int
