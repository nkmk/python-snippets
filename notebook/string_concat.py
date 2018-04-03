s = 'aaa' + 'bbb' + 'ccc'
print(s)
# aaabbbccc

s1 = 'aaa'
s2 = 'bbb'
s3 = 'ccc'

s = s1 + s2 + s3
print(s)
# aaabbbccc

s = s1 + s2 + s3 + 'ddd'
print(s)
# aaabbbcccddd

s1 += s2
print(s1)
# aaabbb

s = 'aaa'

s += 'xxx'
print(s)
# aaaxxx

s = 'aaa''bbb''ccc'
print(s)
# aaabbbccc

s = 'aaa'  'bbb'    'ccc'
print(s)
# aaabbbccc

s = 'aaa'\
    'bbb'\
    'ccc'
print(s)
# aaabbbccc

# s = s1 s2 s3
# SyntaxError: invalid syntax

s1 = 'aaa'
s2 = 'bbb'

i = 100
f = 0.25

# s = s1 + i
# TypeError: must be str, not int

s = s1 + '_' + str(i) + '_' + s2 + '_' + str(f)
print(s)
# aaa_100_bbb_0.25

s = s1 + '_' + format(i, '05') + '_' + s2 + '_' + format(f, '.5f')
print(s)
# aaa_00100_bbb_0.25000

s = '{}_{:05}_{}_{:.5f}'.format(s1, i, s2, f)
print(s)
# aaa_00100_bbb_0.25000

l = ['aaa', 'bbb', 'ccc']

s = ''.join(l)
print(s)
# aaabbbccc

s = ','.join(l)
print(s)
# aaa,bbb,ccc

s = '-'.join(l)
print(s)
# aaa-bbb-ccc

s = '\n'.join(l)
print(s)
# aaa
# bbb
# ccc

l = [2017, 12, 31]

s = '-'.join([str(n) for n in l])
print(s)
# 2017-12-31
