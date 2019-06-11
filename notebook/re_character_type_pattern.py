import re

p = re.compile('[0123456789]+')
print(p.fullmatch('123'))
# <re.Match object; span=(0, 3), match='123'>

p = re.compile('[^0123456789]+')
print(p.fullmatch('123'))
# None

print(p.fullmatch('abc'))
# <re.Match object; span=(0, 3), match='abc'>

p = re.compile('[0-9]+')
print(p.fullmatch('123'))
# <re.Match object; span=(0, 3), match='123'>

# p = re.compile('[9-0]+')
# error: bad character range 9-0 at position 1

p = re.compile('[\u3041-\u309F]+')
print(p.fullmatch('あいうえおぁぃぅぇぉわをん'))
# <re.Match object; span=(0, 13), match='あいうえおぁぃぅぇぉわをん'>

p = re.compile('[ぁ-ゟ]+')
print(p.fullmatch('あいうえおぁぃぅぇぉわをん'))
# <re.Match object; span=(0, 13), match='あいうえおぁぃぅぇぉわをん'>

print('[\u3041-\u309F]+')
# [ぁ-ゟ]+

print(r'[\u3041-\u309F]+')
# [\u3041-\u309F]+

print(r'[{}-{}]+'.format('\u3041', '\u309F'))
# [ぁ-ゟ]+

p = re.compile('[a-zA-Z]+')
print(p.fullmatch('abcABC'))
# <re.Match object; span=(0, 6), match='abcABC'>

p = re.compile('[a-zA-Z\-[\]]+')
print(p.fullmatch('abc-[ABC]'))
# <re.Match object; span=(0, 9), match='abc-[ABC]'>
