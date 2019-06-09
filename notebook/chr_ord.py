i = ord('A')
print(i)
# 65

print(type(i))
# <class 'int'>

# ord('abc')
# TypeError: ord() expected a character, but string of length 3 found

s = hex(i)
print(s)
# 0x41

print(type(s))
# <class 'str'>

print(format(i, '04x'))
# 0041

print(format(i, '#06x'))
# 0x0041

print(format(ord('X'), '#08x'))
# 0x000058

print(format(ord('💯'), '#08x'))
# 0x01f4af

# ord('🇯🇵')
# TypeError: ord() expected a character, but string of length 2 found

print(len('🇯🇵'))
# 2

print(chr(65))
# A

print(type(chr(65)))
# <class 'str'>

print(65 == 0x41)
# True

print(chr(0x41))
# A

print(chr(0x000041))
# A

s = '0x0041'

print(int(s, 16))
# 65

print(chr(int(s, 16)))
# A

s = 'U+0041'

print(s[2:])
# 0041

print(chr(int(s[2:], 16)))
# A

print('\x41')
# A

print('\u0041')
# A

print('\U00000041')
# A

print('\U0001f4af')
# 💯

# print('\u041')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-4: truncated \uXXXX escape

# print('\U0000041')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-8: truncated \UXXXXXXXX escape

print('\u0041\u0042\u0043')
# ABC

print(len('\u0041\u0042\u0043'))
# 3

print(r'\u0041\u0042\u0043')
# \u0041\u0042\u0043

print(len(r'\u0041\u0042\u0043'))
# 18
