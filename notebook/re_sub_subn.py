import re

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

result = re.sub(r'[a-z]+@[a-z]+\.com', 'new-address', s)
print(result)
# new-address, new-address, ccc@zzz.net

print(type(result))
# <class 'str'>

result = re.sub(r'([a-z]+)@([a-z]+)\.com', r'\1@\2.net', s)
print(result)
# aaa@xxx.net, bbb@yyy.net, ccc@zzz.net

result = re.sub(r'(?P<local>[a-z]+)@(?P<SLD>[a-z]+)\.com', r'\g<local>@\g<SLD>.net', s)
print(result)
# aaa@xxx.net, bbb@yyy.net, ccc@zzz.net

result = re.sub(r'[a-z]+@[a-z]+\.com', 'new-address', s, count=1)
print(result)
# new-address, bbb@yyy.com, ccc@zzz.net

result = re.subn(r'[a-z]+@[a-z]+\.com', 'new-address', s)
print(result)
# ('new-address, new-address, ccc@zzz.net', 2)

print(result[0])
# new-address, new-address, ccc@zzz.net

print(result[1])
# 2

result = re.subn(r'(?P<local>[a-z]+)@(?P<SLD>[a-z]+)\.com', r'\g<local>@\g<SLD>.net', s)
print(result)
# ('aaa@xxx.net, bbb@yyy.net, ccc@zzz.net', 2)

result = re.subn(r'[a-z]+@[a-z]+\.com', 'new-address', s, count=1)
print(result)
# ('new-address, bbb@yyy.com, ccc@zzz.net', 1)
