l = [10, 1, 5]

l.sort()
print(l)
# [1, 5, 10]

l = [10, 1, 5]

print(sorted(l))
# [1, 5, 10]

print(l)
# [10, 1, 5]

print(sorted(l, reverse=True))
# [10, 5, 1]

l = ['10', '01', '05']

print(sorted(l))
# ['01', '05', '10']

l = ['10', '1', '5']

print(sorted(l))
# ['1', '10', '5']

l = ['10', '1', '5']

print(sorted(l, key=int))
# ['1', '5', '10']

print(sorted(l, key=float))
# ['1', '5', '10']

l = ['10.0', '1.0', '5.0']

print(sorted(l, key=float))
# ['1.0', '5.0', '10.0']

l = ['10', '1', '5']

l.sort(key=int)
print(l)
# ['1', '5', '10']

l = ['10', '1', '5']

print([int(s) for s in l])
# [10, 1, 5]

print(sorted([int(s) for s in l]))
# [1, 5, 10]
