from fractions import Fraction

print(Fraction(1, 3))
# 1/3

print(Fraction(3))
# 3

print(Fraction(0.25))
# 1/4

print(Fraction(0.33))
# 5944751508129055/18014398509481984

print(Fraction('2/5'))
# 2/5

a = Fraction(1, 3)
print(a)
# 1/3

print(a.numerator)
print(type(a.numerator))
# 1
# <class 'int'>

print(a.denominator)
print(type(a.denominator))
# 3
# <class 'int'>

# a.numerator = 7
# AttributeError: can't set attribute

result = Fraction(1, 6) ** 2 + Fraction(1, 3) / Fraction(1, 2)
print(result)
print(type(result))
# 25/36
# <class 'fractions.Fraction'>

print(Fraction(7, 13) > Fraction(8, 15))
# True

a_f = float(a)
print(a_f)
print(type(a_f))
# 0.3333333333333333
# <class 'float'>

b = a + 0.1
print(b)
print(type(b))
# 0.43333333333333335
# <class 'float'>

a_s = str(a)
print(a_s)
print(type(a_s))
# 1/3
# <class 'str'>

pi = Fraction(3.14159265359)
print(pi)
# 3537118876014453/1125899906842624

print(pi.limit_denominator(10))
print(pi.limit_denominator(100))
print(pi.limit_denominator(1000))
# 22/7
# 311/99
# 355/113

e = Fraction(2.71828182846)
print(e)
# 6121026514870223/2251799813685248

print(e.limit_denominator(10))
print(e.limit_denominator(100))
print(e.limit_denominator(1000))
# 19/7
# 193/71
# 1457/536

a = Fraction(0.565656565656)
print(a)
# 636872674577009/1125899906842624

print(a.limit_denominator())
# 56/99

a = Fraction(0.3333)
print(a)
# 6004199023210345/18014398509481984

print(a.limit_denominator())
print(a.limit_denominator(100))
# 3333/10000
# 1/3
