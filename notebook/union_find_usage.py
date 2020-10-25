from union_find import UnionFind, UnionFindLabel

uf = UnionFind(6)
print(uf.parents)
# [-1, -1, -1, -1, -1, -1]

print(uf)
# 0: [0]
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]

uf.union(0, 2)
print(uf.parents)
# [-2, -1, 0, -1, -1, -1]

print(uf)
# 0: [0, 2]
# 1: [1]
# 3: [3]
# 4: [4]
# 5: [5]

uf.union(1, 3)
print(uf.parents)
uf.union(4, 5)
print(uf.parents)
uf.union(1, 4)
print(uf.parents)
# [-2, -2, 0, 1, -1, -1]
# [-2, -2, 0, 1, -2, 4]
# [-2, -4, 0, 1, 1, 4]

print(uf)
# 0: [0, 2]
# 1: [1, 3, 4, 5]

print(uf.parents)
# [-2, -4, 0, 1, 1, 1]

print(uf.find(0))
# 0

print(uf.find(5))
# 1

print(uf.size(0))
# 2

print(uf.size(5))
# 4

print(uf.same(0, 2))
# True

print(uf.same(0, 5))
# False

print(uf.members(0))
# [0, 2]

print(uf.members(5))
# [1, 3, 4, 5]

print(uf.roots())
# [0, 1]

print(uf.group_count())
# 2

print(uf.all_group_members())
# defaultdict(<class 'list'>, {0: [0, 2], 1: [1, 3, 4, 5]})

print(list(uf.all_group_members().values()))
# [[0, 2], [1, 3, 4, 5]]

l = ['A', 'B', 'C', 'D', 'E']

d = {x: i for i, x in enumerate(l)}
print(d)
# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

d_inv = {i: x for i, x in enumerate(l)}
print(d_inv)
# {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

uf_s = UnionFind(len(l))
print(uf_s)
# 0: [0]
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]

uf_s.union(d['A'], d['D'])
uf_s.union(d['D'], d['C'])
uf_s.union(d['E'], d['B'])
print(uf_s)
# 0: [0, 2, 3]
# 4: [1, 4]

print(d_inv[uf_s.find(d['D'])])
# A

print(uf_s.size(d['D']))
# 3

print(uf_s.same(d['A'], d['D']))
# True

print([d_inv[i] for i in uf_s.members(d['D'])])
# ['A', 'C', 'D']

print([d_inv[i] for i in uf_s.roots()])
# ['A', 'E']

print(uf_s.group_count())
# 2

l = ['A', 'B', 'C', 'D', 'E']

ufl = UnionFindLabel(l)
print(ufl)
# A: ['A']
# B: ['B']
# C: ['C']
# D: ['D']
# E: ['E']

ufl.union('A', 'D')
ufl.union('D', 'C')
ufl.union('E', 'B')
print(ufl)
# A: ['A', 'C', 'D']
# E: ['B', 'E']

print(ufl.find_label('D'))
# A

print(ufl.size('D'))
# 3

print(ufl.same('A', 'D'))
# True

print(ufl.members('D'))
# ['A', 'C', 'D']

print(ufl.roots())
# ['A', 'E']

print(ufl.group_count())
# 2

print(ufl.all_group_members())
# defaultdict(<class 'list'>, {'A': ['A', 'C', 'D'], 'E': ['B', 'E']})

ufl_n = UnionFindLabel([1, 2, 3, 4, 5])
print(ufl_n)
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]

ufl_n.union(1, 4)
ufl_n.union(4, 3)
ufl_n.union(5, 2)
print(ufl_n)
# 1: [1, 3, 4]
# 5: [2, 5]

ufl_n2 = UnionFind(6)
print(ufl_n2)
# 0: [0]
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]

ufl_n2.union(1, 4)
ufl_n2.union(4, 3)
ufl_n2.union(5, 2)
print(ufl_n2)
# 0: [0]
# 1: [1, 3, 4]
# 5: [2, 5]

ufl_t = UnionFindLabel([(0, 0), (0, 1), (1, 0), (1, 1)])
print(ufl_t)
# (0, 0): [(0, 0)]
# (0, 1): [(0, 1)]
# (1, 0): [(1, 0)]
# (1, 1): [(1, 1)]

ufl_t.union((0, 1), (1, 0))
ufl_t.union((0, 0), (1, 0))
print(ufl_t)
# (0, 1): [(0, 0), (0, 1), (1, 0)]
# (1, 1): [(1, 1)]

print(ufl_t.same((0, 1), (0, 0)))
# True
