from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

print(Decimal(0.05))
# 0.05000000000000000277555756156289135105907917022705078125

print(type(Decimal(0.05)))
# <class 'decimal.Decimal'>

print(Decimal(0.5))
# 0.5

print(Decimal('0.05'))
# 0.05

f = 123.456

print(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# 123

print(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
# 123.5

print(Decimal(str(f)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# 123.46

print('0.4 =>', Decimal(str(0.4)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print('0.5 =>', Decimal(str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print('0.6 =>', Decimal(str(0.6)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# 0.4 => 0
# 0.5 => 1
# 0.6 => 1

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

print('0.05 =>', Decimal(0.05).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.15 =>', Decimal(0.15).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.25 =>', Decimal(0.25).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.35 =>', Decimal(0.35).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.45 =>', Decimal(0.45).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
# 0.05 => 0.1
# 0.15 => 0.1
# 0.25 => 0.2
# 0.35 => 0.3
# 0.45 => 0.5

print('0.05 =>', Decimal(str(0.05)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.15 =>', Decimal(str(0.15)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.25 =>', Decimal(str(0.25)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.35 =>', Decimal(str(0.35)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print('0.45 =>', Decimal(str(0.45)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
# 0.05 => 0.0
# 0.15 => 0.2
# 0.25 => 0.2
# 0.35 => 0.4
# 0.45 => 0.4

print(Decimal(2.675))
# 2.67499999999999982236431605997495353221893310546875

print(Decimal(2.675).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# 2.67

print(Decimal(str(2.675)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# 2.68

print(Decimal(2.675).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))
# 2.67

print(Decimal(str(2.675)).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))
# 2.68

d = Decimal('123.456').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(d)
# 123.46

print(type(d))
# <class 'decimal.Decimal'>

# print(1.2 + d)
# TypeError: unsupported operand type(s) for +: 'float' and 'decimal.Decimal'

print(1.2 + float(d))
# 124.66

i = 99518

print(Decimal(i).quantize(Decimal('10'), rounding=ROUND_HALF_UP))
# 99518

print(Decimal('10').as_tuple())
# DecimalTuple(sign=0, digits=(1, 0), exponent=0)

print(Decimal('1E1').as_tuple())
# DecimalTuple(sign=0, digits=(1,), exponent=1)

print(Decimal(i).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
# 9.952E+4

print(int(Decimal(i).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
# 99520

print(int(Decimal(i).quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)))
# 99500

print(int(Decimal(i).quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)))
# 100000

print('4 =>', int(Decimal(4).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print('5 =>', int(Decimal(5).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print('6 =>', int(Decimal(6).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
# 4 => 0
# 5 => 10
# 6 => 10
