l = [3, 6, 7, -1, 23, -10, 18]

print(max(l))
# 23

print(min(l))
# -10

ld = sorted(l, reverse=True)
print(ld)
# [23, 18, 7, 6, 3, -1, -10]

print(ld[:3])
# [23, 18, 7]

la = sorted(l)
print(la)
# [-10, -1, 3, 6, 7, 18, 23]

print(la[:3])
# [-10, -1, 3]

print(sorted(l, reverse=True)[:3])
# [23, 18, 7]

print(sorted(l)[:3])
# [-10, -1, 3]

print(l)
# [3, 6, 7, -1, 23, -10, 18]

l.sort(reverse=True)
print(l[:3])
# [23, 18, 7]

print(l)
# [23, 18, 7, 6, 3, -1, -10]

l.sort()
print(l[:3])
# [-10, -1, 3]

print(l)
# [-10, -1, 3, 6, 7, 18, 23]
