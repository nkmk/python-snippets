import keyword
import pprint

print(type(keyword.kwlist))
# <class 'list'>

print(len(keyword.kwlist))
# 35

pprint.pprint(keyword.kwlist, compact=True)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
#  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
#  'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(keyword.kwlist[0])
# False

print(type(keyword.kwlist[0]))
# <class 'str'>

# True = 100
# SyntaxError: can't assign to keyword

print(keyword.iskeyword('None'))
# True

print(keyword.iskeyword('none'))
# False
