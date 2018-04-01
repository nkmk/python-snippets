import math

print(math.pi)
# 3.141592653589793

print(math.degrees(math.pi))
# 180.0

print(math.radians(180))
# 3.141592653589793

sin30 = math.sin(math.radians(30))
print(sin30)
# 0.49999999999999994

sin30_round = round(sin30, 3)
print(sin30_round)
# 0.5

print('{:.3}'.format(sin30))
# 0.5

print(format(sin30, '.3'))
# 0.5

asin05 = math.degrees(math.asin(0.5))
print(asin05)
# 29.999999999999996

asin05_round = round(asin05, 3)
print(asin05_round)
# 30.0

cos60 = math.cos(math.radians(60))
print(cos60)
# 0.5000000000000001

acos05 = math.degrees(math.acos(0.5))
print(acos05)
# 59.99999999999999

tan45 = math.tan(math.radians(45))
print(tan45)
# 0.9999999999999999

atan1 = math.degrees(math.atan(1))
print(atan1)
# 45.0

print(math.degrees(math.atan(1)))
# 45.0

print(math.degrees(math.atan(-1)))
# -45.0

print(math.degrees(math.atan(math.inf)))
# 90.0

print(math.degrees(math.atan(-math.inf)))
# -90.0

print(math.degrees(math.atan2(1, 1)))
# 45.0

print(math.degrees(math.atan2(1, -1)))
# 135.0

print(math.degrees(math.atan2(-1, -1)))
# -135.0

print(math.degrees(math.atan2(-1, 1)))
# -45.0

print(math.degrees(math.atan2(0, -math.inf)))
# 180.0
