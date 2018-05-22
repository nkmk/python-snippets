path = 'data/src/sample_for_grep.txt'

with open(path) as f:
    print(f.read())
# XXX YYY ZZZ
# YYY
# aaa
# XXX
# ZZZ XXX
# xxx

with open(path) as f:
    lines = f.readlines()

print(lines)
# ['XXX YYY ZZZ\n', 'YYY\n', 'aaa\n', 'XXX\n', 'ZZZ XXX\n', 'xxx']

print(type(lines))
# <class 'list'>

lines_strip = [line.strip() for line in lines]
print(lines_strip)
# ['XXX YYY ZZZ', 'YYY', 'aaa', 'XXX', 'ZZZ XXX', 'xxx']

l_XXX = [line for line in lines_strip if 'XXX' in line]
print(l_XXX)
# ['XXX YYY ZZZ', 'XXX', 'ZZZ XXX']

for line in l_XXX:
    print(line)
# XXX YYY ZZZ
# XXX
# ZZZ XXX

print(l_XXX[0])
# XXX YYY ZZZ

print(l_XXX[-1])
# ZZZ XXX

l_XXX_start = [line for line in lines_strip if line.startswith('XXX')]
print(l_XXX_start)
# ['XXX YYY ZZZ', 'XXX']

l_XXX_ZZZ_and = [line for line in lines_strip if ('XXX' in line) and ('ZZZ' in line)]
print(l_XXX_ZZZ_and)
# ['XXX YYY ZZZ', 'ZZZ XXX']

l_XXX_xxx = [line for line in lines_strip if 'xxx' in line.lower()]
print(l_XXX_xxx)
# ['XXX YYY ZZZ', 'XXX', 'ZZZ XXX', 'xxx']

l_XXX_i = [i for i, line in enumerate(lines_strip) if 'XXX' in line]
print(l_XXX_i)
# [0, 3, 4]

l_XXX_both = [(i, line) for i, line in enumerate(lines_strip) if 'XXX' in line]
print(l_XXX_both)
# [(0, 'XXX YYY ZZZ'), (3, 'XXX'), (4, 'ZZZ XXX')]

l_i, l_str = list(zip(*l_XXX_both))

print(l_i)
# (0, 3, 4)

print(l_str)
# ('XXX YYY ZZZ', 'XXX', 'ZZZ XXX')

with open(path) as f:
    for i, line in enumerate(f):
        if 'aaa' in line:
            break

print(i)
# 2

print(line)
# aaa

with open(path) as f:
    for i, line in enumerate(f):
        if line == 'ZZZ XXX\n':
            break

print(i)
# 4

print(line)
# ZZZ XXX
