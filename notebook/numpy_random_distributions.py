import numpy as np

print(np.__version__)
# 1.26.1

rng = np.random.default_rng()

print(rng.binomial(10, 0.5, (2, 3)))
# [[3 7 5]
#  [4 3 5]]

print(rng.beta(2, 2, (2, 3)))
# [[0.84643935 0.50674151 0.30812967]
#  [0.52728096 0.76007311 0.26255972]]

print(rng.gamma(5, 1, (2, 3)))
# [[5.6484851  8.28210475 2.65957385]
#  [2.00776839 6.65851101 7.77808412]]

print(rng.poisson(4, (2, 3)))
# [[1 6 3]
#  [5 2 1]]
