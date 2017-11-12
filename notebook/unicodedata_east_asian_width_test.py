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
