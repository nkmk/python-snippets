import numpy as np

print(np.__version__)
# 1.26.1

a_nan = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a_nan)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(np.nan == np.nan)
# False

print(a_nan == np.nan)
# [[False False False False]
#  [False False False False]
#  [False False False False]]

print(np.isnan(a_nan))
# [[False False  True False]
#  [False  True  True False]
#  [False False False False]]

print(np.count_nonzero(np.isnan(a_nan)))
# 3

print(np.count_nonzero(np.isnan(a_nan), axis=0))
# [0 1 2 0]

print(np.count_nonzero(np.isnan(a_nan), axis=1))
# [1 2 0]

print(~np.isnan(a_nan))
# [[ True  True False  True]
#  [ True False False  True]
#  [ True  True  True  True]]
