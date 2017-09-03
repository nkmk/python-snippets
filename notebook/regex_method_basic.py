# https://docs.python.jp/3/howto/regex.html
# https://docs.python.jp/3/library/re.html

import re

s = 'one two one two'

m = re.match('one', s)
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='one'>

print(m.group())
print(m.start())
print(m.end())
print(m.span())
# one
# 0
# 3
# (0, 3)

m = re.match('one two', s)
print(m)
print(m.group())
# <_sre.SRE_Match object; span=(0, 7), match='one two'>
# one two

m = re.match('(one) (two)', s)
print(m)
print(m.group())
print(m.groups())
# <_sre.SRE_Match object; span=(0, 7), match='one two'>
# one two
# ('one', 'two')

m = re.match('two', s)
print(m)
# None

m = re.search('one', s)
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='one'>

m = re.search('two', s)
print(m)
# <_sre.SRE_Match object; span=(4, 7), match='two'>

m = re.findall('one', s)
print(m)
# ['one', 'one']

m = re.findall('one two', s)
print(m)
# ['one two', 'one two']

m = re.findall('(one) (two)', s)
print(m)
# [('one', 'two'), ('one', 'two')]

m = re.finditer('one', s)
print(m)
# <callable_iterator object at 0x10d4d5a90>

for match in m:
    print(match)
# <_sre.SRE_Match object; span=(0, 3), match='one'>
# <_sre.SRE_Match object; span=(8, 11), match='one'>

m = re.sub('one', 'ONE', s)
print(m)
# ONE two ONE two

m = re.sub('one two', 'xxx', s)
print(m)
# xxx xxx

m = re.sub('(one) (two)', '\\1X\\2', s)
print(m)
# oneXtwo oneXtwo

m = re.sub('(one) (two)', r'\1X\2', s)
print(m)
# oneXtwo oneXtwo

m = re.subn('one', 'ONE', s)
print(m)
# ('ONE two ONE two', 2)

m = re.split(' ', s)
print(m)
# ['one', 'two', 'one', 'two']

p = re.compile('one')

m = p.match(s)
print(m)
# <_sre.SRE_Match object; span=(0, 3), match='one'>
