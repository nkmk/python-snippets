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

val = input('Enter number: ')
# Enter number: 100

print(val)
# 100

print(type(val))
# <class 'str'>

i = int(val)

print(i)
# 100

print(type(i))
# <class 'int'>

f = float(val)

print(f)
# 100.0

print(type(f))
# <class 'float'>

val = input('Enter number: ')
# Enter number: abc

print(val)
# abc

# i = int(val)
# ValueError: invalid literal for int() with base 10: 'abc'

try:
    i = int(val)
except ValueError:
    i = 0

print(i)
# 0

val_1 = input('Enter 1st value: ')
val_2 = input('Enter 2nd value: ')
val_3 = input('Enter 3rd value: ')
# Enter 1st value: x
# Enter 2nd value: y
# Enter 3rd value: z

print(val_1)
# x

print(val_2)
# y

print(val_3)
# z

l = []

print('Enter "over" then finish')
while True:
    val = input('Enter value: ')
    if val == 'over':
        print('FINISH')
        break
    l.append(val)
# Enter "over" then finish
# Enter value: x
# Enter value: y
# Enter value: z
# Enter value: over
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

l = list(iter(lambda: input('Enter value: '), 'over'))
# Enter value: x
# Enter value: y
# Enter value: z
# Enter value: over

print(l)
# ['x', 'y', 'z']

s = '\n'.join(iter(input, ''))
# line1
# line2
# line3
# 

print(s)
# line1
# line2
# line3

print(type(s))
# <class 'str'>

val = input('Enter values separated by comma: ')
# Enter values separated by comma: x,y,z

print(val)
# x,y,z

l = val.split(',')

print(l)
# ['x', 'y', 'z']

print(type(l))
# <class 'list'>
