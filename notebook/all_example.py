print(all([True, True, True]))
# True

print(all([True, False, True]))
# False

print(all((True, True, True)))
# True

print(all({True, True, True}))
# True

print(all([]))
# True

print(all([100, [0, 1, 2], 'abc']))
# True

print(all([100, [0, 1, 2], 'abc', {}]))
# False
