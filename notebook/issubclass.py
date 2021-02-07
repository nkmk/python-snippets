print(issubclass(bool, int))
# True

print(issubclass(bool, float))
# False

print(issubclass(bool, bool))
# True

print(issubclass(bool, (int, float)))
# True

print(issubclass(bool, (str, float)))
# False

print(issubclass(ZeroDivisionError, ArithmeticError))
# True

print(issubclass(ZeroDivisionError, Exception))
# True

print(issubclass(ZeroDivisionError, BaseException))
# True

# print(issubclass(True, int))
# TypeError: issubclass() arg 1 must be a class

print(issubclass(type(True), int))
# True

print(isinstance(True, bool))
# True

print(isinstance(True, int))
# True

print(isinstance(True, float))
# False

print(isinstance(True, (int, float)))
# True
