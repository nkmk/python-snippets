import cmath
import math

c = 1 + 1j

print(math.atan2(c.imag, c.real))
# 0.7853981633974483

print(cmath.phase(c))
# 0.7853981633974483

print(cmath.phase(c) == math.atan2(c.imag, c.real))
# True

print(math.degrees(cmath.phase(c)))
# 45.0

c = 1 + 1j

print(cmath.polar(c))
print(type(cmath.polar(c)))
# (1.4142135623730951, 0.7853981633974483)
# <class 'tuple'>

print(cmath.polar(c)[0] == abs(c))
# True

print(cmath.polar(c)[1] == cmath.phase(c))
# True

print(cmath.rect(1, 1))
# (0.5403023058681398+0.8414709848078965j)

print(cmath.rect(1, 0))
# (1+0j)

print(cmath.rect(cmath.polar(c)[0], cmath.polar(c)[1]))
# (1.0000000000000002+1j)

r = 2
ph = math.pi

print(cmath.rect(r, ph).real == r * math.cos(ph))
# True

print(cmath.rect(r, ph).imag == r * math.sin(ph))
# True

print((-3 + 4j) ** 0.5)
# (1.0000000000000002+2j)

print((-1) ** 0.5)
# (6.123233995736766e-17+1j)

print(cmath.sqrt(-3 + 4j))
# (1+2j)

print(cmath.sqrt(-1))
# 1j
