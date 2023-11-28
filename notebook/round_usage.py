f = 123.456

print(round(f))
# 123

print(type(round(f)))
# <class 'int'>

print(round(f, 1))
# 123.5

print(round(f, 2))
# 123.46

print(round(f, -1))
# 120.0

print(round(f, -2))
# 100.0

print(round(f, 0))
# 123.0

print(type(round(f, 0)))
# <class 'float'>

i = 99518

print(round(i))
# 99518

print(round(i, 2))
# 99518

print(round(i, -1))
# 99520

print(round(i, -2))
# 99500

print(round(i, -3))
# 100000

print('0.5 =>', round(0.5))
print('1.5 =>', round(1.5))
print('2.5 =>', round(2.5))
print('3.5 =>', round(3.5))
print('4.5 =>', round(4.5))
# 0.5 => 0
# 1.5 => 2
# 2.5 => 2
# 3.5 => 4
# 4.5 => 4

print(' 5 =>', round(5, -1))
print('15 =>', round(15, -1))
print('25 =>', round(25, -1))
print('35 =>', round(35, -1))
print('45 =>', round(45, -1))
#  5 => 0
# 15 => 20
# 25 => 20
# 35 => 40
# 45 => 40

print('2.49 =>', round(0.49))
print('2.50 =>', round(0.5))
print('2.51 =>', round(0.51))
# 2.49 => 0
# 2.50 => 0
# 2.51 => 1

print('0.05 =>', round(0.05, 1))
print('0.15 =>', round(0.15, 1))
print('0.25 =>', round(0.25, 1))
print('0.35 =>', round(0.35, 1))
print('0.45 =>', round(0.45, 1))
# 0.05 => 0.1
# 0.15 => 0.1
# 0.25 => 0.2
# 0.35 => 0.3
# 0.45 => 0.5

print(f'{0.15:.20}')
# 0.14999999999999999445
