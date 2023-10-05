import platform
import os
import sys

print(platform.system())
# Darwin

print(os.name)
# posix

print(sys.platform)
# darwin

print(platform.release())
# 23.0.0

print(platform.version())
# Darwin Kernel Version 23.0.0: Fri Sep 15 14:42:57 PDT 2023; root:xnu-10002.1.13~1/RELEASE_ARM64_T8112

print(platform.platform())
# macOS-14.0-arm64-arm-64bit

print(platform.platform(terse=True))
# macOS-14.0

print(platform.platform(aliased=True))
# macOS-14.0-arm64-arm-64bit

print(platform.mac_ver())
# ('14.0', ('', '', ''), 'arm64')
