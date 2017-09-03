# http://www.unicode.org
# http://www.unicode.org/charts/
# https://docs.python.jp/3/howto/unicode.html

import unicodedata

s = 'あ'
print(unicodedata.name(s))
# HIRAGANA LETTER A

name = 'grinning face'
value = unicodedata.lookup(name)
print(value)
print(type(value))
# 😀
# <class 'str'>

print('\N{grinning face}')
# 😀

u8 = value.encode('utf-8')
print(u8)
print(type(u8))
# b'\xf0\x9f\x98\x80'
# <class 'bytes'>

ue = value.encode('unicode-escape')
print(ue)
print(type(ue))
# b'\\U0001f600'
# <class 'bytes'>

emoji = '\U0001f600'
print(emoji)
# 😀

emoji_2 = '\U0001f601'
print(emoji_2)
# 😁

print(unicodedata.name(emoji_2))
# GRINNING FACE WITH SMILING EYES

u8_2 = emoji_2.encode('utf-8')
print(u8_2)
print(type(u8_2))
# b'\xf0\x9f\x98\x81'
# <class 'bytes'>
