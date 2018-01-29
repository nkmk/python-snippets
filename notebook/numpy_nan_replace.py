import numpy as np

arr = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(arr)
# [[ 11.  12.  nan  14.]
#  [ 21.  nan  nan  24.]
#  [ 31.  32.  33.  34.]]

arr_fill = np.genfromtxt('data/src/sample_nan.csv', delimiter=',', filling_values=0)
print(arr_fill)
# [[ 11.  12.   0.  14.]
#  [ 21.   0.   0.  24.]
#  [ 31.  32.  33.  34.]]

print(np.isnan(arr))
# [[False False  True False]
#  [False  True  True False]
#  [False False False False]]

arr[np.isnan(arr)] = 0
print(arr)
# [[ 11.  12.   0.  14.]
#  [ 21.   0.   0.  24.]
#  [ 31.  32.  33.  34.]]

arr = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
arr[np.isnan(arr)] = np.nanmean(arr)
print(arr)
# [[ 11.          12.          23.55555556  14.        ]
#  [ 21.          23.55555556  23.55555556  24.        ]
#  [ 31.          32.          33.          34.        ]]
