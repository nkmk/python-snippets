import numpy as np

print(np.__version__)
# 1.26.1

np.random.seed(1234)

rng = np.random.default_rng(1234)

print(rng.random())
# 0.9766997666981422

print(rng.random(3))
# [0.38019574 0.92324623 0.26169242]

print(rng.random((2, 3)))
# [[0.31909706 0.11809123 0.24176629]
#  [0.31853393 0.96407925 0.2636498 ]]

print(np.random.random_sample((2, 3)))
# [[0.19151945 0.62210877 0.43772774]
#  [0.78535858 0.77997581 0.27259261]]

print(np.random.rand(2, 3))
# [[0.27646426 0.80187218 0.95813935]
#  [0.87593263 0.35781727 0.50099513]]

rng = np.random.default_rng(1234)

print(rng.uniform(-50.0, 50.0))
# 47.66997666981422

print(rng.uniform(-50.0, 50.0, 3))
# [-11.9804265   42.32462338 -23.83075761]

print(rng.uniform(-50.0, 50.0, (2, 3)))
# [[-18.09029416 -38.1908767  -25.82337067]
#  [-18.14660712  46.40792452 -23.63501957]]

print(np.random.uniform(-50.0, 50.0, (2, 3)))
# [[ 18.34629352  21.2702027  -12.97492452]
#  [  6.11961861   0.30831653 -48.62315504]]

rng = np.random.default_rng(1234)

print(rng.integers(100))
# 97

print(rng.integers(100, size=3))
# [97 98 38]

print(rng.integers(100, size=(2, 3)))
# [[17 92 10]
#  [26 13 31]]

print(rng.integers(100, 200, (2, 3)))
# [[153 111 179]
#  [124 178 131]]

print(rng.integers(100, 200, (2, 3), endpoint=True))
# [[180 197 196]
#  [126 156 144]]

print(np.random.randint(100, 200, (2, 3)))
# [[134 138 167]
#  [111 100 175]]
