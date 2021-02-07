import pprint

pprint.pprint(ArithmeticError.__subclasses__())
# [<class 'FloatingPointError'>,
#  <class 'OverflowError'>,
#  <class 'ZeroDivisionError'>,
#  <class 'decimal.DecimalException'>]

print(type(ArithmeticError.__subclasses__()))
# <class 'list'>

print(type(ArithmeticError.__subclasses__()[0]))
# <class 'type'>

class Base(): pass
class SubA(Base): pass
class SubB(Base): pass
class SubSubA(SubA): pass
class SUbSubB(SubB): pass

print(Base.__subclasses__())
# [<class '__main__.SubA'>, <class '__main__.SubB'>]

# https://stackoverflow.com/a/3862957
def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])

pprint.pprint(all_subclasses(Base))
# {<class '__main__.SubA'>,
#  <class '__main__.SubB'>,
#  <class '__main__.SubSubA'>,
#  <class '__main__.SUbSubB'>}

print(len(dict.__subclasses__()))
# 24

import pandas as pd

print(len(dict.__subclasses__()))
# 29
