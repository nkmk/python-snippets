import itertools

l1 = [1, 2, 3]
l2 = [10, 20, 30]

for i, j in itertools.product(l1, l2):
    print(i, j)
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# 2 30
# 3 10
# 3 20
# 3 30

for i, j in itertools.product(l1, l2):
    print(i, j)
    if i == 2 and j == 20:
        print('BREAK')
        break
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# BREAK

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

for i, j, k in itertools.product(l1, l2, l3):
    print(i, j, k)
    if i == 2 and j == 20 and k == 200:
        print('BREAK')
        break
# 1 10 100
# 1 10 200
# 1 10 300
# 1 20 100
# 1 20 200
# 1 20 300
# 1 30 100
# 1 30 200
# 1 30 300
# 2 10 100
# 2 10 200
# 2 10 300
# 2 20 100
# 2 20 200
# BREAK

for i, j in itertools.product(l1, l2):
    x = i * 2 + j * 3
    print(i, j, x)
# 1 10 32
# 1 20 62
# 1 30 92
# 2 10 34
# 2 20 64
# 2 30 94
# 3 10 36
# 3 20 66
# 3 30 96

for i in l1:
    temp = i * 2
    for j in l2:
        x = temp + j * 3
        print(i, j, x)
# 1 10 32
# 1 20 62
# 1 30 92
# 2 10 34
# 2 20 64
# 2 30 94
# 3 10 36
# 3 20 66
# 3 30 96
