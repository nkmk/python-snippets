import unicodedata

print(unicodedata.numeric('五'))
print(type(unicodedata.numeric('五')))
# 5.0
# <class 'float'>

print(unicodedata.numeric('十'))
# 10.0

print(unicodedata.numeric('参'))
# 3.0

print(unicodedata.numeric('億'))
# 100000000.0

# print(unicodedata.numeric('五十'))
# TypeError: numeric() argument 1 must be a unicode character, not str

# print(unicodedata.numeric('漢'))
# ValueError: not a numeric character
