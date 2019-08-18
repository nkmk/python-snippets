from union_find_basic import UnionFindBasic, UnionFindPathCompression, UnionFindByRank, UnionFindBySize, UnionFind

ufb = UnionFindBasic(5)
print(ufb.parents)
# [0, 1, 2, 3, 4]

ufb.union(3, 4)
print(ufb.parents)
ufb.union(2, 3)
print(ufb.parents)
ufb.union(1, 2)
print(ufb.parents)
ufb.union(0, 4)
print(ufb.parents)
# [0, 1, 2, 3, 3]
# [0, 1, 2, 2, 3]
# [0, 1, 1, 2, 3]
# [0, 0, 1, 2, 3]

print([ufb.find(i) for i in range(5)])
# [0, 0, 0, 0, 0]

ufpc = UnionFindPathCompression(5)
print(ufpc.parents)
# [0, 1, 2, 3, 4]

ufpc.union(3, 4)
print(ufpc.parents)
ufpc.union(2, 3)
print(ufpc.parents)
ufpc.union(1, 2)
print(ufpc.parents)
ufpc.union(0, 4)
print(ufpc.parents)
# [0, 1, 2, 3, 3]
# [0, 1, 2, 2, 3]
# [0, 1, 1, 2, 3]
# [0, 0, 1, 1, 1]

print([ufpc.find(i) for i in range(5)])
# [0, 0, 0, 0, 0]

ufbr = UnionFindByRank(5)
print(ufbr.parents)
# [0, 1, 2, 3, 4]

ufbr.union(3, 4)
print(ufbr.parents)
ufbr.union(2, 3)
print(ufbr.parents)
ufbr.union(1, 2)
print(ufbr.parents)
ufbr.union(0, 4)
print(ufbr.parents)
# [0, 1, 2, 3, 3]
# [0, 1, 3, 3, 3]
# [0, 3, 3, 3, 3]
# [3, 3, 3, 3, 3]

ufbs = UnionFindBySize(5)
print(ufbs.parents)
# [0, 1, 2, 3, 4]

ufbs.union(3, 4)
print(ufbs.parents)
ufbs.union(2, 3)
print(ufbs.parents)
ufbs.union(1, 2)
print(ufbs.parents)
ufbs.union(0, 4)
print(ufbs.parents)
# [0, 1, 2, 3, 3]
# [0, 1, 3, 3, 3]
# [0, 3, 3, 3, 3]
# [3, 3, 3, 3, 3]

print(ufbs.size)
# [1, 1, 1, 5, 1]

print(ufbs.size[ufbs.find(0)])
# 5

uf = UnionFind(5)
print(uf.parents)
# [-1, -1, -1, -1, -1]

uf.union(3, 4)
print(uf.parents)
uf.union(2, 3)
print(uf.parents)
uf.union(1, 2)
print(uf.parents)
uf.union(0, 4)
print(uf.parents)
# [-1, -1, -1, -2, 3]
# [-1, -1, 3, -3, 3]
# [-1, 3, 3, -4, 3]
# [3, 3, 3, -5, 3]
