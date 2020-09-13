l = [1, -3, 2]

print(sorted(l))
# [-3, 1, 2]

print(sorted(l, key=abs))
# [1, 2, -3]

l_abs = [abs(i) for i in l]
print(l_abs)
# [1, 3, 2]

print(sorted(l_abs))
# [1, 2, 3]

l.sort(key=abs)
print(l)
# [1, 2, -3]

l = [1, -3, 2]

print(max(l))
# 2

print(max(l, key=abs))
# -3

print(min(l))
# -3

print(min(l, key=abs))
# 1

l_str = ['bbb', 'c', 'aa']

print(sorted(l_str))
# ['aa', 'bbb', 'c']

print(sorted(l_str, key=len))
# ['c', 'aa', 'bbb']

l_2d = [[2, 10], [1, -30], [-3, 20]]

print(sorted(l_2d))
# [[-3, 20], [1, -30], [2, 10]]

print(sorted(l_2d, key=max))
# [[1, -30], [2, 10], [-3, 20]]

print(sorted(l_2d, key=lambda x: max([abs(i) for i in x])))
# [[2, 10], [-3, 20], [1, -30]]

print(sorted(l_2d, key=lambda x: max(abs(i) for i in x)))
# [[2, 10], [-3, 20], [1, -30]]

def max_abs(x):
    return max(abs(i) for i in x)

print(sorted(l_2d, key=max_abs))
# [[2, 10], [-3, 20], [1, -30]]
