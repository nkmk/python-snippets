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
#     

print(type(my_func.__doc__))
# <class 'str'>

help(my_func)
# Help on function my_func in module __main__:
# 
# my_func()
#     docstring-test
#     line1
#     line2
#     line3
# 

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
#     

def func_rest(param1, param2):
    """Summary line.
    
    :param param1: Description of param1
    :type param1: int
    :param param2: Description of param2
    :type param2: str
    :returns: Description of return value
    :rtype: bool
    """
    return True

def func_numpy(param1, param2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    param1 : int
        Description of param1
    param2 : str
        Description of param2

    Returns
    -------
    bool
        Description of return value
    """
    return True

def func_google(param1, param2):
    """Summary line.

    Extended description of function.

    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2

    Returns:
        bool: Description of return value

    """
    return True
