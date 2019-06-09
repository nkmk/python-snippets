import re

p = re.compile('[a-z]+')
print(p.fullmatch('abc'))
# <re.Match object; span=(0, 3), match='abc'>

print(p.fullmatch('abc123'))
# None

s = 'abc'

if p.fullmatch(s):
    print('match')
else:
    print('no match')
# match

s = 'abc123'

if p.fullmatch(s):
    print('match')
else:
    print('no match')
# no match

p = re.compile('[a-z]+$')
print(p.match('abc'))
# <re.Match object; span=(0, 3), match='abc'>

print(p.match('abc123'))
# None

p = re.compile('[a-z]+')
print(p.search('123abcABC'))
# <re.Match object; span=(3, 6), match='abc'>

print(p.search('123ABC'))
# None

p = re.compile('[a-z]+')
result = p.findall('123abcABCxyz')
print(result)
# ['abc', 'xyz']

print(type(result))
# <class 'list'>

print(type(result[0]))
# <class 'str'>

print(p.findall('123ABC'))
# []

s_result = ''.join(p.findall('123abcABCxyz'))
print(s_result)
# abcxyz

print(len(s_result))
# 6

print(len('🇯🇵'))
# 2
