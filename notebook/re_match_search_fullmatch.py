import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.match(r'[a-z]+@[a-z]+\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(re.match(r'[a-z]+@[a-z]+\.net', s))
# None

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.search(r'[a-z]+@[a-z]+\.net', s))
# <re.Match object; span=(12, 23), match='bbb@yyy.net'>

print(re.search(r'[a-z]+@[a-z]+\.[a-z]+', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

s = 'aaa@xxx.com'
print(re.fullmatch(r'[a-z]+@[a-z]+\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

s = '!!!aaa@xxx.com!!!'
print(re.fullmatch(r'[a-z]+@[a-z]+\.com', s))
# None

s = '!!!aaa@xxx.com!!!'
print(re.match(r'[a-z]+@[a-z]+\.com$', s))
# None
