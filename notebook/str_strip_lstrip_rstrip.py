s = ' \n a b c　\t'

print(s)
#  
#  a b c　	

print(repr(s))
# ' \n a b c\u3000\t'

print(s.strip())
# a b c

print(repr(s.strip()))
# 'a b c'

s_strip = s.strip()
print(repr(s_strip))
# 'a b c'

print(repr(s))
# ' \n a b c\u3000\t'

s = s.strip()
print(repr(s))
# 'a b c'

s = 'aabbcc-abc-aabbcc'

print(s.strip('abc'))
# -abc-

print(s.strip('cba'))
# -abc-

print(s.strip('ab'))
# cc-abc-aabbcc

s = ' \n aabbcc-abc-aabbcc　\t'

print(repr(s))
# ' \n aabbcc-abc-aabbcc\u3000\t'

print(repr(s.strip('abc')))
# ' \n aabbcc-abc-aabbcc\u3000\t'

print(repr(s.strip('abc \n　\t')))
# '-abc-'

print(repr(s.strip().strip('abc')))
# '-abc-'

s = ' \n a b c 　\t'

print(repr(s.lstrip()))
# 'a b c \u3000\t'

s = 'aabbcc-abc-aabbcc'

print(s.lstrip('abc'))
# -abc-aabbcc

s = ' \n a b c 　\t'

print(repr(s.rstrip()))
# ' \n a b c'

s = 'aabbcc-abc-aabbcc'

print(s.rstrip('abc'))
# aabbcc-abc-
