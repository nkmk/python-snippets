import platform
import os
import sys

print(platform.system())
# Windows

print(os.name)
# nt

print(sys.platform)
# win32

print(platform.release())
# 10

print(platform.version())
# 10.0.22621

print(platform.platform())
# Windows-10-10.0.22621-SP0

print(platform.win32_ver())
# ('10', '10.0.22621', 'SP0', 'Multiprocessor Free')

print(platform.win32_edition())
# Core

print(platform.win32_is_iot())
# False
