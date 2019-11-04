import numpy as np

ii64 = np.iinfo(np.int64)
print(type(ii64))
# <class 'numpy.iinfo'>

print(ii64)
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# 

print(ii64.max)
# 9223372036854775807

print(type(ii64.max))
# <class 'int'>

print(ii64.min)
# -9223372036854775808

print(ii64.bits)
# 64

print(np.iinfo('int16'))
# Machine parameters for int16
# ---------------------------------------------------------------
# min = -32768
# max = 32767
# ---------------------------------------------------------------
# 

print(np.iinfo('i4'))
# Machine parameters for int32
# ---------------------------------------------------------------
# min = -2147483648
# max = 2147483647
# ---------------------------------------------------------------
# 

print(np.iinfo(int))
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# 

print(np.iinfo('uint64'))
# Machine parameters for uint64
# ---------------------------------------------------------------
# min = 0
# max = 18446744073709551615
# ---------------------------------------------------------------
# 

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

# print(np.iinfo(np.float64))
# ValueError: Invalid integer data type 'f'.

fi64 = np.finfo(np.float64)
print(type(fi64))
# <class 'numpy.finfo'>

print(fi64)
# Machine parameters for float64
# ---------------------------------------------------------------
# precision =  15   resolution = 1.0000000000000001e-15
# machep =    -52   eps =        2.2204460492503131e-16
# negep =     -53   epsneg =     1.1102230246251565e-16
# minexp =  -1022   tiny =       2.2250738585072014e-308
# maxexp =   1024   max =        1.7976931348623157e+308
# nexp =       11   min =        -max
# ---------------------------------------------------------------
# 

print(fi64.max)
# 1.7976931348623157e+308

print(type(fi64.max))
# <class 'numpy.float64'>

print(fi64.min)
# -1.7976931348623157e+308

print(fi64.eps)
# 2.220446049250313e-16

print(fi64.bits)
# 64

print(fi64.iexp)
# 11

print(fi64.nmant)
# 52
