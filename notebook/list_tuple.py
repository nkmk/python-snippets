l = [0, 1, 2]
print(l)
print(type(l))
# [0, 1, 2]
# <class 'list'>

t = ('one', 'two', 'three')
print(t)
print(type(t))
# ('one', 'two', 'three')
# <class 'tuple'>

r = range(10)
print(r)
print(type(r))
# range(0, 10)
# <class 'range'>

tl = list(t)
print(tl)
print(type(tl))
# ['one', 'two', 'three']
# <class 'list'>

rl = list(r)
print(rl)
print(type(rl))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# <class 'list'>

lt = tuple(l)
print(lt)
print(type(lt))
# (0, 1, 2)
# <class 'tuple'>

rt = tuple(r)
print(rt)
print(type(rt))
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# <class 'tuple'>

# t[0] = 'ONE'
# TypeError: 'tuple' object does not support item assignment

tl = list(t)
tl.append('four')
t_new = tuple(tl)
print(t_new)
print(type(t_new))
# ('one', 'two', 'three', 'four')
# <class 'tuple'>

tl = list(t)
tl[0] = 'ONE'
t_new = tuple(tl)
print(t_new)
print(type(t_new))
# ('ONE', 'two', 'three')
# <class 'tuple'>
