import numpy as np

print(np.__version__)
# 1.26.1

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

a_nan = np.array([0, 1, np.nan, float('nan')])
print(a_nan)
# [ 0.  1. nan nan]

print(np.nan == np.nan)
# False

print(np.isnan(np.nan))
# True

print(a_nan == np.nan)
# [False False False False]

print(np.isnan(a_nan))
# [False False  True  True]

a_fill = np.genfromtxt('data/src/sample_nan.csv', delimiter=',',
                       filling_values=0)
print(a_fill)
# [[11. 12.  0. 14.]
#  [21.  0.  0. 24.]
#  [31. 32. 33. 34.]]

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(np.nan_to_num(a))
# [[11. 12.  0. 14.]
#  [21.  0.  0. 24.]
#  [31. 32. 33. 34.]]

print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

np.nan_to_num(a, copy=False)
print(a)
# [[11. 12.  0. 14.]
#  [21.  0.  0. 24.]
#  [31. 32. 33. 34.]]

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(np.nan_to_num(a, nan=-1))
# [[11. 12. -1. 14.]
#  [21. -1. -1. 24.]
#  [31. 32. 33. 34.]]

print(np.nanmean(a))
# 23.555555555555557

print(np.nan_to_num(a, nan=np.nanmean(a)))
# [[11.         12.         23.55555556 14.        ]
#  [21.         23.55555556 23.55555556 24.        ]
#  [31.         32.         33.         34.        ]]

print(np.nanmean(a, axis=0, keepdims=True))
# [[21. 22. 33. 24.]]

print(np.nan_to_num(a, nan=np.nanmean(a, axis=0, keepdims=True)))
# [[11. 12. 33. 14.]
#  [21. 22. 33. 24.]
#  [31. 32. 33. 34.]]

print(np.nanmean(a, axis=1, keepdims=True))
# [[12.33333333]
#  [22.5       ]
#  [32.5       ]]

print(np.nan_to_num(a, nan=np.nanmean(a, axis=1, keepdims=True)))
# [[11.         12.         12.33333333 14.        ]
#  [21.         22.5        22.5        24.        ]
#  [31.         32.         33.         34.        ]]

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')
print(a)
# [[11. 12. nan 14.]
#  [21. nan nan 24.]
#  [31. 32. 33. 34.]]

print(np.isnan(a))
# [[False False  True False]
#  [False  True  True False]
#  [False False False False]]

a[np.isnan(a)] = 0
print(a)
# [[11. 12.  0. 14.]
#  [21.  0.  0. 24.]
#  [31. 32. 33. 34.]]

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')

a[np.isnan(a)] = np.nanmean(a)
print(a)
# [[11.         12.         23.55555556 14.        ]
#  [21.         23.55555556 23.55555556 24.        ]
#  [31.         32.         33.         34.        ]]

a = np.genfromtxt('data/src/sample_nan.csv', delimiter=',')

print(np.where(np.isnan(a), np.nanmean(a, axis=0, keepdims=True), a))
# [[11. 12. 33. 14.]
#  [21. 22. 33. 24.]
#  [31. 32. 33. 34.]]

print(np.where(np.isnan(a), np.nanmean(a, axis=1, keepdims=True), a))
# [[11.         12.         12.33333333 14.        ]
#  [21.         22.5        22.5        24.        ]
#  [31.         32.         33.         34.        ]]
