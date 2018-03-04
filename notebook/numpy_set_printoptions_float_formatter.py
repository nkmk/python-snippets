import numpy as np

print(np.get_printoptions())
# {'edgeitems': 3, 'threshold': 1000, 'floatmode': 'maxprec', 'precision': 8, 'suppress': False, 'linewidth': 75, 'nanstr': 'nan', 'infstr': 'inf', 'sign': '-', 'formatter': None, 'legacy': False}

a = np.array([12.3456, 0.123456789])
print(a)
# [12.3456      0.12345679]

np.set_printoptions(precision=3)
print(a)
# [12.346  0.123]

np.set_printoptions(precision=10)
print(a)
# [12.3456       0.123456789]

np.set_printoptions(precision=4, floatmode='maxprec')
print(a)
# [12.3456  0.1235]

np.set_printoptions(precision=10, floatmode='maxprec')
print(a)
# [12.3456       0.123456789]

np.set_printoptions(precision=4, floatmode='fixed')
print(a)
# [12.3456  0.1235]

np.set_printoptions(precision=10, floatmode='fixed')
print(a)
# [12.3456000000  0.1234567890]

np.set_printoptions(precision=4, floatmode='maxprec_equal')
print(a)
# [12.3456  0.1235]

np.set_printoptions(precision=10, floatmode='maxprec_equal')
print(a)
# [12.345600000  0.123456789]

np.set_printoptions(precision=4, floatmode='unique')
print(a)
# [12.3456       0.123456789]

np.set_printoptions(precision=10, floatmode='unique')
print(a)
# [12.3456       0.123456789]

np.set_printoptions(precision=8, floatmode='maxprec')

b = np.round(a, 2)
print(b)
# [12.35  0.12]

b = np.round(a, -1)
print(b)
# [10.  0.]

b = np.round([1234.56, 123456.789], -2)
print(b)
# [  1200. 123500.]

a = np.array([0.123456, 0.123456])
print(a)
# [0.123456 0.123456]

a = np.array([0.123456, 0.0000123456])
print(a)
# [1.23456e-01 1.23456e-05]

a = np.array([123.456, 0.0123456])
print(a)
# [1.23456e+02 1.23456e-02]

np.set_printoptions(suppress=True)
print(a)
# [123.456       0.0123456]

np.set_printoptions(suppress=True, precision=2)
print(a)
# [123.46   0.01]

np.set_printoptions(suppress=False, precision=2)
print(a)
# [1.23e+02 1.23e-02]

np.set_printoptions(suppress=False, precision=8, floatmode='fixed')
print(a)
# [1.23456000e+02 1.23456000e-02]

np.set_printoptions(precision=8, floatmode='maxprec', suppress=False)

a = np.array([123.456, 0.0123456])
print(a)
# [1.23456e+02 1.23456e-02]

np.set_printoptions(formatter={'float': '{:.2f}'.format})
print(a)
# [123.46 0.01]

np.set_printoptions(formatter={'float': '{:.8f}'.format})
print(a)
# [123.45600000 0.01234560]

np.set_printoptions(formatter={'float': '{:.2e}'.format})
print(a)
# [1.23e+02 1.23e-02]

np.set_printoptions(formatter={'float': '{:.8e}'.format})
print(a)
# [1.23456000e+02 1.23456000e-02]

a = np.array([12, 1234])
print(a)
# [  12 1234]

np.set_printoptions(formatter={'int': '{:08d}'.format})
print(a)
# [00000012 00001234]

np.set_printoptions(formatter={'int': '{:b}'.format})
print(a)
# [1100 10011010010]

np.set_printoptions(formatter={'int': '{:o}'.format})
print(a)
# [14 2322]

np.set_printoptions(formatter={'int': '{:x}'.format})
print(a)
# [c 4d2]

a = np.array(['One', 'Two'])
print(a)
# ['One' 'Two']

np.set_printoptions(formatter={'numpystr': str.upper})
print(a)
# [ONE TWO]

np.set_printoptions(formatter={'numpystr': lambda x: '***' + x + '***'})
print(a)
# [***One*** ***Two***]

np.set_printoptions(formatter={'float': '{:0.8e}'.format, 'int': '{:08d}'.format})

a = np.array([12, 12.34])
print(a.dtype)
print(a)
# float64
# [1.20000000e+01 1.23400000e+01]

a = np.array([12, 123])
print(a.dtype)
print(a)
# int64
# [00000012 00000123]
