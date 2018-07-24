l = [i**2 for i in range(5)]

print(l)
# [0, 1, 4, 9, 16]

print(type(l))
# <class 'list'>

g = (i**2 for i in range(5))

print(g)
# <generator object <genexpr> at 0x1052154f8>

print(type(g))
# <class 'generator'>

for i in g:
    print(i)
# 0
# 1
# 4
# 9
# 16

g_cells = ((row, col) for row in range(0, 3)
           for col in range(0, 2) if col == row)

print(type(g_cells))
# <class 'generator'>

for i in g_cells:
    print(i)
# (0, 0)
# (1, 1)

print(sum([i**2 for i in range(5)]))
# 30

print(sum((i**2 for i in range(5))))
# 30

print(sum(i**2 for i in range(5)))
# 30
