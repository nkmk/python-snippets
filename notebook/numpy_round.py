import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([12.3, 45.6, 78.9])

print(np.round(a))
# [12. 46. 79.]

print(np.round(a).dtype)
# float64

print(np.round(a).astype(int))
# [12 46 79]

print(a.astype(int))
# [12 45 78]

l = [12.3, 45.6, 78.9]

print(np.round(l))
# [12. 46. 79.]

print(type(np.round(l)))
# <class 'numpy.ndarray'>

print(np.round(12.3))
# 12.0

print(np.round(123.456))
# 123.0

print(np.round(123.456, 2))
# 123.46

print(np.round(123.456, -2))
# 100.0

print(np.round(123456))
# 123456

print(np.round(123456, 2))
# 123456

print(np.round(123456, -2))
# 123500

a = np.array([12345, 67890])

print(np.round(a, -3))
# [12000 68000]

print(np.round(a, -3).dtype)
# int64

print(np.round([-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]))
# [-4. -2. -2. -0.  0.  2.  2.  4.]

print(np.round([-350, -250, -150, -50, 50, 150, 250, 350], -2))
# [-400 -200 -200    0    0  200  200  400]

print(np.round([2.49, 2.5, 2.51]))
# [2. 2. 3.]

print(np.round([249, 250, 251], -2))
# [200 200 300]

print(np.round(0.15, 1))
# 0.2

print(round(0.15, 1))
# 0.1

print(f'{0.15:.20}')
# 0.14999999999999999445

print(np.round(56294995342131.5, 3))
# 56294995342131.51

print(round(56294995342131.5, 3))
# 56294995342131.5

a = np.array([12.3, 45.6, 78.9])

print(np.around(a))
# [12. 46. 79.]

print(np.around(a, -1))
# [10. 50. 80.]

print(a.round())
# [12. 46. 79.]

print(a.round(-1))
# [10. 50. 80.]

def my_round(x, decimals=0):
    return np.floor(x * 10**decimals + 0.5) / 10**decimals

a = np.array([-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5])

print(np.round(a))
# [-4. -2. -2. -0.  0.  2.  2.  4.]

print(my_round(a))
# [-3. -2. -1.  0.  1.  2.  3.  4.]

print(a / 10)
# [-0.35 -0.25 -0.15 -0.05  0.05  0.15  0.25  0.35]

print(np.round(a / 10, 1))
# [-0.4 -0.2 -0.2 -0.   0.   0.2  0.2  0.4]

print(my_round(a / 10, 1))
# [-0.3 -0.2 -0.1  0.   0.1  0.2  0.3  0.4]

def my_round2(x, decimals=0):
    return np.sign(x) * np.floor(np.abs(x) * 10**decimals + 0.5) / 10**decimals

print(a)
# [-3.5 -2.5 -1.5 -0.5  0.5  1.5  2.5  3.5]

print(my_round(a))
# [-3. -2. -1.  0.  1.  2.  3.  4.]

print(my_round2(a))
# [-4. -3. -2. -1.  1.  2.  3.  4.]

print(a / 10)
# [-0.35 -0.25 -0.15 -0.05  0.05  0.15  0.25  0.35]

print(my_round(a / 10, 1))
# [-0.3 -0.2 -0.1  0.   0.1  0.2  0.3  0.4]

print(my_round2(a / 10, 1))
# [-0.4 -0.3 -0.2 -0.1  0.1  0.2  0.3  0.4]
