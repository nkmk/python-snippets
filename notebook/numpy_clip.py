import numpy as np

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(np.clip(a, 2, 7))
# [2 2 2 3 4 5 6 7 7 7]

print(np.clip(a, None, 7))
# [0 1 2 3 4 5 6 7 7 7]

print(np.clip(a, 2, None))
# [2 2 2 3 4 5 6 7 8 9]

# print(np.clip(a, 2))
# TypeError: clip() missing 1 required positional argument: 'a_max'

a_clip = np.clip(a, 2, 7)
print(a_clip)
# [2 2 2 3 4 5 6 7 7 7]

print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(a.clip(2, 7))
# [2 2 2 3 4 5 6 7 7 7]

print(a.clip(None, 7))
# [0 1 2 3 4 5 6 7 7 7]

print(a.clip(2, None))
# [2 2 2 3 4 5 6 7 8 9]

print(a.clip(2))
# [2 2 2 3 4 5 6 7 8 9]

print(a.clip(min=2))
# [2 2 2 3 4 5 6 7 8 9]

print(a.clip(max=7))
# [0 1 2 3 4 5 6 7 7 7]

a_clip = a.clip(2, 7)
print(a_clip)
# [2 2 2 3 4 5 6 7 7 7]

print(a)
# [0 1 2 3 4 5 6 7 8 9]
