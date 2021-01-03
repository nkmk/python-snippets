import unicodedata

print(unicodedata.east_asian_width('あ'))  # 全角かな
print(type(unicodedata.east_asian_width('あ')))
# W
# <class 'str'>

print(unicodedata.east_asian_width('a'))  # 半角英数
# Na

print(unicodedata.east_asian_width('Ａ'))  # 全角英数
# F

print(unicodedata.east_asian_width('ｱ'))  # 半角カナ
# H

print(unicodedata.east_asian_width('Å'))  # 特殊文字（例: オングストローム）
# A

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

print(get_east_asian_width_count('あいうえお'))
# 10

print(get_east_asian_width_count('abcde'))
# 5

print(get_east_asian_width_count('ｱｲｳｴｵ'))
# 5

print(get_east_asian_width_count('ａｂｃｄｅ'))
# 10

print(get_east_asian_width_count('あｱaａ'))  # 全角2文字（あ, ａ）、半角2文字（ｱ, a）
# 6
