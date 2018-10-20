print(bool('True'))
print(bool('False'))
print(bool('abc'))
# True
# True
# True

print(bool(''))
# False

print(bool(1))
print(bool(2))
print(bool(1.23))
print(bool(-1))
# True
# True
# True
# True

print(bool(0))
print(bool(0.0))
print(bool(0j))
# False
# False
# False

print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool({1, 2, 3}))
print(bool({'k1': 1, 'k2':2, 'k3': 3}))
# True
# True
# True
# True

print(bool([]))
print(bool(()))
print(bool({}))
# False
# False
# False

print(bool(None))
# False
