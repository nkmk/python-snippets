import re

print(re.match(r'\w+', 'あいう漢字ＡＢＣ１２３'))
# <re.Match object; span=(0, 11), match='あいう漢字ＡＢＣ１２３'>

print(re.match('[a-zA-Z0-9_]+', 'あいう漢字ＡＢＣ１２３'))
# None

print(re.match(r'\w+', 'あいう漢字ＡＢＣ１２３', flags=re.ASCII))
# None

print(re.match(r'(?a)\w+', 'あいう漢字ＡＢＣ１２３'))
# None

p = re.compile(r'\w+', flags=re.ASCII)
print(p)
# re.compile('\\w+', re.ASCII)

print(p.match('あいう漢字ＡＢＣ１２３'))
# None

p = re.compile(r'(?a)\w+')
print(p)
# re.compile('(?a)\\w+', re.ASCII)

print(p.match('あいう漢字ＡＢＣ１２３'))
# None

print(re.ASCII is re.A)
# True

print(re.match(r'\W+', 'あいう漢字ＡＢＣ１２３'))
# None

print(re.match(r'\W+', 'あいう漢字ＡＢＣ１２３', flags=re.ASCII))
# <re.Match object; span=(0, 11), match='あいう漢字ＡＢＣ１２３'>

print(re.match(r'\d+', '123'))
# <re.Match object; span=(0, 3), match='123'>

print(re.match(r'\d+', '１２３'))
# <re.Match object; span=(0, 3), match='１２３'>

print(re.match(r'\d+', '123', flags=re.ASCII))
# <re.Match object; span=(0, 3), match='123'>

print(re.match(r'\d+', '１２３', flags=re.ASCII))
# None

print(re.match(r'\s+', '　'))  # 全角スペース
# <re.Match object; span=(0, 1), match='\u3000'>

print(re.match(r'\s+', '　', flags=re.ASCII))
# None

print(re.match('[a-zA-Z]+', 'abcABC'))
# <re.Match object; span=(0, 6), match='abcABC'>

print(re.match('[a-z]+', 'abcABC', flags=re.IGNORECASE))
# <re.Match object; span=(0, 6), match='abcABC'>

print(re.match('[A-Z]+', 'abcABC', flags=re.IGNORECASE))
# <re.Match object; span=(0, 6), match='abcABC'>

s = '''aaa-xxx
bbb-yyy
ccc-zzz'''

print(s)
# aaa-xxx
# bbb-yyy
# ccc-zzz

print(re.findall('^[a-z]+', s))
# ['aaa']

print(re.findall('^[a-z]+', s, flags=re.MULTILINE))
# ['aaa', 'bbb', 'ccc']

print(re.findall('[a-z]+$', s))
# ['zzz']

print(re.findall('[a-z]+$', s, flags=re.MULTILINE))
# ['xxx', 'yyy', 'zzz']

s = '''aaa-xxx
あああ-んんん
bbb-zzz'''

print(s)
# aaa-xxx
# あああ-んんん
# bbb-zzz

print(re.findall(r'^\w+', s, flags=re.M))
# ['aaa', 'あああ', 'bbb']

print(re.findall(r'^\w+', s, flags=re.M | re.A))
# ['aaa', 'bbb']

print(re.findall(r'(?am)^\w+', s))
# ['aaa', 'bbb']
