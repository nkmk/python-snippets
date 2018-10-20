print(any([True, False, False]))
# True

print(any([False, False, False]))
# False

print(any((True, False, False)))
# True

print(any({True, False, False}))
# True

print(any([]))
# False

print(any([False, None, 0, 0.0, 0 + 0j, '', [], {}, ()]))
# False

print(any([False, None, 0, 0.0, 0 + 0j, '', [], {}, (), 1]))
# True

print(not any([False, False, False]))
# True

print(not any([True, False, False]))
# False
