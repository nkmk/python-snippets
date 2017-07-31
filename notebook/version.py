import sys

print(sys.version)
# 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]

print(type(sys.version))
# <class 'str'>

print(sys.version_info)
# sys.version_info(major=3, minor=6, micro=2, releaselevel='final', serial=0)

print(type(sys.version_info))
# <class 'sys.version_info'>

print(sys.version_info.major)
# 3

print(type(sys.version_info.major))
# <class 'int'>

# ---

import platform

print(platform.python_version())
# 3.6.2

print(type(platform.python_version()))
# <class 'str'>

print(platform.python_version_tuple())
# ('3', '6', '2')

print(type(platform.python_version_tuple()))
# <class 'tuple'>

print(platform.python_version_tuple()[0])
# 3

print(type(platform.python_version_tuple()[0]))
# <class 'str'>
