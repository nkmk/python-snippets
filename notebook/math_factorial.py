import math

print(math.factorial(5))
# 120

print(math.factorial(0))
# 1

# print(math.factorial(1.5))
# ValueError: factorial() only accepts integral values

# print(math.factorial(-1))
# ValueError: factorial() not defined for negative values

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

print(permutations_count(4, 2))
# 12

print(permutations_count(4, 4))
# 24

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(combinations_count(4, 2))
# 6

def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)

print(combinations_with_replacement_count(4, 2))
# 10
