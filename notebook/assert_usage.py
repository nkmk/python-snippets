a = 100

assert a == 100

# assert a == 0
# AssertionError: 

assert [0, 1, 2]

# assert []
# AssertionError: 

a = 100

assert a > 0 and a % 2 == 0

# assert a < 0 and a % 2 == 0
# AssertionError: 

a = 100

# assert a == 0, 'a must be 0.'
# AssertionError: a must be 0.

def test1(x):
    print('test1 is called.')
    return x > 0

def test2(x):
    print('test2 is called.')
    return x % 2 == 0

a = -100

# assert test1(a) and test2(a), 'Error Message'
# test1 is called.
# AssertionError: Error Message

# assert test1(a), 'Error Message1'
# assert test2(a), 'Error Message2'
# test1 is called.
# AssertionError: Error Message1

# assert (test1(a), test2(a)) == (True, True), 'Error Message'
# test1 is called.
# test2 is called.
# AssertionError: Error Message
