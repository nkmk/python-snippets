i = 100
f = 1.23

print(type(i))
print(type(f))
# <class 'int'>
# <class 'float'>

print(isinstance(i, int))
# True

print(isinstance(i, float))
# False

print(isinstance(f, int))
# False

print(isinstance(f, float))
# True

f_i = 100.0

print(type(f_i))
# <class 'float'>

print(isinstance(f_i, int))
# False

print(isinstance(f_i, float))
# True

f = 1.23

print(f.is_integer())
# False

f_i = 100.0

print(f_i.is_integer())
# True

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

print(is_integer_num(100))
# True

print(is_integer_num(1.23))
# False

print(is_integer_num(100.0))
# True

print(is_integer_num('100'))
# False

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

print(is_integer(100))
# True

print(is_integer(100.0))
# True

print(is_integer(1.23))
# False

print(is_integer('100'))
# True

print(is_integer('100.0'))
# True

print(is_integer('1.23'))
# False

print(is_integer('string'))
# False
