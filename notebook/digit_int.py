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

print(len(s))
# 4

print(type(len(s)))
# <class 'int'>

print(len(str(i)))
# 4

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
