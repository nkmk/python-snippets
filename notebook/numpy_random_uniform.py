import numpy as np

print(np.__version__)
# 1.26.1

rng = np.random.default_rng()

print(rng.random())
# 0.11769302730981768

print(rng.random(3))
# [0.58905312 0.90484592 0.90395364]

print(rng.random((2, 3)))
# [[0.59463288 0.19670697 0.95594319]
#  [0.94165422 0.18974122 0.33570092]]

print(np.random.random_sample((2, 3)))
# [[0.34446051 0.76218429 0.37339732]
#  [0.22533506 0.00148215 0.70198151]]

print(np.random.rand(2, 3))
# [[0.78823483 0.00620854 0.96619249]
#  [0.32573769 0.36434893 0.04472163]]

rng = np.random.default_rng()

print(rng.uniform(-50.0, 50.0))
# 17.611381123655846

print(rng.uniform(-50.0, 50.0, 3))
# [ 5.80448109  6.64291183 22.27752257]

print(rng.uniform(-50.0, 50.0, (2, 3)))
# [[ 12.23855165  -9.97903127 -38.40667299]
#  [-14.42414448 -45.04563195  14.37486871]]

print(np.random.uniform(-50.0, 50.0, (2, 3)))
# [[-25.63149057  16.80691914  20.69418218]
#  [ 32.53480087 -10.83462837  15.18192629]]

rng = np.random.default_rng()

print(rng.integers(100))
# 24

print(rng.integers(100, size=3))
# [ 9 25 27]

print(rng.integers(100, size=(2, 3)))
# [[78  2 42]
#  [25  6 16]]

print(rng.integers(100, 200, (2, 3)))
# [[134 142 129]
#  [154 180 103]]

print(rng.integers(100, 200, (2, 3), endpoint=True))
# [[170 157 172]
#  [121 200 191]]

print(np.random.randint(100, 200, (2, 3)))
# [[120 121 138]
#  [159 140 197]]
