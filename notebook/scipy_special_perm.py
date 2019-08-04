from scipy.special import perm

print(perm(4, 2))
# 12.0

print(perm(4, 2, exact=True))
# 12

print(perm(4, 4, exact=True))
# 24
