import unicodedata

s = '１２３ａｂｃｱｲｳｴｵ①㈱㌖'
print(unicodedata.normalize('NFKC', s))
# 123abcアイウエオ1(株)キロメートル

s = '１２３ａｂｃｱｲｳｴｵ①②③¹²³'
print(unicodedata.normalize('NFD', s))
# １２３ａｂｃｱｲｳｴｵ①②③¹²³

print(unicodedata.normalize('NFC', s))
# １２３ａｂｃｱｲｳｴｵ①②③¹²³

print(unicodedata.normalize('NFKD', s))
# 123abcアイウエオ123123

print(unicodedata.normalize('NFKC', s))
# 123abcアイウエオ123123

s = 'がガぱパ'
print(unicodedata.normalize('NFD', s))
print(list(unicodedata.normalize('NFD', s)))
# がガぱパ
# ['か', '゙', 'カ', '゙', 'は', '゚', 'ハ', '゚']

print(unicodedata.normalize('NFC', s))
print(list(unicodedata.normalize('NFC', s)))
# がガぱパ
# ['が', 'ガ', 'ぱ', 'パ']

print(unicodedata.normalize('NFKD', s))
print(list(unicodedata.normalize('NFKD', s)))
# がガぱパ
# ['か', '゙', 'カ', '゙', 'は', '゚', 'ハ', '゚']

print(unicodedata.normalize('NFKC', s))
print(list(unicodedata.normalize('NFKC', s)))
# がガぱパ
# ['が', 'ガ', 'ぱ', 'パ']

s = 'ｶﾞﾊﾟ'
print(s)
print(list(s))
# ｶﾞﾊﾟ
# ['ｶ', 'ﾞ', 'ﾊ', 'ﾟ']

print(unicodedata.normalize('NFD', s))
print(list(unicodedata.normalize('NFD', s)))
# ｶﾞﾊﾟ
# ['ｶ', 'ﾞ', 'ﾊ', 'ﾟ']

print(unicodedata.normalize('NFC', s))
print(list(unicodedata.normalize('NFC', s)))
# ｶﾞﾊﾟ
# ['ｶ', 'ﾞ', 'ﾊ', 'ﾟ']

print(unicodedata.normalize('NFKD', s))
print(list(unicodedata.normalize('NFKD', s)))
# ガパ
# ['カ', '゙', 'ハ', '゚']

print(unicodedata.normalize('NFKC', s))
print(list(unicodedata.normalize('NFKC', s)))
# ガパ
# ['ガ', 'パ']

s = '㈱㌖'
print(unicodedata.normalize('NFD', s))
# ㈱㌖

print(unicodedata.normalize('NFC', s))
# ㈱㌖

print(unicodedata.normalize('NFKD', s))
# (株)キロメートル

print(unicodedata.normalize('NFKC', s))
# (株)キロメートル

s = '１２３ａｂｃアイウエオ123abcｱｲｳｴｵ'
print(unicodedata.normalize('NFKC', s))
# 123abcアイウエオ123abcアイウエオ

s = '（）．，「」。、().,｢｣｡､'
print(unicodedata.normalize('NFKC', s))
# ().,「」。、().,「」。、

s = '～〜'
print(unicodedata.normalize('NFKC', s))
# ~〜

print([hex(ord(c)) for c in s])
# ['0xff5e', '0x301c']

print([hex(ord(c)) for c in unicodedata.normalize('NFKC', s)])
# ['0x7e', '0x301c']

s = '①㈱㌖'
print(unicodedata.normalize('NFKC', s))
# 1(株)キロメートル

s = '®©💯'
print(unicodedata.normalize('NFKC', s))
# ®©💯

s = '～〜'
print(unicodedata.normalize('NFKC', s).replace('〜', '~'))
# ~~

print(unicodedata.normalize('NFKC', s.replace('〜', '～')))
# ~~

s = '®©'
print(s.translate(str.maketrans('®©', 'RC')))
# RC

s = '１２３ａｂｃｱｲｳｴｵ①②③¹²³'
print(unicodedata.is_normalized('NFC', s))
# True

print(unicodedata.is_normalized('NFKC', s))
# False
