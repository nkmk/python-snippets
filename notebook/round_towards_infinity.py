import math

def round_towards_infinity(x):
    return int(math.copysign(math.ceil(abs(x)), x))

print(round_towards_infinity(10.123))
# 11

print(round_towards_infinity(-10.123))
# -11

print(math.floor(10.123))
# 10

print(math.floor(-10.123))
# -11

print(math.ceil(10.123))
# 11

print(math.ceil(-10.123))
# -10

print(int(10.123))
# 10

print(int(-10.123))
# -10
