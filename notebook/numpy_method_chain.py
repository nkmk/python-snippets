import numpy as np

a = np.arange(12)
a = a.reshape(3, 4)
a = a.clip(2, 9)

print(a)
# [[2 2 2 3]
#  [4 5 6 7]
#  [8 9 9 9]]

a_mc = np.arange(12).reshape(3, 4).clip(2, 9)

print(a_mc)
# [[2 2 2 3]
#  [4 5 6 7]
#  [8 9 9 9]]

a_mc_break_parens = (
    np.arange(12)
    .reshape(3, 4)
    .clip(2, 9)
)

print(a_mc_break_parens)
# [[2 2 2 3]
#  [4 5 6 7]
#  [8 9 9 9]]
