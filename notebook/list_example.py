l = ['apple', 100, 0.123]
print(l)
# ['apple', 100, 0.123]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(l[1])
# 100

print(l_2d[1])
# [3, 4, 5]

print(l_2d[1][1])
# 4

print(l[:2])
# ['apple', 100]

l_num = [0, 10, 20, 30]

print(min(l_num))
# 0

print(max(l_num))
# 30

print(sum(l_num))
# 60

print(sum(l_num) / len(l_num))
# 15.0

l_str = ['apple', 'orange', 'banana']

for s in l_str:
    print(s)
# apple
# orange
# banana
