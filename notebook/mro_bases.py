print(bool.__mro__)
# (<class 'bool'>, <class 'int'>, <class 'object'>)

print(type(True).__mro__)
# (<class 'bool'>, <class 'int'>, <class 'object'>)

print(type(bool.__mro__))
# <class 'tuple'>

print(type(bool.__mro__[0]))
# <class 'type'>

print([c.__name__ for c in bool.__mro__])
# ['bool', 'int', 'object']

import pprint

pprint.pprint(ZeroDivisionError.__mro__)
# (<class 'ZeroDivisionError'>,
#  <class 'ArithmeticError'>,
#  <class 'Exception'>,
#  <class 'BaseException'>,
#  <class 'object'>)

class BaseA(): pass
class BaseB(): pass
class Sub(BaseA, BaseB): pass

pprint.pprint(Sub.__mro__)
# (<class '__main__.Sub'>,
#  <class '__main__.BaseA'>,
#  <class '__main__.BaseB'>,
#  <class 'object'>)

print(bool.__bases__)
# (<class 'int'>,)

print(type(bool.__bases__))
# <class 'tuple'>

print(type(bool.__bases__[0]))
# <class 'type'>

print(object.__bases__)
# ()

print(Sub.__bases__)
# (<class '__main__.BaseA'>, <class '__main__.BaseB'>)

print(bool.__base__)
# <class 'int'>

print(Sub.__base__)
# <class '__main__.BaseA'>
