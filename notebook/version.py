import sys

sys.version
# '3.6.2 (default, Jul 17 2017, 16:44:45) \n[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]'

type(sys.version)
# str

sys.version_info
# sys.version_info(major=3, minor=6, micro=2, releaselevel='final', serial=0)

type(sys.version_info)
# sys.version_info

sys.version_info.major
# 3

type(sys.version_info.major)
# int

# ---

import platform

platform.python_version()
# '3.6.2'

type(platform.python_version())
# str

platform.python_version_tuple()
# ('3', '6', '2')

type(platform.python_version_tuple())
# tuple

platform.python_version_tuple()[0]
# '3'

type(platform.python_version_tuple()[0])
# str
