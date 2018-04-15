import array

arr_int = array.array('i', [0, 1, 2])
print(arr_int)
# array('i', [0, 1, 2])

arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)
# array('f', [0.0, 0.10000000149011612, 0.20000000298023224])

# arr_int = array.array('i', [0, 0.1, 2])
# TypeError: integer argument expected, got float

print(arr_int[1])
# 1

print(sum(arr_int))
# 3
