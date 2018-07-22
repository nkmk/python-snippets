import collections

print(collections)
# <module 'collections' from '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/collections/__init__.py'>

print(collections.Counter)
# <class 'collections.Counter'>

# import collections.Counter
# ModuleNotFoundError: No module named 'collections.Counter'

from collections import Counter

print(Counter)
# <class 'collections.Counter'>
