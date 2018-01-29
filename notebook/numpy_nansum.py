import numpy as np

arr = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(arr)
# [[ 11.  12.  nan  14.]
#  [ 21.  nan  nan  24.]
#  [ 31.  32.  33.  34.]]

print(arr.sum())
# nan

print(np.sum(arr))
# nan

print(np.nansum(arr))
# 212.0

print(np.nansum(arr, axis=0))
# [ 63.  44.  33.  72.]

print(np.nansum(arr, axis=1))
# [  37.   45.  130.]

print(np.nanmean(arr))
# 23.5555555556

print(np.nanmax(arr))
# 34.0

print(np.nanmin(arr))
# 11.0

print(np.nanstd(arr))
# 8.90831211237

print(np.nanvar(arr))
# 79.3580246914
