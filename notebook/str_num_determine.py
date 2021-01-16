s = '1234567890'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = 1234567890
# isdecimal: True
# isdigit: True
# isnumeric: True

s = '１２３４５６７８９０'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = １２３４５６７８９０
# isdecimal: True
# isdigit: True
# isnumeric: True

s = '-1.23'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = -1.23
# isdecimal: False
# isdigit: False
# isnumeric: False

s = '10\u00B2'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = 10²
# isdecimal: False
# isdigit: True
# isnumeric: True

s = '\u00BD'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = ½
# isdecimal: False
# isdigit: False
# isnumeric: True

s = '\u2166'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = Ⅶ
# isdecimal: False
# isdigit: False
# isnumeric: True

s = '一二三四五六七八九〇'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = 一二三四五六七八九〇
# isdecimal: False
# isdigit: False
# isnumeric: True

s = '壱億参阡萬'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = 壱億参阡萬
# isdecimal: False
# isdigit: False
# isnumeric: True

s = 'abc'
print('s =', s)
print('isalpha:', s.isalpha())
# s = abc
# isalpha: True

s = 'あいうえお'
print('s =', s)
print('isalpha:', s.isalpha())
# s = あいうえお
# isalpha: True

s = 'アイウエオ'
print('s =', s)
print('isalpha:', s.isalpha())
# s = アイウエオ
# isalpha: True

s = '漢字'
print('s =', s)
print('isalpha:', s.isalpha())
# s = 漢字
# isalpha: True

s = '1234567890'
print('s =', s)
print('isalpha:', s.isalpha())
# s = 1234567890
# isalpha: False

s = '１２３４５６７８９０'
print('s =', s)
print('isalpha:', s.isalpha())
# s = １２３４５６７８９０
# isalpha: False

s = '一二三四五六七八九'
print('s =', s)
print('isalpha:', s.isalpha())
# s = 一二三四五六七八九
# isalpha: True

s = '壱億参阡萬'
print('s =', s)
print('isalpha:', s.isalpha())
# s = 壱億参阡萬
# isalpha: True

s = '〇'
print('s =', s)
print('isalpha:', s.isalpha())
# s = 〇
# isalpha: False

s = '\u2166'
print('s =', s)
print('isalpha:', s.isalpha())
# s = Ⅶ
# isalpha: False

s = 'abc123'
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = abc123
# isalnum: True
# isalpha: False
# isdecimal: False
# isdigit: False
# isnumeric: False

s = 'abc123+-,.&'
print('s =', s)
print('isascii:', s.isascii())
print('isalnum:', s.isalnum())
# s = abc123+-,.&
# isascii: True
# isalnum: False

s = 'あいうえお'
print('s =', s)
print('isascii:', s.isascii())
print('isalnum:', s.isalnum())
# s = あいうえお
# isascii: False
# isalnum: True

s = ''
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
print('isascii:', s.isascii())
# s = 
# isalnum: False
# isalpha: False
# isdecimal: False
# isdigit: False
# isnumeric: False
# isascii: True

print(bool(''))
# False

print(bool('abc123'))
# True

s = '-1.23'
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
print('isascii:', s.isascii())
# s = -1.23
# isalnum: False
# isalpha: False
# isdecimal: False
# isdigit: False
# isnumeric: False
# isascii: True

print(float('-1.23'))
# -1.23

print(type(float('-1.23')))
# <class 'float'>

# print(float('abc'))
# ValueError: could not convert string to float: 'abc'

def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

print(is_num('123'))
# True

print(is_num('-1.23'))
# True

print(is_num('+1.23e10'))
# True

print(is_num('abc'))
# False

print(is_num('10,000,000'))
# False

def is_num_delimiter(s):
    try:
        float(s.replace(',', ''))
    except ValueError:
        return False
    else:
        return True

print(is_num_delimiter('10,000,000'))
# True

def is_num_delimiter2(s):
    try:
        float(s.replace(',', '').replace(' ', ''))
    except ValueError:
        return False
    else:
        return True

print(is_num_delimiter2('10,000,000'))
# True

print(is_num_delimiter2('10 000 000'))
# True
