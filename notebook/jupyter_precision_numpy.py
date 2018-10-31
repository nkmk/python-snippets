import numpy as np

a = np.array([0.123456789, 0.987654321])

a
# array([0.12345679, 0.98765432])

%precision 3
# '%.3f'

a
# array([0.123, 0.988])

print(a)
# [0.123 0.988]

print(np.get_printoptions()['precision'])
# 3

np.set_printoptions(precision=5)

a
# array([0.12346, 0.98765])

print(a)
# [0.12346 0.98765]

print(a[0])
# 0.123456789

%precision
# '%r'

a
# array([0.12345679, 0.98765432])

print(np.get_printoptions()['precision'])
# 8

%precision %.2e
# '%.2e'

a
# array([0.12345679, 0.98765432])

np.set_printoptions(formatter={'float': '{:.2e}'.format})

a
# array([1.23e-01, 9.88e-01])
