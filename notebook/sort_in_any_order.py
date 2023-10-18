l = ['Banana', 'Alice', 'Apple', 'Bob']

print(sorted(l))
# ['Alice', 'Apple', 'Banana', 'Bob']

print(sorted(l, reverse=True))
# ['Bob', 'Banana', 'Apple', 'Alice']

print(sorted(l, key=len))
# ['Bob', 'Alice', 'Apple', 'Banana']

l = ['Bob', 'Banana', 'Alice', 'Apple', 'Bob', 'Apple']
l_order = ['Alice', 'Bob', 'Apple', 'Banana']

print(sorted(l, key=l_order.index))
# ['Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana']

l = ['Bob', 'Banana', 'Alice', 'Apple', 'Bob', 'Apple']
d_order = {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3}

print(sorted(l, key=lambda x: d_order[x]))
# ['Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana']

l_order = ['Alice', 'Bob', 'Apple', 'Banana']

d_order = {x: i for i, x in enumerate(l_order)}
print(d_order)
# {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3}

l = ['Bob', 'Banana', 'Alice', 'Apple', 'Bob', 'Apple', 'xxx']
l_order = ['Alice', 'Bob', 'Apple', 'Banana']

# print(sorted(l, key=l_order.index))
# ValueError: 'xxx' is not in list

print(sorted(l, key=lambda x: l_order.index(x) if x in l_order else -1))
# ['xxx', 'Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana']

print(sorted(l, key=lambda x: l_order.index(x) if x in l_order else float('inf')))
# ['Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana', 'xxx']

l = ['Bob', 'Banana', 'Alice', 'Apple', 'Bob', 'Apple']
l_order = ['Alice', 'Bob', 'Apple', 'Banana', 'xxx']

print(sorted(l, key=l_order.index))
# ['Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana']

l = ['Bob', 'Banana', 'Alice', 'Apple', 'Bob', 'Apple', 'xxx']
d_order = {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3}

# print(sorted(l, key=lambda x: d_order[x]))
# KeyError: 'xxx'

print(sorted(l, key=lambda x: d_order.get(x, -1)))
# ['xxx', 'Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana']

print(sorted(l, key=lambda x: d_order.get(x, float('inf'))))
# ['Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana', 'xxx']

l = ['Bob', 'Banana', 'Alice', 'Apple', 'Bob', 'Apple']
d_order = {'Alice': 0, 'Bob': 1, 'Apple': 2, 'Banana': 3, 'xxx': 4}

print(sorted(l, key=lambda x: d_order[x]))
# ['Alice', 'Bob', 'Bob', 'Apple', 'Apple', 'Banana']
