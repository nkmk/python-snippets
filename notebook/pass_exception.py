def divide(a, b):
    print(a / b)

# divide(1, 0)
# ZeroDivisionError: division by zero

def divide_exception(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('ZeroDivisionError: ', e)

divide_exception(1, 0)
# ZeroDivisionError:  division by zero

def divide_exception_pass(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        pass

divide_exception_pass(1, 0)
