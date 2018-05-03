import statistics
import math

l = [10, 1, 3, 7, 1]

mean = statistics.mean(l)
print(mean)
# 4.4

my_mean = sum(l) / len(l)
print(my_mean)
# 4.4

harmonic_mean = statistics.harmonic_mean(l)
print(harmonic_mean)
# 1.9408502772643252

my_harmonic_mean = len(l) / sum(1 / x for x in l)
print(my_harmonic_mean)
# 1.9408502772643255

median = statistics.median(l)
print(median)
# 3

l_even = [10, 1, 3, 7, 1, 6]

median = statistics.median(l_even)
print(median)
# 4.5

median_low = statistics.median_low(l_even)
print(median_low)
# 3

median_high = statistics.median_high(l_even)
print(median_high)
# 6

print(statistics.median_high(l) == statistics.median_low(l) == statistics.median(l))
# True

mode = statistics.mode(l)
print(mode)
# 1

l_mode_error = [1, 2, 3, 4, 5]

# mode = statistics.mode(l_mode_error)
# StatisticsError: no unique mode; found 5 equally common values

l_mode_error = [1, 1, 1, 2, 2, 2, 3]

# mode = statistics.mode(l_mode_error)
# StatisticsError: no unique mode; found 2 equally common values

pvariance = statistics.pvariance(l)
print(pvariance)
# 12.64

my_pvariance = sum((x - sum(l) / len(l))**2 for x in l) / len(l)
print(my_pvariance)
# 12.64

pstdev = statistics.pstdev(l)
print(pstdev)
# 3.5552777669262356

print(math.sqrt(pvariance))
# 3.5552777669262356

variance = statistics.variance(l)
print(variance)
# 15.8

my_variance = sum((x - sum(l) / len(l))**2 for x in l) / (len(l) - 1)
print(my_variance)
# 15.8

stdev = statistics.stdev(l)
print(stdev)
# 3.9749213828703582

print(math.sqrt(variance))
# 3.9749213828703582
