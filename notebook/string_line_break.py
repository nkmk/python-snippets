s = 'Line1\nLine2\nLine3'
print(s)
# Line1
# Line2
# Line3

s = 'Line1\r\nLine2\r\nLine3'
print(s)
# Line1
# Line2
# Line3

s = '''Line1
Line2
Line3'''
print(s)
# Line1
# Line2
# Line3

s = '''
    Line1
    Line2
    Line3
    '''
print(s)
# 
#     Line1
#     Line2
#     Line3
#     

s = 'Line1\n'\
    'Line2\n'\
    'Line3'
print(s)
# Line1
# Line2
# Line3

s = 'Line1\n'\
    '    Line2\n'\
    '        Line3'
print(s)
# Line1
#     Line2
#         Line3

s = ('Line1\n'
     'Line2\n'
     'Line3')
print(s)
# Line1
# Line2
# Line3

s = ('Line1\n'
     '    Line2\n'
     '        Line3')
print(s)
# Line1
#     Line2
#         Line3

s = '''\
Line1
Line2
Line3'''
print(s)
# Line1
# Line2
# Line3

s = '''\
Line1
    Line2
        Line3'''
print(s)
# Line1
#     Line2
#         Line3

l = ['Line1', 'Line2', 'Line3']

s_n = '\n'.join(l)
print(s_n)
# Line1
# Line2
# Line3

print(repr(s_n))
# 'Line1\nLine2\nLine3'

s_rn = '\r\n'.join(l)
print(s_rn)
# Line1
# Line2
# Line3

print(repr(s_rn))
# 'Line1\r\nLine2\r\nLine3'

s = 'Line1\nLine2\r\nLine3'
print(s.splitlines())
# ['Line1', 'Line2', 'Line3']

s = 'Line1\nLine2\r\nLine3'

print(''.join(s.splitlines()))
# Line1Line2Line3

print(' '.join(s.splitlines()))
# Line1 Line2 Line3

print(','.join(s.splitlines()))
# Line1,Line2,Line3

s_n = '\n'.join(s.splitlines())
print(s_n)
# Line1
# Line2
# Line3

print(repr(s_n))
# 'Line1\nLine2\nLine3'

s = 'Line1\nLine2\nLine3'

print(s.replace('\n', ''))
# Line1Line2Line3

print(s.replace('\n', ','))
# Line1,Line2,Line3

s = 'Line1\nLine2\r\nLine3'

s_error = s.replace('\n', ',')
print(s_error)
# ,Line3Line2

print(repr(s_error))
# 'Line1,Line2\r,Line3'

s_error = s.replace('\r\n', ',')
print(s_error)
# Line1
# Line2,Line3

print(repr(s_error))
# 'Line1\nLine2,Line3'

s = 'Line1\nLine2\r\nLine3'

print(s.replace('\r\n', ',').replace('\n', ','))
# Line1,Line2,Line3

s_error = s.replace('\n', ',').replace('\r\n', ',')
print(s_error)
# ,Line3Line2

print(repr(s_error))
# 'Line1,Line2\r,Line3'

print(','.join(s.splitlines()))
# Line1,Line2,Line3

s = 'aaa\n'
print(s + 'bbb')
# aaa
# bbb

print(s.rstrip() + 'bbb')
# aaabbb

print('a')
print('b')
print('c')
# a
# b
# c

print('a', end='')
print('b', end='')
print('c', end='')
# abc

print('a', end='-')
print('b', end='-')
print('c')
# a-b-c
