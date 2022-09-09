import re

s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

m = re.match(r'([a-z]+)@([a-z]+)\.com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

result = re.sub(r'([a-z]+)@([a-z]+)\.com', 'new-address', s)
print(result)
# new-address, new-address, ccc@zzz.net

p = re.compile(r'([a-z]+)@([a-z]+)\.com')

print(p)
# re.compile('([a-z]+)@([a-z]+)\\.com')

print(type(p))
# <class 're.Pattern'>

m = p.match(s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

result = p.sub('new-address', s)
print(result)
# new-address, new-address, ccc@zzz.net
