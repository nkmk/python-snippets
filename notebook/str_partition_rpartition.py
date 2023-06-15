s = 'abc@xyz'
print(s.partition('@'))
# ('abc', '@', 'xyz')

print(type(s.partition('@')))
# <class 'tuple'>

print(s.partition('123'))
# ('abc@xyz', '', '')

print(s.partition('abc'))
# ('', 'abc', '@xyz')

print(s.partition('xyz'))
# ('abc@', 'xyz', '')

s = 'abc@xyz@123'
print(s.partition('@'))
# ('abc', '@', 'xyz@123')

print(s.rpartition('@'))
# ('abc@xyz', '@', '123')
