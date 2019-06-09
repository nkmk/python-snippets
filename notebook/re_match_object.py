import re

s = 'aaa@xxx.com'

m = re.match(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(type(m))
# <class 're.Match'>

print(m.start())
# 0

print(m.end())
# 11

print(m.span())
# (0, 11)

print(m.group())
# aaa@xxx.com

print(type(m.group()))
# <class 'str'>

m = re.match(r'([a-z]+)@([a-z]+)\.([a-z]+)', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(m.groups())
# ('aaa', 'xxx', 'com')

print(m.group())
# aaa@xxx.com

print(m.group(0))
# aaa@xxx.com

print(m.group(1))
# aaa

print(m.group(2))
# xxx

print(m.group(3))
# com

# print(m.group(4))
# IndexError: no such group

print(m.group(0, 1, 3))
# ('aaa@xxx.com', 'aaa', 'com')

print(m.span())
# (0, 11)

print(m.span(3))
# (8, 11)

# print(m.span(4))
# IndexError: no such group

# print(m.span(0, 1))
# TypeError: span expected at most 1 arguments, got 2

m = re.match(r'(([a-z]+)@([a-z]+)\.([a-z]+))', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(m.groups())
# ('aaa@xxx.com', 'aaa', 'xxx', 'com')

m = re.match(r'(?P<local>[a-z]+)@(?P<SLD>[a-z]+)\.(?P<TLD>[a-z]+)', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(m.group('local'))
# aaa

print(m.group('SLD'))
# xxx

print(m.group('TLD'))
# com

print(m.group(0))
# aaa@xxx.com

print(m.group(3))
# com

print(m.group(0, 2, 'TLD'))
# ('aaa@xxx.com', 'xxx', 'com')

print(m.groups())
# ('aaa', 'xxx', 'com')

print(m.groupdict())
# {'local': 'aaa', 'SLD': 'xxx', 'TLD': 'com'}

print(type(m.groupdict()))
# <class 'dict'>

print(re.match(r'[a-z]+@[a-z]+\.[a-z]+', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(bool(re.match(r'[a-z]+@[a-z]+\.[a-z]+', s)))
# True

print(re.match('[0-9]+', s))
# None

print(bool(re.match('[0-9]+', s)))
# False

if re.match(r'[a-z]+@[a-z]+\.[a-z]+', s):
    print('match')
else:
    print('no match')
# match

if re.match('[0-9]+', s):
    print('match')
else:
    print('no match')
# no match

m = re.match('[0-9]*', s)
print(m)
# <re.Match object; span=(0, 0), match=''>

print(m.group() == '')
# True

print(bool(m))
# True

if re.match('[0-9]*', s):
    print('match')
else:
    print('no match')
# match
