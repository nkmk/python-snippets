import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.match(r'([a-z]+)@([a-z]+)\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(re.sub(r'([a-z]+)@([a-z]+)\.com', 'NEW_ADDRESS', s))
# NEW_ADDRESS bbb@yyy.net ccc@zzz.org

p = re.compile(r'([a-z]+)@([a-z]+)\.com')

print(p)
# re.compile('([a-z]+)@([a-z]+)\\.com')

print(type(p))
# <class 're.Pattern'>

print(p.match(s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(p.sub('NEW_ADDRESS', s))
# NEW_ADDRESS bbb@yyy.net ccc@zzz.org
