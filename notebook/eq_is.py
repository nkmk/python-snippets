a = 100
b = 100
c = 200
print(a == b)
# True

print(a == c)
# False

print(a != b)
# False

print(a != c)
# True

print(100 == 100.0)
# True

print(100 == 100 + 0j)
# True

print(1 == True)
# True

print(0.0 == False)
# True

a = 100
b = 100.0
print(a == b)
# True

print(a == b and type(a) == type(b))
# False

print(100 == '100')
# False

print(100 == int('100'))
# True

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
# True

print(l1 is l2)
# False

l3 = l1
print(l1 is l3)
# True

l1[0] = 100
print(l1)
# [100, 2, 3]

print(l2)
# [1, 2, 3]

print(l3)
# [100, 2, 3]

print(l1 is not l2)
# True

print(l1 is not l3)
# False

print(id(l1))
# 4388188480

print(id(l2))
# 4388187456

print(id(l3))
# 4388188480

a = 256
b = 256
print(a is b)
# True

a = 257
b = 257
print(a is b)
# False

a = 'abc_123'
b = 'abc_123'
print(a is b)
# True

a = 'abc_123?'
b = 'abc_123?'
print(a is b)
# False

a, b = 257, 257
print(a is b)
# True

a, b = 'abc_123?', 'abc_123?'
print(a is b)
# True

class MyClass:
    def __eq__(self, other):
        return '__eq__'

    def __ne__(self, other):
        return '__ne__'

my_obj = MyClass()
print(my_obj == 100)
# __eq__

print(my_obj != 100)
# __ne__

a = None
print(a is None)
# True

print(a is not None)
# False

class MyClass:
    def __eq__(self, other):
        return True

my_obj = MyClass()
print(my_obj == None)
# True

print(my_obj is None)
# False
