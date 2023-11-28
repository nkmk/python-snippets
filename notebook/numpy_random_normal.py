import numpy as np

print(np.__version__)
# 1.26.1

np.random.seed(1234)

rng = np.random.default_rng(1234)

print(rng.standard_normal())
# -1.6038368053963015

print(rng.standard_normal(3))
# [0.06409991 0.7408913  0.15261919]

print(rng.standard_normal((2, 3)))
# [[ 0.86374389  2.91309922 -1.47882336]
#  [ 0.94547297 -1.66613546  0.34374458]]

print(np.random.standard_normal((2, 3)))
# [[ 0.47143516 -1.19097569  1.43270697]
#  [-0.3126519  -0.72058873  0.88716294]]

print(np.random.randn(2, 3))
# [[ 0.85958841 -0.6365235   0.01569637]
#  [-2.24268495  1.15003572  0.99194602]]

rng = np.random.default_rng(1234)

print(rng.normal(2, 2.5))
# -2.009592013490754

print(rng.normal(2, 2.5, 3))
# [2.16024979 3.85222824 2.38154798]

print(rng.normal(2, 2.5, (2, 3)))
# [[ 4.15935973  9.28274806 -1.6970584 ]
#  [ 4.36368244 -2.16533864  2.85936145]]

print(np.random.normal(2, 2.5, (2, 3)))
# [[ 4.38331032 -3.05313705  1.16480659]
#  [ 2.00529591  3.01363353  2.72272985]]
