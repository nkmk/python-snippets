import platform

print(platform.system())
# Darwin

print(platform.release())
# 18.2.0

print(platform.version())
# Darwin Kernel Version 18.2.0: Mon Nov 12 20:24:46 PST 2018; root:xnu-4903.231.4~2/RELEASE_X86_64

print(platform.platform())
# Darwin-18.2.0-x86_64-i386-64bit

print(platform.platform(terse=True))
# Darwin-18.2.0

print(platform.platform(aliased=True))
# Darwin-18.2.0-x86_64-i386-64bit

print(platform.mac_ver())
# ('10.14.2', ('', '', ''), 'x86_64')
