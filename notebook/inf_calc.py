print(float('inf') + 100)
# inf

print(float('inf') + float('inf'))
# inf

print(float('inf') - 100)
# inf

print(float('inf') - float('inf'))
# nan

print(type(float('inf') - float('inf')))
# <class 'float'>

print(float('inf') * 2)
# inf

print(float('inf') * float('inf'))
# inf

print(float('inf') * 0)
# nan

print(float('inf') / 2)
# inf

print(float('inf') / float('inf'))
# nan

print(0 / float('inf'))
# 0.0

# print(float('inf') / 0)
# ZeroDivisionError: float division by zero

print(float('inf') ** 2)
# inf

print(float('inf') ** float('inf'))
# inf

print(float('inf') ** 0)
# 1.0

print(2 ** float('inf'))
# inf

print(1 ** float('inf'))
# 1.0

print(0 ** float('inf'))
# 0.0
