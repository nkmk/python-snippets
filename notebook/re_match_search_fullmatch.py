import re

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

m = re.match(r'[a-z]+@[a-z]+\.com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

m = re.match(r'[a-z]+@[a-z]+\.net', s)
print(m)
# None

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

m = re.search(r'[a-z]+@[a-z]+\.net', s)
print(m)
# <re.Match object; span=(26, 37), match='ccc@zzz.net'>

m = re.search(r'[a-z]+@[a-z]+\.com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

s = 'aaa@xxx.com'

m = re.fullmatch(r'[a-z]+@[a-z]+\.com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

s = '!!!aaa@xxx.com!!!'

m = re.fullmatch(r'[a-z]+@[a-z]+\.com', s)
print(m)
# None

s = '!!!aaa@xxx.com!!!'

m = re.match(r'[a-z]+@[a-z]+\.com$', s)
print(m)
# None
