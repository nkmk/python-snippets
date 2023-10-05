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

s = 'one, two,  three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', 'two', 'three']

s = ''
l = [x.strip() for x in s.split(',')]
print(l)
# ['']

s = ''
l = [x.strip() for x in s.split(',') if not s == '']
print(l)
# []

s = 'one, ,  three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', '', 'three']

s = 'one, ,  three'
l = [x.strip() for x in s.split(',') if not x.strip() == '']
print(l)
# ['one', 'three']

s = '1, 2,  3,   4'
l = [x.strip() for x in s.split(',')]
print(l)
print(type(l[0]))
# ['1', '2', '3', '4']
# <class 'str'>

s = '1, 2,  3,   4'
l = [int(x) for x in s.split(',')]
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
