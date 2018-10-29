import random

print([random.random() for i in range(5)])
# [0.5518201298350598, 0.3476911314933616, 0.8463426180468342, 0.8949046353303931, 0.40822657702632625]

print([random.randint(0, 10) for i in range(5)])
# [8, 5, 7, 10, 7]

print(random.sample(range(10), k=5))
# [6, 4, 3, 7, 5]

print(random.sample(range(100, 200, 10), k=5))
# [130, 190, 140, 150, 170]
