import numpy as np

print(np.__version__)
# 1.26.1

ii = np.iinfo(np.int64)
print(type(ii))
# <class 'numpy.iinfo'>

print(ii)
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# 

print(ii.max)
# 9223372036854775807

print(type(ii.max))
# <class 'int'>

print(ii.min)
# -9223372036854775808

print(ii.bits)
# 64

i = 100
print(type(i))
# <class 'int'>

print(np.iinfo(i))
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# 

ui = np.uint8(100)
print(type(ui))
# <class 'numpy.uint8'>

print(np.iinfo(ui))
# Machine parameters for uint8
# ---------------------------------------------------------------
# min = 0
# max = 255
# ---------------------------------------------------------------
# 

a = np.array([1, 2, 3], dtype=np.int8)
print(type(a))
# <class 'numpy.ndarray'>

# print(np.iinfo(a))
# ValueError: Invalid integer data type 'O'.

print(np.iinfo(a.dtype))
# Machine parameters for int8
# ---------------------------------------------------------------
# min = -128
# max = 127
# ---------------------------------------------------------------
# 

print(np.iinfo(a[0]))
# Machine parameters for int8
# ---------------------------------------------------------------
# min = -128
# max = 127
# ---------------------------------------------------------------
# 

fi = np.finfo(np.float64)
print(type(fi))
# <class 'numpy.finfo'>

print(fi)
# Machine parameters for float64
# ---------------------------------------------------------------
# precision =  15   resolution = 1.0000000000000001e-15
# machep =    -52   eps =        2.2204460492503131e-16
# negep =     -53   epsneg =     1.1102230246251565e-16
# minexp =  -1022   tiny =       2.2250738585072014e-308
# maxexp =   1024   max =        1.7976931348623157e+308
# nexp =       11   min =        -max
# smallest_normal = 2.2250738585072014e-308   smallest_subnormal = 4.9406564584124654e-324
# ---------------------------------------------------------------
# 

print(fi.max)
# 1.7976931348623157e+308

print(type(fi.max))
# <class 'numpy.float64'>

print(fi.min)
# -1.7976931348623157e+308

print(fi.eps)
# 2.220446049250313e-16

print(fi.bits)
# 64

print(fi.iexp)
# 11

print(fi.nmant)
# 52
