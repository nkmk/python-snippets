l = list(range(-5, 6))
print(l)
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

l_square = [i**2 for i in l]
print(l_square)
# [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]

l_str = [str(i) for i in l]
print(l_str)
# ['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']

l_even = [i for i in l if i % 2 == 0]
print(l_even)
# [-4, -2, 0, 2, 4]

l_minus = [i for i in l if i < 0]
print(l_minus)
# [-5, -4, -3, -2, -1]

l_odd = [i for i in l if not i % 2 == 0]
print(l_odd)
# [-5, -3, -1, 1, 3, 5]

l_plus = [i for i in l if not i < 0]
print(l_plus)
# [0, 1, 2, 3, 4, 5]

l_odd = [i for i in l if i % 2 != 0]
print(l_odd)
# [-5, -3, -1, 1, 3, 5]

l_plus = [i for i in l if i >= 0]
print(l_plus)
# [0, 1, 2, 3, 4, 5]

l_minus_or_even = [i for i in l if (i < 0) or (i % 2 == 0)]
print(l_minus_or_even)
# [-5, -4, -3, -2, -1, 0, 2, 4]

l_minus_and_odd = [i for i in l if (i < 0) and not (i % 2 == 0)]
print(l_minus_and_odd)
# [-5, -3, -1]

a = 80
x = 100 if a > 50 else 0
print(x)
# 100

b = 30
y = 100 if b > 50 else 0
print(y)
# 0

l_replace = [100 if i > 0 else i for i in l]
print(l_replace)
# [-5, -4, -3, -2, -1, 0, 100, 100, 100, 100, 100]

l_replace2 = [100 if i > 0 else 0 for i in l]
print(l_replace2)
# [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100]

l_convert = [i * 10 if i % 2 == 0 else i for i in l]
print(l_convert)
# [-5, -40, -3, -20, -1, 0, 1, 20, 3, 40, 5]

l_convert2 = [i * 10 if i % 2 == 0 else i / 10 for i in l]
print(l_convert2)
# [-0.5, -40, -0.3, -20, -0.1, 0, 0.1, 20, 0.3, 40, 0.5]
