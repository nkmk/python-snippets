print(isinstance('string', str))
# True

print(isinstance(100, str))
# False

print(isinstance(100, (int, str)))
# True

def is_str(v):
    return isinstance(v, str)

print(is_str('string'))
# True

print(is_str(100))
# False

print(is_str([0, 1, 2]))
# False

def is_str_or_int(v):
    return isinstance(v, (int, str))

print(is_str_or_int('string'))
# True

print(is_str_or_int(100))
# True

print(is_str_or_int([0, 1, 2]))
# False

def type_condition(v):
    if isinstance(v, str):
        print('type is str')
    elif isinstance(v, int):
        print('type is int')
    else:
        print('type is not str or int')

type_condition('string')
# type is str

type_condition(100)
# type is int

type_condition([0, 1, 2])
# type is not str or int

class Base:
    pass

class Derive(Base):
    pass

base = Base()
print(type(base))
# <class '__main__.Base'>

derive = Derive()
print(type(derive))
# <class '__main__.Derive'>

print(type(derive) is Derive)
# True

print(type(derive) is Base)
# False

print(isinstance(derive, Derive))
# True

print(isinstance(derive, Base))
# True

print(type(True))
# <class 'bool'>

print(type(True) is bool)
# True

print(type(True) is int)
# False

print(isinstance(True, bool))
# True

print(isinstance(True, int))
# True
