a_l = [0, 1, 2]
b_l = [10, 20, 30]

a_t = (0, 1, 2)
b_t = (10, 20, 30)

a_s = 'abc'
b_s = 'xyz'

print(a_l + b_l)
# [0, 1, 2, 10, 20, 30]

print(a_t + b_t)
# (0, 1, 2, 10, 20, 30)

print(a_s + b_s)
# abcxyz

# print(a_l + 3)
# TypeError: can only concatenate list (not "int") to list

print(a_l + [3])
# [0, 1, 2, 3]

# print(a_t + (3))
# TypeError: can only concatenate tuple (not "int") to tuple

print(a_t + (3, ))
# (0, 1, 2, 3)

a_l += b_l
print(a_l)
# [0, 1, 2, 10, 20, 30]

a_t += b_t
print(a_t)
# (0, 1, 2, 10, 20, 30)

a_s += b_s
print(a_s)
# abcxyz

print(b_l * 3)
# [10, 20, 30, 10, 20, 30, 10, 20, 30]

print(3 * b_l)
# [10, 20, 30, 10, 20, 30, 10, 20, 30]

print(b_t * 3)
# (10, 20, 30, 10, 20, 30, 10, 20, 30)

print(3 * b_t)
# (10, 20, 30, 10, 20, 30, 10, 20, 30)

print(b_s * 3)
# xyzxyzxyz

print(3 * b_s)
# xyzxyzxyz

# print(b_l * 0.5)
# TypeError: can't multiply sequence by non-int of type 'float'

print(b_l * -1)
# []

b_l *= 3
print(b_l)
# [10, 20, 30, 10, 20, 30, 10, 20, 30]

b_t *= 3
print(b_t)
# (10, 20, 30, 10, 20, 30, 10, 20, 30)

b_s *= 3
print(b_s)
# xyzxyzxyz

a_l = [0, 1, 2]
b_l = [10, 20, 30]

c_l = a_l + b_l * 3
print(c_l)
# [0, 1, 2, 10, 20, 30, 10, 20, 30, 10, 20, 30]
