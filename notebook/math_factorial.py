import math

print(math.factorial(5))
# 120

print(math.factorial(0))
# 1

# print(math.factorial(1.5))
# TypeError: 'float' object cannot be interpreted as an integer

# print(math.factorial(-1))
# ValueError: factorial() not defined for negative values

def permutations_count(n, k):
    return math.factorial(n) // math.factorial(n - k)

print(permutations_count(4, 2))
# 12

print(permutations_count(4, 4))
# 24

def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

print(combinations_count(4, 2))
# 6

def combinations_with_replacement_count(n, k):
    return combinations_count(n + k - 1, k)

print(combinations_with_replacement_count(4, 2))
# 10
