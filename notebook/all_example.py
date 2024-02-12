print(all([True, True, True]))
# True

print(all([True, False, True]))
# False

print(all((True, True, True)))
# True

print(all({True, True, True}))
# True

print(all(['aaa', 'bbb', 'ccc']))
# True

print(all(['aaa', 'bbb', 'ccc', '']))
# False

print(all([1, 2, 3]))
# True

print(all([0, 1, 2, 3]))
# False

print(all([]))
# True
