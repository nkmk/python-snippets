import urllib

print(type(urllib))
# <class 'module'>

print(urllib)
# <module 'urllib' from '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/__init__.py'>

# print(urllib.error)
# AttributeError: module 'urllib' has no attribute 'error'

import urllib.error

print(urllib.error)
# <module 'urllib.error' from '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/error.py'>

print(urllib.error.HTTPError)
# <class 'urllib.error.HTTPError'>

from urllib import error

print(error)
# <module 'urllib.error' from '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/error.py'>

print(error.HTTPError)
# <class 'urllib.error.HTTPError'>

from urllib.error import HTTPError

print(HTTPError)
# <class 'urllib.error.HTTPError'>
