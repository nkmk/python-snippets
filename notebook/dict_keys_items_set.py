d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4, 'd': 5}

print(d1.keys())
# dict_keys(['a', 'b', 'c'])

print(type(d1.keys()))
# <class 'dict_keys'>

print(d1.items())
# dict_items([('a', 1), ('b', 2), ('c', 3)])

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
# {'d', 'c', 'a', 'b'}

union_items = d1.items() | d2.items()
print(union_items)
# {('b', 2), ('a', 1), ('c', 4), ('d', 5), ('c', 3)}

union_dict = dict(d1.items() | d2.items())
print(union_dict)
# {'b': 2, 'a': 1, 'c': 3, 'd': 5}

print(d1 | d2)
# {'a': 1, 'b': 2, 'c': 4, 'd': 5}

print(d2 | d1)
# {'b': 2, 'c': 3, 'd': 5, 'a': 1}

symmetric_difference_keys = d1.keys() ^ d2.keys()
print(symmetric_difference_keys)
# {'d', 'a'}

symmetric_difference_items = d1.items() ^ d2.items()
print(symmetric_difference_items)
# {('d', 5), ('a', 1), ('c', 3), ('c', 4)}

symmetric_difference_dict = dict(d1.items() ^ d2.items())
print(symmetric_difference_dict)
# {'d': 5, 'a': 1, 'c': 4}

difference_keys = d1.keys() - d2.keys()
print(difference_keys)
# {'a'}

difference_items = d1.items() - d2.items()
print(difference_items)
# {('a', 1), ('c', 3)}

difference_dict = dict(d1.items() - d2.items())
print(difference_dict)
# {'a': 1, 'c': 3}
