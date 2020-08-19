s = 'one two one two one'

print(s.replace(' ', '-'))
# one-two-one-two-one

print(s.replace(' ', ''))
# onetwoonetwoone

print(s.replace('one', 'XXX'))
# XXX two XXX two XXX

print(s.replace('one', 'XXX', 2))
# XXX two XXX two one

print(s.replace('one', 'XXX').replace('two', 'YYY'))
# XXX YYY XXX YYY XXX

print(s.replace('one', 'XtwoX').replace('two', 'YYY'))
# XYYYX YYY XYYYX YYY XYYYX

print(s.replace('two', 'YYY').replace('one', 'XtwoX'))
# XtwoX YYY XtwoX YYY XtwoX

s_lines = 'one\ntwo\nthree'
print(s_lines)
# one
# two
# three

print(s_lines.replace('\n', '-'))
# one-two-three

s_lines_multi = 'one\ntwo\r\nthree'
print(s_lines_multi)
# one
# two
# three

print(repr(s_lines_multi))
# 'one\ntwo\r\nthree'

print(s_lines_multi.replace('\r\n', '-').replace('\n', '-'))
# one-two-three

print(repr(s_lines_multi.replace('\r\n', '-').replace('\n', '-')))
# 'one-two-three'

print(s_lines_multi.replace('\n', '-').replace('\r\n', '-'))
# -threeo

print(repr(s_lines_multi.replace('\n', '-').replace('\r\n', '-')))
# 'one-two\r-three'

print(s_lines_multi.splitlines())
# ['one', 'two', 'three']

print('-'.join(s_lines_multi.splitlines()))
# one-two-three

s = 'one two one two one'

print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
# One TwO One TwO One

print(s.translate(str.maketrans({'o': 'XXX', 't': None})))
# XXXne wXXX XXXne wXXX XXXne

print(s.translate(str.maketrans('ow', 'XY', 'n')))
# Xe tYX Xe tYX Xe

# print(s.translate(str.maketrans('ow', 'XXY', 'n')))
# ValueError: the first two maketrans arguments must have equal length

s = 'abcdefghij'

print(s[:4] + 'XXX' + s[7:])
# abcdXXXhij

s_replace = 'XXX'
i = 4

print(s[:i] + s_replace + s[i + len(s_replace):])
# abcdXXXhij

print(s[:4] + '-' + s[7:])
# abcd-hij

print(s[:4] + '+++++' + s[4:])
# abcd+++++efghij
