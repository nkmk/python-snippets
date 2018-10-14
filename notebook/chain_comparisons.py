x = 15
print(10 < x < 20)
# True

print(10 < x and x < 20)
# True

x = 0
print(10 < x < 20)
# False

print(10 < x and x < 20)
# False

x = 15
y = 25

print(10 < x < 20 < y < 30)
# True

print(10 < x and x < 20 and 20 < y and y < 30)
# True

x = 15
y = 40

print(10 < x < 20 < y < 30)
# False

print(10 < x and x < 20 and 20 < y and y < 30)
# False

def test(x):
    print('function is called')
    return(x)

print(test(15))
# function is called
# 15

print(10 < test(15) < 20)
# function is called
# True

print(10 < test(15) and test(15) < 20)
# function is called
# function is called
# True

print(10 < test(0) < 20)
# function is called
# False

print(10 < test(0) and test(0) < 20)
# function is called
# False

x = 15

if 10 < x < 20:
    print('result: 10 < x < 20')
else:
    print('result: x <= 10 or 20 <= x')
# result: 10 < x < 20

x = 30

if 10 < x < 20:
    print('result: 10 < x < 20')
else:
    print('result: x <= 10 or 20 <= x')
# result: x <= 10 or 20 <= x

a = 10
b = 10
c = 10

if a == b == c:
    print('all equal')
else:
    print('not all equal')
# all equal

a = 10
b = 1
c = 10

if a == b == c:
    print('all equal')
else:
    print('not all equal')
# not all equal

a = 10
b = 1
c = 100

print(a != b != c)
# True

a = 10
b = 10
c = 1

print(a != b != c)
# False

a = 10
b = 1
c = 10

print(a != b != c)
# True

a = 100
l = [0, 10, 100, 1000]

print(50 < a in l)
# True

print(50 < a and a in l)
# True
