l = [3, 1, 4, 5, 2]

l.sort()
print(l)
# [1, 2, 3, 4, 5]

print(l.sort())
# None

l.sort(reverse=True)
print(l)
# [5, 4, 3, 2, 1]

l = [3, 1, 4, 5, 2]

l_sorted = sorted(l)
print(l_sorted)
# [1, 2, 3, 4, 5]

print(l)
# [3, 1, 4, 5, 2]

l_reverse_sorted = sorted(l, reverse=True)
print(l_reverse_sorted)
# [5, 4, 3, 2, 1]

print(l)
# [3, 1, 4, 5, 2]

l = [-3, 1, 4, -5, 2]
print(sorted(l))
# [-5, -3, 1, 2, 4]

print(sorted(l, key=abs))
# [1, 2, -3, 4, -5]

l = ['b', 'cc', 'aaa']
print(sorted(l))
# ['aaa', 'b', 'cc']

print(sorted(l, key=len))
# ['b', 'cc', 'aaa']

s = 'cebad'

l_sorted = sorted(s)
print(l_sorted)
# ['a', 'b', 'c', 'd', 'e']

print(s)
# cebad

s_sorted = ''.join(l_sorted)
print(s_sorted)
# abcde

s_sorted = ''.join(sorted(s))
print(s_sorted)
# abcde

s_reverse_sorted = ''.join(sorted(s, reverse=True))
print(s_reverse_sorted)
# edcba

l = ['banana', 'cherry', 'apple']
print(sorted(l))
# ['apple', 'banana', 'cherry']

l.sort()
print(l)
# ['apple', 'banana', 'cherry']

t = (3, 1, 4, 5, 2)

l_sorted = sorted(t)
print(l_sorted)
# [1, 2, 3, 4, 5]

print(t)
# (3, 1, 4, 5, 2)

t_sorted = tuple(l_sorted)
print(t_sorted)
# (1, 2, 3, 4, 5)

t_sorted = tuple(sorted(t))
print(t_sorted)
# (1, 2, 3, 4, 5)

t_reverse_sorted = tuple(sorted(t, reverse=True))
print(t_reverse_sorted)
# (5, 4, 3, 2, 1)
