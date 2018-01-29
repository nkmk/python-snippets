import numpy as np

arr = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(arr)
# [[ 11.  12.  nan  14.]
#  [ 21.  nan  nan  24.]
#  [ 31.  32.  33.  34.]]

print(np.isnan(arr))
# [[False False  True False]
#  [False  True  True False]
#  [False False False False]]

print(arr[~np.isnan(arr)])
# [ 11.  12.  14.  21.  24.  31.  32.  33.  34.]

print(np.isnan(arr).any(axis=1))
# [ True  True False]

print(~np.isnan(arr).any(axis=1))
# [False False  True]

print(arr[~np.isnan(arr).any(axis=1), :])
# [[ 31.  32.  33.  34.]]

print(arr[~np.isnan(arr).any(axis=1)])
# [[ 31.  32.  33.  34.]]

print(~np.isnan(arr).any(axis=0))
# [ True False False  True]

print(arr[:, ~np.isnan(arr).any(axis=0)])
# [[ 11.  14.]
#  [ 21.  24.]
#  [ 31.  34.]]
