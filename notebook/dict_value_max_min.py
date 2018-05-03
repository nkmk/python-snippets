d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

max_d = max(d)
print(max_d)
# e

min_d = min(d)
print(min_d)
# a

max_v = max(d.values())
print(max_v)
# 100

min_v = min(d.values())
print(min_v)
# 20

max_k = max(d, key=d.get)
print(max_k)
# a

min_k = min(d, key=d.get)
print(min_k)
# b

max_kv = max(d.items(), key=lambda x: x[1])
print(max_kv)
# ('a', 100)

print(type(max_kv))
# <class 'tuple'>

max_k, max_v = max(d.items(), key=lambda x: x[1])
print(max_k)
# a

print(max_v)
# 100

min_kv = min(d.items(), key=lambda x: x[1])
print(min_kv)
# ('b', 20)

max_kv_list = [kv for kv in d.items() if kv[1] == max(d.values())]
print(max_kv_list)
# [('a', 100), ('d', 100)]

max_k_list = [kv[0] for kv in d.items() if kv[1] == max(d.values())]
print(max_k_list)
# ['a', 'd']

min_kv_list = [kv for kv in d.items() if kv[1] == min(d.values())]
print(min_kv_list)
# [('b', 20)]
