from setuptools._distutils.util import strtobool

print(strtobool('true'))
print(strtobool('True'))
print(strtobool('TRUE'))
# True
# True
# True

print(strtobool('t'))
print(strtobool('yes'))
print(strtobool('y'))
print(strtobool('on'))
print(strtobool('1'))
# True
# True
# True
# True
# True

print(strtobool('false'))
print(strtobool('False'))
print(strtobool('FALSE'))
# False
# False
# False

print(strtobool('f'))
print(strtobool('no'))
print(strtobool('n'))
print(strtobool('off'))
print(strtobool('0'))
# False
# False
# False
# False
# False

# print(strtobool('abc'))
# ValueError: invalid truth value 'abc'

try:
    strtobool('abc')
except ValueError as e:
    print(e)
# invalid truth value 'abc'
