import numpy as np

print(np.__version__)
# 1.26.1

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(np.sum(a))
# nan

print(a.sum())
# nan

print(np.nansum(a))
# 212.0

print(np.nansum(a, axis=0))
# [63. 44. 33. 72.]

print(np.nansum(a, axis=1))
# [ 37.  45. 130.]

print(np.nanmean(a))
# 23.555555555555557

print(np.nanmax(a))
# 34.0

print(np.nanmin(a))
# 11.0

print(np.nanstd(a))
# 8.908312112367753

print(np.nanvar(a))
# 79.35802469135803
