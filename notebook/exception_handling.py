# print(1 / 0)
# ZeroDivisionError: division by zero

try:
    print(1 / 0)
except ZeroDivisionError:
    print('Error')
# Error

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)
    print(type(e))
# division by zero
# <class 'ZeroDivisionError'>

print(issubclass(ZeroDivisionError, ArithmeticError))
# True

try:
    print(1 / 0)
except ArithmeticError as e:
    print(e)
    print(type(e))
# division by zero
# <class 'ZeroDivisionError'>

try:
    for i in [-2, -1, 0, 1, 2]:
        print(1 / i)
except ZeroDivisionError as e:
    print(e)
# -0.5
# -1.0
# division by zero

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)

divide(1, 0)
# catch ZeroDivisionError: division by zero

# divide('a', 'b')
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

def divide_each(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    except TypeError as e:
        print('catch TypeError:', e)

divide_each(1, 0)
# catch ZeroDivisionError: division by zero

divide_each('a', 'b')
# catch TypeError: unsupported operand type(s) for /: 'str' and 'str'

def divide_same(a, b):
    try:
        print(a / b)
    except (ZeroDivisionError, TypeError) as e:
        print(e)

divide_same(1, 0)
# division by zero

divide_same('a', 'b')
# unsupported operand type(s) for /: 'str' and 'str'

def divide_wildcard(a, b):
    try:
        print(a / b)
    except:
        print('Error')

divide_wildcard(1, 0)
# Error

divide_wildcard('a', 'b')
# Error

def divide_exception(a, b):
    try:
        print(a / b)
    except Exception as e:
        print(e)

divide_exception(1, 0)
# division by zero

divide_exception('a', 'b')
# unsupported operand type(s) for /: 'str' and 'str'

def divide_else(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    else:
        print('finish (no error)')

divide_else(1, 2)
# 0.5
# finish (no error)

divide_else(1, 0)
# catch ZeroDivisionError: division by zero

def divide_finally(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    finally:
        print('all finish')

divide_finally(1, 2)
# 0.5
# all finish

divide_finally(1, 0)
# catch ZeroDivisionError: division by zero
# all finish

def divide_else_finally(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    else:
        print('finish (no error)')
    finally:
        print('all finish')

divide_else_finally(1, 2)
# 0.5
# finish (no error)
# all finish

divide_else_finally(1, 0)
# catch ZeroDivisionError: division by zero
# all finish

def divide_pass(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        pass

divide_pass(1, 0)
