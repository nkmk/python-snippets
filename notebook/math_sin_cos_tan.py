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

print(round(sin30, 1))
# 0.5

print(math.isclose(sin30, 0.5))
# True

asin05 = math.degrees(math.asin(0.5))
print(asin05)
# 29.999999999999996

print(round(asin05, 1))
# 30.0

print(math.cos(math.radians(60)))
# 0.5000000000000001

print(math.degrees(math.acos(0.5)))
# 59.99999999999999

print(math.tan(math.radians(45)))
# 0.9999999999999999

print(math.degrees(math.atan(1)))
# 45.0

print(math.degrees(math.atan(0)))
# 0.0

print(math.degrees(math.atan(1)))
# 45.0

print(math.degrees(math.atan(-1)))
# -45.0

print(math.degrees(math.atan(math.inf)))
# 90.0

print(math.degrees(math.atan(-math.inf)))
# -90.0

print(math.degrees(math.atan2(0, 1)))
# 0.0

print(math.degrees(math.atan2(1, 1)))
# 45.0

print(math.degrees(math.atan2(1, 0)))
# 90.0

print(math.degrees(math.atan2(1, -1)))
# 135.0

print(math.degrees(math.atan2(0, -1)))
# 180.0

print(math.degrees(math.atan2(-1, -1)))
# -135.0

print(math.degrees(math.atan2(-1, 0)))
# -90.0

print(math.degrees(math.atan2(-1, 1)))
# -45.0

print(math.degrees(math.atan2(-0.0, -1)))
# -180.0

print(-1 / math.inf)
# -0.0

print(-1.0 * 0.0)
# -0.0

print(-0.0)
# -0.0

print(-0)
# 0

print(math.degrees(math.atan2(0.0, 0.0)))
# 0.0

print(math.degrees(math.atan2(-0.0, 0.0)))
# -0.0

print(math.degrees(math.atan2(-0.0, -0.0)))
# -180.0

print(math.degrees(math.atan2(0.0, -0.0)))
# 180.0

print(math.sin(0.0))
# 0.0

print(math.sin(-0.0))
# -0.0

print(math.asin(0.0))
# 0.0

print(math.asin(-0.0))
# -0.0

print(math.tan(0.0))
# 0.0

print(math.tan(-0.0))
# -0.0

print(math.atan(0.0))
# 0.0

print(math.atan(-0.0))
# -0.0

print(math.atan2(0.0, 1.0))
# 0.0

print(math.atan2(-0.0, 1.0))
# -0.0
