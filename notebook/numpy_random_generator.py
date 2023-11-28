import numpy as np

print(np.__version__)
# 1.26.1

rng = np.random.default_rng()
print(rng)
# Generator(PCG64)

print(rng.random())
# 0.2281556131299135

print(type(rng.random()))
# <class 'float'>

print(rng.random(3))
# [0.3888496  0.9058742  0.74585675]

print(type(rng.random(3)))
# <class 'numpy.ndarray'>

print(rng.random((2, 3)))
# [[0.42818743 0.22573104 0.33022384]
#  [0.64782123 0.82035051 0.31118108]]

print(type(rng.random((2, 3))))
# <class 'numpy.ndarray'>

rng_1 = np.random.default_rng(1234)
print(rng_1.random())
# 0.9766997666981422

rng_2 = np.random.default_rng(1234)
print(rng_2.random())
# 0.9766997666981422

rng_mt = np.random.Generator(np.random.MT19937(1234))
print(rng_mt)
# Generator(MT19937)

print(rng_mt.random())
# 0.12038356302504949
