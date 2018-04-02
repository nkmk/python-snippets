import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')

print(type(x))
# <class 'sympy.core.symbol.Symbol'>

expr = x**2 + y + 1

print(expr)
# x**2 + y + 1

z = sympy.Symbol('ZZZZ')

expr_z = z**2 + 3 * z

print(expr_z)
# ZZZZ**2 + 3*ZZZZ

print(expr)
# x**2 + y + 1

print(expr.subs(x, 1))
# y + 2

print(expr.subs(x, y))
# y**2 + y + 1

print(expr.subs([(x, 1), (y, 2)]))
# 4

expr = (x + 1)**2

print(expr)
# (x + 1)**2

expr_ex = sympy.expand(expr)

print(expr_ex)
# x**2 + 2*x + 1

expr_factor = sympy.factor(expr_ex)

print(expr_factor)
# (x + 1)**2

print(sympy.factor(x**3 - x**2 - 3 * x + 3))
# (x - 1)*(x**2 - 3)

print(sympy.factor(x * y + x + y + 1))
# (x + 1)*(y + 1)

print(sympy.solve(x**2 - 3 * x + 2))
# [1, 2]

print(sympy.solve(x**2 + x + 1))
# [-1/2 - sqrt(3)*I/2, -1/2 + sqrt(3)*I/2]

expr = x + y**2 - 4

print(sympy.solve(expr, x))
# [-y**2 + 4]

print(sympy.solve(expr, y))
# [-sqrt(-x + 4), sqrt(-x + 4)]

expr1 = 3 * x + 5 * y - 29
expr2 = x + y - 7

print(sympy.solve([expr1, expr2]))
# {x: 3, y: 4}

print(sympy.diff(x**3 + 2 * x**2 + x))
# 3*x**2 + 4*x + 1

expr = x**3 + y**2 - y

print(sympy.diff(expr, x))
# 3*x**2

print(sympy.diff(expr, y))
# 2*y - 1

print(sympy.integrate(3 * x**2 + 4 * x + 1))
# x**3 + 2*x**2 + x

print(sympy.diff(sympy.cos(x)))
# -sin(x)

print(sympy.diff(sympy.exp(x)))
# exp(x)

print(sympy.diff(sympy.log(x)))
# 1/x

print(sympy.integrate(sympy.cos(x)))
# sin(x)

print(sympy.integrate(sympy.exp(x)))
# exp(x)

print(sympy.integrate(sympy.log(x)))
# x*log(x) - x
