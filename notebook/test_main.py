import test_module

print('This is test_main.py')
print('test_module.__name__ is', test_module.__name__)

print('---')
print('call test_module.func()')

test_module.func()
