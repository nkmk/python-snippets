import re

m = re.match(r'\w+', 'あいう漢字ＡＢＣ１２３')
print(m)
# <re.Match object; span=(0, 11), match='あいう漢字ＡＢＣ１２３'>

m = re.match('[a-zA-Z0-9_]+', 'あいう漢字ＡＢＣ１２３')
print(m)
# None

m = re.match(r'\w+', 'あいう漢字ＡＢＣ１２３', flags=re.ASCII)
print(m)
# None

m = re.match(r'(?a)\w+', 'あいう漢字ＡＢＣ１２３')
print(m)
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

m = re.match(r'\W+', 'あいう漢字ＡＢＣ１２３')
print(m)
# None

m = re.match(r'\W+', 'あいう漢字ＡＢＣ１２３', flags=re.ASCII)
print(m)
# <re.Match object; span=(0, 11), match='あいう漢字ＡＢＣ１２３'>

m = re.match(r'\d+', '123')
print(m)
# <re.Match object; span=(0, 3), match='123'>

m = re.match(r'\d+', '１２３')
print(m)
# <re.Match object; span=(0, 3), match='１２３'>

m = re.match(r'\d+', '123', flags=re.ASCII)
print(m)
# <re.Match object; span=(0, 3), match='123'>

m = re.match(r'\d+', '１２３', flags=re.ASCII)
print(m)
# None

m = re.match(r'\s+', '　')  # 全角スペース
print(m)
# <re.Match object; span=(0, 1), match='\u3000'>

m = re.match(r'\s+', '　', flags=re.ASCII)
print(m)
# None

m = re.match('[a-zA-Z]+', 'abcABC')
print(m)
# <re.Match object; span=(0, 6), match='abcABC'>

m = re.match('[a-z]+', 'abcABC', flags=re.IGNORECASE)
print(m)
# <re.Match object; span=(0, 6), match='abcABC'>

m = re.match('[A-Z]+', 'abcABC', flags=re.IGNORECASE)
print(m)
# <re.Match object; span=(0, 6), match='abcABC'>

s = '''aaa-xxx
bbb-yyy
ccc-zzz'''

print(s)
# aaa-xxx
# bbb-yyy
# ccc-zzz

result = re.findall('[a-z]+', s)
print(result)
# ['aaa', 'xxx', 'bbb', 'yyy', 'ccc', 'zzz']

result = re.findall('^[a-z]+', s)
print(result)
# ['aaa']

result = re.findall('^[a-z]+', s, flags=re.MULTILINE)
print(result)
# ['aaa', 'bbb', 'ccc']

result = re.findall('[a-z]+$', s)
print(result)
# ['zzz']

result = re.findall('[a-z]+$', s, flags=re.MULTILINE)
print(result)
# ['xxx', 'yyy', 'zzz']

s = '''aaa-xxx
あああ-んんん
bbb-zzz'''

print(s)
# aaa-xxx
# あああ-んんん
# bbb-zzz

result = re.findall(r'^\w+', s, flags=re.M)
print(result)
# ['aaa', 'あああ', 'bbb']

result = re.findall(r'^\w+', s, flags=re.M | re.A)
print(result)
# ['aaa', 'bbb']

result = re.findall(r'(?am)^\w+', s)
print(result)
# ['aaa', 'bbb']
