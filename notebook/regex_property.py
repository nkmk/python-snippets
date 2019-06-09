import regex

p = regex.compile(r'\p{Block=Hiragana}+')
print(p.fullmatch('あいうえおぁぃぅぇぉわをんゟ'))
# <regex.Match object; span=(0, 14), match='あいうえおぁぃぅぇぉわをんゟ'>

p = regex.compile(r'\p{Script=Hiragana}+')
print(p.fullmatch('あいうえおぁぃぅぇぉわをんゟ🈀'))
# <regex.Match object; span=(0, 15), match='あいうえおぁぃぅぇぉわをんゟ🈀'>

p = regex.compile(r'\p{Hiragana}+')
print(p.fullmatch('あいうえおぁぃぅぇぉわをんゟ🈀'))
# <regex.Match object; span=(0, 15), match='あいうえおぁぃぅぇぉわをんゟ🈀'>

# p = regex.compile(r'\p{subhead=Hiragana_letters}+')
# error: unknown property at position 28

p = regex.compile(r'[\p{Script=Hiragana}\p{Script=Katakana}ーa-z]+')
print(p.fullmatch('あーいアイウabc🈀'))
# <regex.Match object; span=(0, 10), match='あーいアイウabc🈀'>
