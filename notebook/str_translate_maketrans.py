z_digit = '１２３４５６７８９０'
h_digit = '1234567890'

z2h_digit = str.maketrans(z_digit, h_digit)
h2z_digit = str.maketrans(h_digit, z_digit)

s = '１２３123'
print(s.translate(z2h_digit))
# 123123

print(s.translate(h2z_digit))
# １２３１２３

z_ascii = '\u3000' + ''.join(chr(i) for i in range(0xFF01, 0xFF5E + 1))
print(z_ascii)
# 　！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～

h_ascii = ''.join(chr(i) for i in range(0x0020, 0x007E + 1))
print(h_ascii)
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

z2h_ascii = str.maketrans(z_ascii, h_ascii)
h2z_ascii = str.maketrans(h_ascii, z_ascii)

s = '１２３ａｂｃ！？123abc!?'
print(s.translate(z2h_ascii))
# 123abc!?123abc!?

print(s.translate(h2z_ascii))
# １２３ａｂｃ！？１２３ａｂｃ！？

z_ascii_yen = z_ascii + '￥'
h_ascii_yen = h_ascii + '¥'

z2h_ascii_yen = str.maketrans(z_ascii_yen, h_ascii_yen)
h2z_ascii_yen = str.maketrans(h_ascii_yen, z_ascii_yen)

s = '１２３ａｂｃ！？￥123abc!?¥'
print(s.translate(z2h_ascii_yen))
# 123abc!?¥123abc!?¥

print(s.translate(h2z_ascii_yen))
# １２３ａｂｃ！？￥１２３ａｂｃ！？￥

print(len('ガ'))
# 1

print(list('ガ'))
# ['ガ']

print(len('ｶﾞ'))
# 2

print(list('ｶﾞ'))
# ['ｶ', 'ﾞ']

# str.maketrans('ガ', 'ｶﾞ')
# ValueError: the first two maketrans arguments must have equal length
