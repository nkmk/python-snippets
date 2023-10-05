i = 9876
print(i)
# 9876

print(type(i))
# <class 'int'>

s = str(i)
print(s)
# 9876

print(type(s))
# <class 'str'>

i = 9876
s = str(i)

print(len(s))
# 4

print(type(len(s)))
# <class 'int'>

print(len(str(i)))
# 4

i_minus = -9876
s_minus = str(i_minus)
print(s_minus)
# -9876

print(len(s_minus))
# 5

print(abs(i_minus))
# 9876

print(len(str(abs(i_minus))))
# 4

i = 9876
s = str(i)

print(s[-1])
# 6

print(s[-3])
# 8

# print(s[-10])
# IndexError: string index out of range

print(type(s[-1]))
# <class 'str'>

print(int(s[-1]))
# 6

print(type(int(s[-1])))
# <class 'int'>

print(str(i)[-1])
# 6

print(int(str(i)[-1]))
# 6

s = '9,675'

print(s.replace(',', ''))
# 9675

print(type(s.replace(',', '')))
# <class 'str'>

print(len(s.replace(',', '')))
# 4

print(s.replace(',', '')[-3])
# 6
