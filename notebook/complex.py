c = 3 + 4j

print(c)
print(type(c))
# (3+4j)
# <class 'complex'>

# c = 3 + j
# NameError: name 'j' is not defined

c = 3 + 1j

print(c)
# (3+1j)

c = 3j

print(c)
# 3j

c = 3 + 0j

print(c)
# (3+0j)

c = 1.2e3 + 3j

print(c)
# (1200+3j)

c = complex(3, 4)

print(c)
print(type(c))
# (3+4j)
# <class 'complex'>

c = 3 + 4j

print(c.real)
print(type(c.real))
# 3.0
# <class 'float'>

print(c.imag)
print(type(c.imag))
# 4.0
# <class 'float'>

# c.real = 5.5
# AttributeError: readonly attribute

c = 3 + 4j

print(c.conjugate())
# (3-4j)

c = 3 + 4j

print(abs(c))
# 5.0

c = 1 + 1j

print(abs(c))
# 1.4142135623730951

c1 = 3 + 4j
c2 = 2 - 1j

print(c1 + c2)
# (5+3j)

print(c1 - c2)
# (1+5j)

print(c1 * c2)
# (10+5j)

print(c1 / c2)
# (0.4+2.2j)

print(c1 ** 3)
# (-117+44j)

print(c1 + 3)
# (6+4j)

print(c1 * 0.5)
# (1.5+2j)
