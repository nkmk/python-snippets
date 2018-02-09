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

s = 'aaa' + str(100) + 'bbb' + str(0.25)
print(s)
# aaa100bbb0.25

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
