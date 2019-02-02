print(0.1)
# 0.1

print(format(0.1, '.20f'))
# 0.10000000000000000555

print(0.1 + 0.1 + 0.1)
# 0.30000000000000004

print(0.1 + 0.1 + 0.1 == 0.3)
# False

print((19 / 155) * (155 / 19))
# 0.9999999999999999

print((19 / 155) * (155 / 19) == 1)
# False

print(round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10))
# True

print(abs((0.1 + 0.1 + 0.1) - 0.3) < 1e-10)
# True

print(1e5)
# 100000.0

print(1e-3)
# 0.001

import math

print(math.isclose(0.1 + 0.1 + 0.1, 0.3))
# True

print(math.isclose((19 / 155) * (155 / 19), 1))
# True

print(math.isclose(1, 1.001))
# False

print(math.isclose(1, 1.001, rel_tol=0.01))
# True

print(math.isclose(0, 0.001))
# False

print(math.isclose(0, 0.001, rel_tol=0.01))
# False

print(math.isclose(0, 0.001, abs_tol=0.01))
# True

print(math.sin(math.pi))
# 1.2246467991473532e-16

print(math.sin(math.pi) == 0)
# False

print(math.isclose(math.sin(math.pi), 0))
# False

print(math.isclose(math.sin(math.pi), 0, abs_tol=1e-10))
# True

print(round(math.sin(math.pi), 10) == 0)
# True

print(abs(math.sin(math.pi)) < 1e-10)
# True
