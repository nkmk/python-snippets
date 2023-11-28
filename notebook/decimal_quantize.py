from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

print(Decimal(0.05))
# 0.05000000000000000277555756156289135105907917022705078125

print(type(Decimal(0.05)))
# <class 'decimal.Decimal'>

print(Decimal(0.5))
# 0.5

print(Decimal(0.25))
# 0.25

print(Decimal('0.05'))
# 0.05

print(Decimal(str(0.05)))
# 0.05

f = 123.456

print(Decimal(str(f)).quantize(Decimal('0'), ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.1'), ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.01'), ROUND_HALF_UP))
# 123
# 123.5
# 123.46

print('0.4 =>', Decimal(str(0.4)).quantize(Decimal('0'), ROUND_HALF_UP))
print('0.5 =>', Decimal(str(0.5)).quantize(Decimal('0'), ROUND_HALF_UP))
print('0.6 =>', Decimal(str(0.6)).quantize(Decimal('0'), ROUND_HALF_UP))
# 0.4 => 0
# 0.5 => 1
# 0.6 => 1

print('0.05 =>', Decimal(str(0.05)).quantize(Decimal('0.1'), ROUND_HALF_EVEN))
print('0.15 =>', Decimal(str(0.15)).quantize(Decimal('0.1'), ROUND_HALF_EVEN))
print('0.25 =>', Decimal(str(0.25)).quantize(Decimal('0.1'), ROUND_HALF_EVEN))
print('0.35 =>', Decimal(str(0.35)).quantize(Decimal('0.1'), ROUND_HALF_EVEN))
print('0.45 =>', Decimal(str(0.45)).quantize(Decimal('0.1'), ROUND_HALF_EVEN))
# 0.05 => 0.0
# 0.15 => 0.2
# 0.25 => 0.2
# 0.35 => 0.4
# 0.45 => 0.4

d = Decimal('123.456').quantize(Decimal('0.01'), ROUND_HALF_UP)
print(d)
# 123.46

print(type(d))
# <class 'decimal.Decimal'>

f = float(d)
print(f)
# 123.46

print(type(f))
# <class 'float'>

print(Decimal(f))
# 123.4599999999999937472239253111183643341064453125

print(Decimal(str(f)))
# 123.46

i = 99518
print(Decimal(i).quantize(Decimal('10'), ROUND_HALF_UP))
# 99518

print(Decimal('10').as_tuple())
# DecimalTuple(sign=0, digits=(1, 0), exponent=0)

print(Decimal('1E1').as_tuple())
# DecimalTuple(sign=0, digits=(1,), exponent=1)

print(Decimal(i).quantize(Decimal('1E1'), ROUND_HALF_UP))
print(Decimal(i).quantize(Decimal('1E2'), ROUND_HALF_UP))
print(Decimal(i).quantize(Decimal('1E3'), ROUND_HALF_UP))
# 9.952E+4
# 9.95E+4
# 1.00E+5

def remove_exponent(d):
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

d = Decimal(i).quantize(Decimal('1E2'), ROUND_HALF_UP)
print(d)
# 9.95E+4

d_remove = remove_exponent(d)
print(d_remove)
# 99500

print(type(d_remove))
# <class 'decimal.Decimal'>

i = int(d)
print(i)
# 99500

print(type(i))
# <class 'int'>
