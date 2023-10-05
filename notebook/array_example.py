import array

arr_int = array.array('i', [0, 1, 2])
print(arr_int)
# array('i', [0, 1, 2])

arr_float = array.array('f', [0.0, 0.25, 0.5])
print(arr_float)
# array('f', [0.0, 0.25, 0.5])

# arr_int = array.array('i', [0, 0.5, 1])
# TypeError: 'float' object cannot be interpreted as an integer

print(arr_int[1])
# 1

print(sum(arr_int))
# 3
