import numpy as np

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(np.isnan(a))
# [[False False  True False]
#  [False  True  True False]
#  [False False False False]]

print(~np.isnan(a))
# [[ True  True False  True]
#  [ True False False  True]
#  [ True  True  True  True]]

print(a[~np.isnan(a)])
# [11. 12. 14. 21. 24. 31. 32. 33. 34.]

print(np.isnan(a).any(axis=1))
# [ True  True False]

print(~np.isnan(a).any(axis=1))
# [False False  True]

print(a[~np.isnan(a).any(axis=1), :])
# [[31. 32. 33. 34.]]

print(a[~np.isnan(a).any(axis=1)])
# [[31. 32. 33. 34.]]

print(~np.isnan(a).any(axis=0))
# [ True False False  True]

print(a[:, ~np.isnan(a).any(axis=0)])
# [[11. 14.]
#  [21. 24.]
#  [31. 34.]]

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
a[2, 2] = np.nan
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. nan 34.]]

print(a[:, ~np.isnan(a).any(axis=0)])
# [[11. 14.]
#  [21. 24.]
#  [31. 34.]]

print(a[:, ~np.isnan(a).all(axis=0)])
# [[11. 12. 14.]
#  [21. nan 24.]
#  [31. 32. 34.]]
