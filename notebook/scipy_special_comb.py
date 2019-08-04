from scipy.special import comb

print(comb(4, 2))
# 6.0

print(comb(4, 2, exact=True))
# 6

print(comb(4, 0, exact=True))
# 1

print(comb(4, 2, exact=True, repetition=True))
# 10
