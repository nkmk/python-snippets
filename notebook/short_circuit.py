def test():
    print('function is called')
    return True

print(True and test())
# function is called
# True

print(False and test())
# False

print(True or test())
# True

print(False or test())
# function is called
# True
