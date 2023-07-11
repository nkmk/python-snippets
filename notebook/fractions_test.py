from fractions import Fraction

print(Fraction(1, 3))
# 1/3

print(Fraction(2, 6))
# 1/3

print(Fraction(3))
# 3

print(Fraction(0.25))
# 1/4

print(Fraction(0.3333333333333333))
# 6004799503160661/18014398509481984

print(Fraction(0.3333333333333333).limit_denominator())
# 1/3

print(Fraction('2/5'))
# 2/5

print(Fraction('16/48'))
# 1/3

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
# AttributeError: property 'numerator' of 'Fraction' object has no setter

print(Fraction(1, 2) + Fraction(1, 3))
# 5/6

print(Fraction(1, 2) / Fraction(1, 3))
# 3/2

print(Fraction(1, 6) ** 2 + Fraction(1, 2) * Fraction(1, 3))
# 7/36

print(Fraction(7, 13) > Fraction(8, 15))
# True

print(float(Fraction(1, 5)))
# 0.2

print(Fraction(1, 5) * 0.5)
# 0.1

print(str(Fraction(1, 3)))
# 1/3

print(type(str(Fraction(1, 3))))
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

a = Fraction(0.3333333333333333)
print(a)
# 6004799503160661/18014398509481984

print(a.limit_denominator())
# 1/3

a = Fraction(0.14285714285714285)
print(a)
# 2573485501354569/18014398509481984

print(a.limit_denominator())
# 1/7
