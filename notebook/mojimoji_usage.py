import mojimoji

s = '１２３ａｂｃ！？アイウエオ123abc!?ｱｲｳｴｵ'
print(mojimoji.zen_to_han(s))
# 123abc!?ｱｲｳｴｵ123abc!?ｱｲｳｴｵ

s = '１２３ａｂｃ！？アイウエオ123abc!?ｱｲｳｴｵ'
print(mojimoji.han_to_zen(s))
# １２３ａｂｃ！？アイウエオ１２３ａｂｃ！？アイウエオ

s = '１２３ａｂｃ！？アイウエオ123abc!?ｱｲｳｴｵ'
print(mojimoji.zen_to_han(s, kana=False))
# 123abc!?アイウエオ123abc!?ｱｲｳｴｵ

print(mojimoji.han_to_zen(s, digit=False, ascii=False))
# １２３ａｂｃ！？アイウエオ123abc!?アイウエオ

print(mojimoji.han_to_zen(mojimoji.zen_to_han(s, kana=False), digit=False, ascii=False))
# 123abc!?アイウエオ123abc!?アイウエオ
