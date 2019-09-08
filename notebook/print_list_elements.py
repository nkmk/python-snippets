l = [0, 1, 2]
print(l)
# [0, 1, 2]

print(*l)  # => print(0, 1, 2)
# 0 1 2

print(*l, sep='')
# 012

print(*l, sep='-')
# 0-1-2

s = '-'.join([str(i) for i in l])
print(s)
# 0-1-2
