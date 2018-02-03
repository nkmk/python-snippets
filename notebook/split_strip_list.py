s = 'one two three'
l = s.split()
print(l)
# ['one', 'two', 'three']

s = 'one two        three'
l = s.split()
print(l)
# ['one', 'two', 'three']

s = 'one\ttwo\tthree'
l = s.split()
print(l)
# ['one', 'two', 'three']

s = 'one::two::three'
l = s.split('::')
print(l)
# ['one', 'two', 'three']

s = 'one,two,three'
l = s.split(',')
print(l)
# ['one', 'two', 'three']

s = 'one, two, three'
l = s.split(',')
print(l)
# ['one', ' two', ' three']

s = 'one, two, three'
l = s.split(', ')
print(l)
# ['one', 'two', 'three']

s = 'one, two,  three'
l = s.split(', ')
print(l)
# ['one', 'two', ' three']

s = '  one  '
print(s.strip())
# one

print(s)
#   one  

s = '-+-one-+-'
print(s.strip('-+'))
# one

s = '-+- one -+-'
print(s.strip('-+'))
#  one 

s = '-+- one -+-'
print(s.strip('-+ '))
# one

s = 'one, two, three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', 'two', 'three']

s = ''
l = [x.strip() for x in s.split(',')]
print(l)
print(len(l))
# ['']
# 1

s = ''
l = [x.strip() for x in s.split(',') if not s == '']
print(l)
print(len(l))
# []
# 0

s = 'one, , three'
l = [x.strip() for x in s.split(',')]
print(l)
print(len(l))
# ['one', '', 'three']
# 3

s = 'one, ,three'
l = [x.strip() for x in s.split(',') if not x.strip() == '']
print(l)
print(len(l))
# ['one', 'three']
# 2

s = '1, 2, 3, 4'
l = [x.strip() for x in s.split(',')]
print(l)
print(type(l[0]))
# ['1', '2', '3', '4']
# <class 'str'>

s = '1, 2, 3, 4'
l = [int(x.strip()) for x in s.split(',')]
print(l)
print(type(l[0]))
# [1, 2, 3, 4]
# <class 'int'>

s = 'one, two,  three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', 'two', 'three']

print(','.join(l))
# one,two,three

print('::'.join(l))
# one::two::three

s = 'one, two,  three'
s_new = '-'.join([x.strip() for x in s.split(',')])
print(s_new)
# one-two-three

s = 'one,two,three'
s_new = s.replace(',', '+')
print(s_new)
# one+two+three
