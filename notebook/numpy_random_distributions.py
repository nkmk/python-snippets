import numpy as np

print(np.__version__)
# 1.26.1

rng = np.random.default_rng(1234)

print(rng.binomial(10, 0.5, (2, 3)))
# [[8 5 7]
#  [4 4 3]]

print(rng.beta(2, 2, (2, 3)))
# [[0.56079809 0.22709038 0.6065771 ]
#  [0.48528102 0.35352709 0.62742706]]

print(rng.gamma(5, 1, (2, 3)))
# [[3.34773947 8.17357458 3.7019044 ]
#  [3.01764646 2.40737805 6.68809771]]

print(rng.poisson(4, (2, 3)))
# [[6 4 8]
#  [2 5 2]]
