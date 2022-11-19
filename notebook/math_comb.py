import math

print(math.comb(4, 2))
# 6

# print(math.comb(4.5, 2.5))
# TypeError: 'float' object cannot be interpreted as an integer

# print(math.comb(-4, -2))
# ValueError: n must be a non-negative integer

def combinations_with_replacement_count(n, k):
    return math.comb(n + k - 1, k)

print(combinations_with_replacement_count(4, 2))
# 10
