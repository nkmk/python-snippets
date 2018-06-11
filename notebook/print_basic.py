# print 'this is a pen'
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('this is a pen')?

print('this is a pen')
# this is a pen

print(100)
# 100

print([0, 1, 2])
# [0, 1, 2]

print({'a': 0, 'b': 1, 'c': 2})
# {'a': 0, 'b': 1, 'c': 2}

print('1.00000')
# 1.00000

print(1.00000)
# 1.0

s = 'this is a pen'
print(s)
# this is a pen

l = [0, 1, 2]
print(l)
# [0, 1, 2]

print(l[0])
# 0

d = {'a': 0, 'b': 1, 'c': 2}
print(d)
# {'a': 0, 'b': 1, 'c': 2}

print(d['b'])
# 1

f = 1.00000
print(f)
# 1.0

i = 100
print('apple', i, 0.123)
# apple 100 0.123

print('apple', i, 0.123, sep='----')
# apple----100----0.123

print('apple', i, 0.123, sep='\n')
# apple
# 100
# 0.123

s = 'Alice'
i = 25

print('Alice is %d years old' % i)
# Alice is 25 years old

print('%s is %d years old' % (s, i))
# Alice is 25 years old

print('Alice is {} years old'.format(i))
# Alice is 25 years old

print('{} is {} years old'.format(s, i))
# Alice is 25 years old

print('{0} is {1} years old / {0}{0}{0}'.format(s, i))
# Alice is 25 years old / AliceAliceAlice

print('{name} is {age} years old'.format(name=s, age=i))
# Alice is 25 years old

print('{} is {} years old / {{xxx}}'.format(s, i))
# Alice is 25 years old / {xxx}

s = 'Alice'
i = 25

print(f'{s} is {i} years old')
# Alice is 25 years old

number = 0.45
print('{0:.4f} is {0:.2%}'.format(number))
# 0.4500 is 45.00%

print(f'{number:.4f} is {number:.2%}')
# 0.4500 is 45.00%

i = 255

print('left   : {:<8}'.format(i))
print('center : {:^8}'.format(i))
print('right  : {:>8}'.format(i))
print('zero   : {:08}'.format(i))
print('bin    : {:b}'.format(i))
print('oct    : {:o}'.format(i))
print('hex    : {:x}'.format(i))
# left   : 255     
# center :   255   
# right  :      255
# zero   : 00000255
# bin    : 11111111
# oct    : 377
# hex    : ff

f = 0.1234

print('digit   : {:.2}'.format(f))
print('digit   : {:.6f}'.format(f))
print('exp     : {:.4e}'.format(f))
print('percent : {:.0%}'.format(f))
# digit   : 0.12
# digit   : 0.123400
# exp     : 1.2340e-01
# percent : 12%
