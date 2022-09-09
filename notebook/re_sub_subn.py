import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.sub('[a-z]+@', 'ABC@', s))
# ABC@xxx.com ABC@yyy.net ABC@zzz.org

print(re.sub('[a-z]+@', 'ABC@', s, 2))
# ABC@xxx.com ABC@yyy.net ccc@zzz.org

p = re.compile('[a-z]+@')
print(p.sub('ABC@', s))
# ABC@xxx.com ABC@yyy.net ABC@zzz.org

print(re.sub('[xyz]', '1', s))
# aaa@111.com bbb@111.net ccc@111.org

print(re.sub('com|net|org', 'biz', s))
# aaa@xxx.biz bbb@yyy.biz ccc@zzz.biz

print(re.sub('([a-z]+)@([a-z]+)', '\\2@\\1', s))
# xxx@aaa.com yyy@bbb.net zzz@ccc.org

print(re.sub('([a-z]+)@([a-z]+)', r'\2@\1', s))
# xxx@aaa.com yyy@bbb.net zzz@ccc.org

print(re.sub('(?P<local>[a-z]+)@(?P<SLD>[a-z]+)', r'\g<SLD>@\g<local>', s))
# xxx@aaa.com yyy@bbb.net zzz@ccc.org

def func(matchobj):
    return matchobj.group(2).upper() + '@' + matchobj.group(1)

print(re.sub('([a-z]+)@([a-z]+)', func, s))
# XXX@aaa.com YYY@bbb.net ZZZ@ccc.org

print(re.sub('([a-z]+)@([a-z]+)', lambda m: m.group(2).upper() + '@' + m.group(1), s))
# XXX@aaa.com YYY@bbb.net ZZZ@ccc.org

t = re.subn('[a-z]*@', 'ABC@', s)
print(t)
# ('ABC@xxx.com ABC@yyy.net ABC@zzz.org', 3)

print(type(t))
# <class 'tuple'>

print(t[0])
# ABC@xxx.com ABC@yyy.net ABC@zzz.org

print(t[1])
# 3

print(re.subn('([a-z]+)@([a-z]+)', r'\2@\1', s, 2))
# ('xxx@aaa.com yyy@bbb.net ccc@zzz.org', 2)
