import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

result = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(result)
# ['aaa@xxx.com', 'bbb@yyy.net', 'ccc@zzz.org']

print(len(result))
# 3

print(re.findall(r'([a-z]+)@([a-z]+)\.([a-z]+)', s))
# [('aaa', 'xxx', 'com'), ('bbb', 'yyy', 'net'), ('ccc', 'zzz', 'org')]

print(re.findall(r'(([a-z]+)@([a-z]+)\.([a-z]+))', s))
# [('aaa@xxx.com', 'aaa', 'xxx', 'com'), ('bbb@yyy.net', 'bbb', 'yyy', 'net'), ('ccc@zzz.org', 'ccc', 'zzz', 'org')]

print(re.findall('[0-9]+', s))
# []

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

result = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(result)
# <callable_iterator object at 0x107863070>

print(type(result))
# <class 'callable_iterator'>

for m in result:
    print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>
# <re.Match object; span=(12, 23), match='bbb@yyy.net'>
# <re.Match object; span=(24, 35), match='ccc@zzz.org'>

l = list(re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s))
print(l)
# [<re.Match object; span=(0, 11), match='aaa@xxx.com'>, <re.Match object; span=(12, 23), match='bbb@yyy.net'>, <re.Match object; span=(24, 35), match='ccc@zzz.org'>]

print(l[0])
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(type(l[0]))
# <class 're.Match'>

print(l[0].span())
# (0, 11)

print([m.span() for m in re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)])
# [(0, 11), (12, 23), (24, 35)]

result = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)

for m in result:
    print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>
# <re.Match object; span=(12, 23), match='bbb@yyy.net'>
# <re.Match object; span=(24, 35), match='ccc@zzz.org'>

print(list(result))
# []
