import copy

l = [0, 1, [2, 3]]
l_assign = l                   # assignment
l_copy = l.copy()              # shallow copy
l_deepcopy = copy.deepcopy(l)  # deep copy

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_assign)
# [0, 100, [200, 3]]

print(l_copy)
# [0, 1, [200, 3]]

print(l_deepcopy)
# [0, 1, [2, 3]]

l1 = [0, 1, [2, 3]]
l2 = l1

print(l1 is l2)
# True

l1[1] = 100
l1[2][0] = 200
print(l1)
# [0, 100, [200, 3]]

print(l2)
# [0, 100, [200, 3]]

print(l1 is l2)
# True

i1 = 1
i2 = i1

print(i1 is i2)
# True

i1 += 100
print(i1)
# 101

print(i2)
# 1

print(i1 is i2)
# False

l = [0, 1, [2, 3]]
l_copy = l.copy()

print(l is l_copy)
# False

print(l[2] is l_copy[2])
# True

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_copy)
# [0, 1, [200, 3]]

print(l[2] is l_copy[2])
# True

l = [0, 1, [2, 3]]
l_slice = l[:]

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_slice)
# [0, 1, [200, 3]]

l = [0, 1, [2, 3]]
l_list = list(l)

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_list)
# [0, 1, [200, 3]]

l = [0, 1, [2, 3]]
l_copy = copy.copy(l)

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_copy)
# [0, 1, [200, 3]]

l = [0, 1, [2, 3]]
l_deepcopy = copy.deepcopy(l)

print(l is l_deepcopy)
# False

print(l[2] is l_deepcopy[2])
# False

l[1] = 100
l[2][0] = 200
print(l)
# [0, 100, [200, 3]]

print(l_deepcopy)
# [0, 1, [2, 3]]
