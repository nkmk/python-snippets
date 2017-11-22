s = 'one two three'
l = s.split()
print(l)
# ['one', 'two', 'three']

s = 'one:two:three'
l = s.split(':')
print(l)
# ['one', 'two', 'three']

s = 'one, two, three'
l = s.split(',')
print(l)
# ['one', ' two', ' three']

s = '  one  '
print(s.strip())
# one

s = '-+-one-+-'
print(s.strip('-+'))
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

s = 'one, two, , four'
l = [x.strip() for x in s.split(',') if not s == '']
print(l)
print(len(l))
# ['one', 'two', '', 'four']
# 4

s = 'one, two, , four'
l = [x.strip() for x in s.split(',') if not x.strip() == '']
print(l)
print(len(l))
# ['one', 'two', 'four']
# 3

s = '1, 2, 3, 4'
l = [x.strip() for x in s.split(',')]
print(l)
# ['1', '2', '3', '4']

s = '1, 2, 3, 4'
l = [int(x.strip()) for x in s.split(',')]
print(l)
# [1, 2, 3, 4]

s = 'one, two, three'
l = [x.strip() for x in s.split(',')]
print(l)
# ['one', 'two', 'three']

print(','.join(l))
# one,two,three

print(', '.join(l))
# one, two, three

print('::'.join(l))
# one::two::three
