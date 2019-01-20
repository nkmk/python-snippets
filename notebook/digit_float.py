f = 987.6543

print(f)
# 987.6543

print(type(f))
# <class 'float'>

s = str(f)

print(s)
# 987.6543

print(type(s))
# <class 'str'>

print(s.split('.'))
# ['987', '6543']

print(type(s.split('.')))
# <class 'list'>

print(type(s.split('.')[0]))
# <class 'str'>

s_i, s_d = s.split('.')

print(s_i)
# 987

print(s_d)
# 6543

print(len(s_i))
# 3

print(len(s_d))
# 4

print(len(str(f).split('.')[0]))
# 3

print(len(str(f).split('.')[1]))
# 4

print(s_i[-1])
# 7

print(s_i[-3])
# 9

print(s_d[0])
# 6

print(s_d[3])
# 3

print(type(s_d[3]))
# <class 'str'>

print(int(s_d[3]))
# 3

print(type(int(s_d[3])))
# <class 'int'>

print(str(f).split('.')[0][-3])
# 9

print(int(str(f).split('.')[0][-3]))
# 9

print(str(f).split('.')[1][3])
# 3

print(int(str(f).split('.')[1][3]))
# 3
