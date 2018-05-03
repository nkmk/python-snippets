d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4, 'd': 5}

print(list(d1.keys()))
# ['a', 'b', 'c']

print(type(d1.keys()))
# <class 'dict_keys'>

print(list(d1.items()))
# [('a', 1), ('b', 2), ('c', 3)]

print(type(d1.items()))
# <class 'dict_items'>

intersection_keys = d1.keys() & d2.keys()
print(intersection_keys)
# {'c', 'b'}

print(type(intersection_keys))
# <class 'set'>

intersection_items = d1.items() & d2.items()
print(intersection_items)
# {('b', 2)}

intersection_dict = dict(d1.items() & d2.items())
print(intersection_dict)
# {'b': 2}

print(type(intersection_dict))
# <class 'dict'>

union_keys = d1.keys() | d2.keys()
print(union_keys)
# {'d', 'a', 'b', 'c'}

union_items = d1.items() | d2.items()
print(union_items)
# {('d', 5), ('c', 4), ('a', 1), ('b', 2), ('c', 3)}

union_dict = dict(d1.items() | d2.items())
print(union_dict)
# {'d': 5, 'c': 3, 'a': 1, 'b': 2}

symmetric_difference_keys = d1.keys() ^ d2.keys()
print(symmetric_difference_keys)
# {'d', 'a'}

symmetric_difference_items = d1.items() ^ d2.items()
print(symmetric_difference_items)
# {('d', 5), ('c', 4), ('a', 1), ('c', 3)}

symmetric_difference_dict = dict(d1.items() ^ d2.items())
print(symmetric_difference_dict)
# {'d': 5, 'c': 3, 'a': 1}

difference_keys = d1.keys() - d2.keys()
print(difference_keys)
# {'a'}

difference_items = d1.items() - d2.items()
print(difference_items)
# {('c', 3), ('a', 1)}

difference_dict = dict(d1.items() - d2.items())
print(difference_dict)
# {'c': 3, 'a': 1}
