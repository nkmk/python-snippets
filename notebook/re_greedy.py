import re

s = 'aaa@xxx.com, bbb@yyy.com'

m = re.match(r'.+com', s)
print(m)
# <re.Match object; span=(0, 24), match='aaa@xxx.com, bbb@yyy.com'>

print(m.group())
# aaa@xxx.com, bbb@yyy.com

m = re.match(r'.+?com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(m.group())
# aaa@xxx.com
