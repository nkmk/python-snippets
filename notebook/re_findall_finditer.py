import re

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

result = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(result)
# ['aaa@xxx.com', 'bbb@yyy.com', 'ccc@zzz.net']

print(len(result))
# 3

result = re.findall(r'([a-z]+)@([a-z]+)\.([a-z]+)', s)
print(result)
# [('aaa', 'xxx', 'com'), ('bbb', 'yyy', 'com'), ('ccc', 'zzz', 'net')]

result = re.findall(r'(([a-z]+)@([a-z]+)\.([a-z]+))', s)
print(result)
# [('aaa@xxx.com', 'aaa', 'xxx', 'com'), ('bbb@yyy.com', 'bbb', 'yyy', 'com'), ('ccc@zzz.net', 'ccc', 'zzz', 'net')]

result = re.findall('[0-9]+', s)
print(result)
# []

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

result = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(result)
# <callable_iterator object at 0x10b0efa90>

print(type(result))
# <class 'callable_iterator'>

for m in result:
    print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>
# <re.Match object; span=(13, 24), match='bbb@yyy.com'>
# <re.Match object; span=(26, 37), match='ccc@zzz.net'>

l = list(re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s))
print(l)
# [<re.Match object; span=(0, 11), match='aaa@xxx.com'>, <re.Match object; span=(13, 24), match='bbb@yyy.com'>, <re.Match object; span=(26, 37), match='ccc@zzz.net'>]

print(l[0])
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(type(l[0]))
# <class 're.Match'>

print(l[0].span())
# (0, 11)

print([m.span() for m in re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)])
# [(0, 11), (13, 24), (26, 37)]

result = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)

for m in result:
    print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>
# <re.Match object; span=(13, 24), match='bbb@yyy.com'>
# <re.Match object; span=(26, 37), match='ccc@zzz.net'>

print(list(result))
# []
