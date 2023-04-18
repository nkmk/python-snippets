a = None
print(a)
# None

print(type(a))
# <class 'NoneType'>

def func_none():
    # do something
    pass

x = func_none()
print(x)
# None

a = None
print(a is None)
# True

print(a is not None)
# False

a = None
print(a == None)
# True

print(a != None)
# False

class MyClass:
    def __eq__(self, other):
        return True

my_obj = MyClass()
print(my_obj == None)
# True

print(my_obj is None)
# False

print(bool(None))
# False

a = None

if a:
    print(f'{a} is not None')
else:
    print(f'{a} is None')
# None is None

a = 0

if a:
    print(f'{a} is not None')
else:
    print(f'{a} is None')
# 0 is None

a = None

if a is not None:
    print(f'{a} is not None')
else:
    print(f'{a} is None')
# None is None

a = 0

if a is not None:
    print(f'{a} is not None')
else:
    print(f'{a} is None')
# 0 is not None
