from decimal import Decimal, ROUND_HALF_UP

f = 123.456

print(Decimal(f).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# 123

print(Decimal(f).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
# 123.5

print(Decimal(f).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# 123.46

print(Decimal(0.4).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print(Decimal(0.5).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print(Decimal(0.6).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# 0
# 1
# 1

d = Decimal(f).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(type(d))
# <class 'decimal.Decimal'>

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

print(int(Decimal(4).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print(int(Decimal(5).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print(int(Decimal(6).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
# 0
# 10
# 10
