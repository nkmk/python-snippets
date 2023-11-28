import numpy as np

print(np.__version__)
# 1.26.1

rs = np.random.RandomState()
print(rs)
# RandomState(MT19937)

print(rs.rand())
# 0.07714411293114853

print(rs.rand(3))
# [0.41864167 0.24060533 0.33237037]

print(rs.rand(2, 3))
# [[0.44510064 0.81320106 0.79076827]
#  [0.84813432 0.83270079 0.10677157]]

rs_1 = np.random.RandomState(1234)
print(rs_1.rand())
# 0.1915194503788923

rs_2 = np.random.RandomState(1234)
print(rs_2.rand())
# 0.1915194503788923

print(np.random.rand())
# 0.2766767103883432

print(np.random.rand(3))
# [0.77490366 0.01897116 0.83984223]

print(np.random.rand(2, 3))
# [[0.22135358 0.56604746 0.03200072]
#  [0.04187504 0.32511305 0.0366836 ]]

np.random.seed(1234)
print(np.random.rand())
# 0.1915194503788923

np.random.seed(1234)
print(np.random.rand())
# 0.1915194503788923
