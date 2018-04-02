import sympy
from sympy import sin, exp

x = sympy.Symbol('x')

print(sympy.diff(sin(x)))
# cos(x)

print(sympy.diff(exp(x)))
# exp(x)
