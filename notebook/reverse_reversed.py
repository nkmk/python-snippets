l = [1, 2, 3, 4, 5]

l.reverse()
print(l)
# [5, 4, 3, 2, 1]

print(l.reverse())
# None

l = [1, 2, 3, 4, 5]

print(type(reversed(l)))
# <class 'list_reverseiterator'>

print(l)
# [1, 2, 3, 4, 5]

for i in reversed(l):
    print(i)
# 5
# 4
# 3
# 2
# 1

l_reversed = list(reversed(l))
print(l_reversed)
# [5, 4, 3, 2, 1]

print(l)
# [1, 2, 3, 4, 5]

l = [1, 2, 3, 4, 5]

l_reversed = l[::-1]
print(l_reversed)
# [5, 4, 3, 2, 1]

print(l)
# [1, 2, 3, 4, 5]

s = 'abcde'

s_reversed_list = list(reversed(s))
print(s_reversed_list)
# ['e', 'd', 'c', 'b', 'a']

s_reversed = ''.join(list(reversed(s)))
print(s_reversed)
# edcba

s_reversed = s[::-1]
print(s_reversed)
# edcba

t = (1, 2, 3, 4, 5)

t_reversed = tuple(reversed(t))
print(t_reversed)
# (5, 4, 3, 2, 1)

t_reversed = t[::-1]
print(t_reversed)
# (5, 4, 3, 2, 1)
