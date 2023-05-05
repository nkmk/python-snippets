import sys

print(sys.version)
# 3.11.3 (main, Apr  7 2023, 20:13:31) [Clang 14.0.0 (clang-1400.0.29.202)]

print(type(sys.version))
# <class 'str'>

print(sys.version_info)
# sys.version_info(major=3, minor=11, micro=3, releaselevel='final', serial=0)

print(type(sys.version_info))
# <class 'sys.version_info'>

print(sys.version_info[0])
# 3

print(sys.version_info.major)
# 3

if sys.version_info[0] == 3:
    print('Python3')
else:
    print('Python2')
# Python3
