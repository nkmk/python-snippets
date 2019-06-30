l = ['Banana', 'Alice', 'Apple', 'Bob']

print(sorted(l))
# ['Alice', 'Apple', 'Banana', 'Bob']

print(sorted(l, reverse=True))
# ['Bob', 'Banana', 'Apple', 'Alice']

l_order = ['Alice', 'Bob', 'Apple', 'Banana']

print(sorted(l, key=l_order.index))
# ['Alice', 'Bob', 'Apple', 'Banana']

print(l)
# ['Banana', 'Alice', 'Apple', 'Bob']

print([l_order.index(s) for s in l])
# [3, 0, 2, 1]

print(sorted(l, key=l_order.index))
# ['Alice', 'Bob', 'Apple', 'Banana']

d_order = {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3}

print(sorted(l, key=lambda x: d_order[x]))
# ['Alice', 'Bob', 'Apple', 'Banana']

l = ['Banana', 'Alice', 'Apple', 'Bob', 'xxx']
l_order = ['Alice', 'Bob', 'Apple', 'Banana']

# print(sorted(l, key=l_order.index))
# ValueError: 'xxx' is not in list

print(sorted(l, key=lambda x: l_order.index(x) if x in l_order else -1))
# ['xxx', 'Alice', 'Bob', 'Apple', 'Banana']

print(sorted(l, key=lambda x: l_order.index(x) if x in l_order else float('inf')))
# ['Alice', 'Bob', 'Apple', 'Banana', 'xxx']

def my_index(x):
    l_order = ['Alice', 'Bob', 'Apple', 'Banana']
    return l_order.index(x) if x in l_order else -1

print(sorted(l, key=my_index))
# ['xxx', 'Alice', 'Bob', 'Apple', 'Banana']

l = ['Banana', 'Alice', 'Apple', 'Bob']
l_order = ['Alice', 'Bob', 'Apple', 'Banana', 'xxx']

print(sorted(l, key=l_order.index))
# ['Alice', 'Bob', 'Apple', 'Banana']

l = ['Banana', 'Alice', 'Apple', 'Bob', 'xxx']
d_order = {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3}

# print(sorted(l, key=lambda x: d_order[x]))
# KeyError: 'xxx'

print(sorted(l, key=lambda x: d_order.get(x, -1)))
# ['xxx', 'Alice', 'Bob', 'Apple', 'Banana']

print(sorted(l, key=lambda x: d_order.get(x, float('inf'))))
# ['Alice', 'Bob', 'Apple', 'Banana', 'xxx']

l = ['Banana', 'Alice', 'Apple', 'Bob']
d_order = {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3, 'xxx': 4}

print(sorted(l, key=lambda x: d_order[x]))
# ['Alice', 'Bob', 'Apple', 'Banana']
