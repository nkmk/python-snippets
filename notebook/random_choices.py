import random

l = [0, 1, 2, 3, 4]

print(random.choices(l, k=3))
# [2, 1, 0]

print(random.choices(l, k=10))
# [3, 4, 1, 4, 4, 2, 0, 4, 2, 0]

print(random.choices(l))
# [1]

print(random.choices(l, k=3, weights=[1, 1, 1, 10, 1]))
# [0, 2, 3]

print(random.choices(l, k=3, weights=[1, 1, 0, 0, 0]))
# [0, 1, 1]

print(random.choices(l, k=3, cum_weights=[1, 2, 3, 13, 14]))
# [3, 2, 3]

# print(random.choices(l, k=3, weights=[1, 1, 1, 10, 1, 1, 1]))
# ValueError: The number of weights does not match the population_

# print(random.choices(l, k=3, weights=[1, 1, 1, 10, 1], cum_weights=[1, 2, 3, 13, 14]))
# TypeError: Cannot specify both weights and cumulative weights
