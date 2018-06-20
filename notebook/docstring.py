def my_func():
    """docstring-test
    line1
    line2
    line3
    """

print(my_func.__doc__)
# docstring-test
#     line1
#     line2
#     line3

print(type(my_func.__doc__))
# <class 'str'>

help(my_func)
# Help on function my_func in module __main__:
# my_func()
#     docstring-test
#     line1
#     line2
#     line3

def my_func2():
    'docstring-test'

print(my_func2.__doc__)
# docstring-test

def my_func_error():
    a = 100
    """docstring-test
    line1
    line2
    line3
    """

print(my_func_error.__doc__)
# None

class MyClass:
    """docstring-test
    line1
    line2
    line3
    """

print(MyClass.__doc__)
# docstring-test
#     line1
#     line2
#     line3

def func_rest(arg1, arg2):
    """Summary line.
    
    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :returns: Description of return value
    :rtype: bool
    """
    return True

def func_numpy(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value
    """
    return True

def func_google(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True
