print(any([True, False, False]))
# True

print(any([False, False, False]))
# False

print(any((True, False, False)))
# True

print(any({True, False, False}))
# True

print(any(['aaa', 'bbb', 'ccc', '']))
# True

print(any(['', '', '', '']))
# False

print(any([0, 1, 2, 3]))
# True

print(any([0, 0, 0, 0]))
# False

print(any([]))
# False

print(not any([False, False, False]))
# True

print(not any([True, False, False]))
# False
