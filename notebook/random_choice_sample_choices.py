import random

l = list(range(5))
print(l)
# [0, 1, 2, 3, 4]

print(random.choice(l))
# 3

print(random.choice(['グー', 'チョキ', 'パー']))
# グー

print(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))
# 中吉

print(random.sample(l, 3))
# [2, 3, 0]

print(random.choices(l, k=3))
# [4, 1, 4]

print(random.choices(l, k=10))
# [1, 4, 3, 2, 4, 0, 3, 2, 4, 1]

print(random.choices(l, k=3, weights=[1, 1, 1, 10, 1]))
# [4, 3, 3]

print(random.choices(l, k=3, weights=[1, 1, 0, 0, 0]))
# [1, 0, 1]

print(random.choices(l, k=3, cum_weights=[1, 2, 3, 13, 14]))
# [3, 3, 3]

random.seed(0)
print(random.choice(l))
# 3
