import platform
import os
import sys

print(platform.system())
# Linux

print(os.name)
# posix

print(sys.platform)
# linux

print(platform.release())
# 5.15.0-86-generic

print(platform.version())
# #96-Ubuntu SMP Wed Sep 20 08:23:49 UTC 2023

print(platform.platform())
# Linux-5.15.0-86-generic-x86_64-with-glibc2.35

import distro

print(distro.name())
# Ubuntu

print(distro.id())
# ubuntu

print(distro.version())
# 22.04
