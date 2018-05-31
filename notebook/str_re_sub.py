import re

s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

print(re.sub('[a-z]*@', 'ABC@', s))
# ABC@xxx.com ABC@yyy.com ABC@zzz.com

print(re.sub('[a-z]*@', 'ABC@', s, 2))
# ABC@xxx.com ABC@yyy.com ccc@zzz.com

print(re.sub('[xyz]', '1', s))
# aaa@111.com bbb@111.com ccc@111.com

print(re.sub('aaa|bbb|ccc', 'ABC', s))
# ABC@xxx.com ABC@yyy.com ABC@zzz.com

print(re.sub('([a-z]*)@', '\\1-123@', s))
# aaa-123@xxx.com bbb-123@yyy.com ccc-123@zzz.com

print(re.sub('([a-z]*)@', r'\1-123@', s))
# aaa-123@xxx.com bbb-123@yyy.com ccc-123@zzz.com

t = re.subn('[a-z]*@', 'ABC@', s)
print(t)
# ('ABC@xxx.com ABC@yyy.com ABC@zzz.com', 3)

print(type(t))
# <class 'tuple'>

print(t[0])
# ABC@xxx.com ABC@yyy.com ABC@zzz.com

print(t[1])
# 3
