import statistics
import math

l = [1, 3, 8, 15]

print(statistics.mean(l))
# 6.75

print(sum(l) / len(l))
# 6.75

l = [3, 1, 8]

print(statistics.median(l))
# 3

print(statistics.median_low(l))
# 3

print(statistics.median_high(l))
# 3

l = [3, 1, 8, 15]

print(statistics.median(l))
# 5.5

print(statistics.median_low(l))
# 3

print(statistics.median_high(l))
# 8

l = [3, 2, 3, 2, 1, 2]

print(statistics.mode(l))
# 2

print(statistics.multimode(l))
# [2]

l = [3, 2, 3, 2, 1, 2, 3]

print(statistics.mode(l))
# 3

print(statistics.multimode(l))
# [3, 2]

l = [10, 1, 3, 7, 1]

print(statistics.pvariance(l))
# 12.64

print(sum((x - sum(l) / len(l)) ** 2 for x in l) / len(l))
# 12.64

l = [10, 1, 3, 7, 1]

print(statistics.variance(l))
# 15.8

print(sum((x - sum(l) / len(l)) ** 2 for x in l) / (len(l) - 1))
# 15.8

l = [10, 1, 3, 7, 1]

print(statistics.pstdev(l))
# 3.5552777669262356

print(math.sqrt(statistics.pvariance(l)))
# 3.5552777669262356

l = [10, 1, 3, 7, 1]

print(statistics.stdev(l))
# 3.9749213828703582

print(math.sqrt(statistics.variance(l)))
# 3.9749213828703582
