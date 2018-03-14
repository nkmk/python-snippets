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

s = '\u00B2'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = ²
# isdecimal: False
# isdigit: True
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

s = 'abc100'
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = abc100
# isalnum: True
# isalpha: False
# isdecimal: False
# isdigit: False
# isnumeric: False

s = ''
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())
# s = 
# isalnum: False
# isalpha: False
# isdecimal: False
# isdigit: False
# isnumeric: False

s = '10,000,000'
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdigit:', s.isdigit())
print('isdecimal:', s.isdecimal())
print('isnumeric:', s.isnumeric())
# s = 10,000,000
# isalnum: False
# isalpha: False
# isdigit: False
# isdecimal: False
# isnumeric: False

s = '1.23'
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdigit:', s.isdigit())
print('isdecimal:', s.isdecimal())
print('isnumeric:', s.isnumeric())
# s = 1.23
# isalnum: False
# isalpha: False
# isdigit: False
# isdecimal: False
# isnumeric: False

s = '-100'
print('s =', s)
print('isalnum:', s.isalnum())
print('isalpha:', s.isalpha())
print('isdigit:', s.isdigit())
print('isdecimal:', s.isdecimal())
print('isnumeric:', s.isnumeric())
# s = -100
# isalnum: False
# isalpha: False
# isdigit: False
# isdecimal: False
# isnumeric: False

def is_num(s):
    return s.replace(',', '').replace('.', '').replace('-', '').isnumeric()

print(is_num('-1.23'))
# True

print(is_num('10,000,000'))
# True

print(is_num('128.0.0.0'))
# True

def is_num2(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

print(is_num2('-1.23'))
# True

print(is_num2('128.0.0.0'))
# False

print(is_num2('10,000,000'))
# False

print(is_num2('1.23e10'))
# True
