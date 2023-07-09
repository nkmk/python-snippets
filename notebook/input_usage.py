val = input()
# abc

print(val)
# abc

print(type(val))
# <class 'str'>

val = input('Enter your name: ')
# Enter your name: Alice

print(val)
# Alice

print(type(val))
# <class 'str'>

val = input('Enter an integer: ')
# Enter an integer: 100

print(val)
# 100

print(type(val))
# <class 'str'>

i = int(input('Enter an integer: '))
# Enter an integer: 100

print(i)
# 100

print(type(i))
# <class 'int'>

# i = int(input('Enter an integer: '))
# Enter an integer: abc
# ValueError: invalid literal for int() with base 10: 'abc'

try:
    i = int(input('Enter an integer: '))
except ValueError:
    i = 0
# Enter an integer: abc

print(i)
# 0

while True:
    try:
        i = int(input('Enter an integer: '))
        break
    except ValueError:
        print('Invalid input!')
# Enter an integer: abc
# Invalid input!
# Enter an integer: 100

print(i)
# 100

l = []

l.append(input('Enter the first value: '))
l.append(input('Enter the second value: '))
l.append(input('Enter the third value: '))
# Enter the first value: x
# Enter the second value: y
# Enter the third value: z

print(l)
# ['x', 'y', 'z']

l = []

print('Enter "over" then finish')
while True:
    val = input('Enter a value: ')
    if val == 'over':
        print('FINISH')
        break
    l.append(val)
# Enter "over" then finish
# Enter a value: x
# Enter a value: y
# Enter a value: z
# Enter a value: over
# FINISH

print(l)
# ['x', 'y', 'z']

l = list(iter(input, 'over'))
# x
# y
# z
# over

print(l)
# ['x', 'y', 'z']

l = list(iter(lambda: input('Enter a value: '), 'over'))
# Enter a value: x
# Enter a value: y
# Enter a value: z
# Enter a value: over

print(l)
# ['x', 'y', 'z']

val = input('Enter values separated by commas: ')
# Enter values separated by commas: x,y,z

print(val)
# x,y,z

l = val.split(',')
print(l)
# ['x', 'y', 'z']

print(type(l))
# <class 'list'>

s = '\n'.join(iter(input, ''))
# Line1
# Line2
# Line3
# 

print(s)
# Line1
# Line2
# Line3

print(type(s))
# <class 'str'>
