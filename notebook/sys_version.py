import sys

print(sys.version)
# 3.7.0 (default, Jun 29 2018, 20:13:13) 
# [Clang 9.1.0 (clang-902.0.39.2)]

print(type(sys.version))
# <class 'str'>

print(sys.version_info)
# sys.version_info(major=3, minor=7, micro=0, releaselevel='final', serial=0)

print(type(sys.version_info))
# <class 'sys.version_info'>

print(sys.version_info[0])
# 3

print(sys.version_info.major)
# 3

if sys.version_info.major == 3:
    print('Python3')
else:
    print('Python2')
# Python3
