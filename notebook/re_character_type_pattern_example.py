import re
import regex

p = re.compile('[a-z]+')
print(p.fullmatch('abc'))
# <re.Match object; span=(0, 3), match='abc'>

p = re.compile('[A-Z]+')
print(p.fullmatch('ABC'))
# <re.Match object; span=(0, 3), match='ABC'>

p = re.compile('[ａ-ｚ]+')
print(p.fullmatch('ａｂｃ'))
# <re.Match object; span=(0, 3), match='ａｂｃ'>

p = re.compile('[Ａ-Ｚ]+')
print(p.fullmatch('ＡＢＣ'))
# <re.Match object; span=(0, 3), match='ＡＢＣ'>

p = re.compile('[a-zA-Zａ-ｚＡ-Ｚ]+')
print(p.fullmatch('abcABCａｂｃＡＢＣ'))
# <re.Match object; span=(0, 12), match='abcABCａｂｃＡＢＣ'>

p = regex.compile(r'\p{Script=Latin}+')
print(p.fullmatch('AÁÀÂÄÆ'))
# <regex.Match object; span=(0, 6), match='AÁÀÂÄÆ'>

p = re.compile('[0-9]+')
print(p.fullmatch('123'))
# <re.Match object; span=(0, 3), match='123'>

p = re.compile('[０-９]+')
print(p.fullmatch('１２３'))
# <re.Match object; span=(0, 3), match='１２３'>

p = regex.compile(r'\p{Numeric_Type=Numeric}+')
print(p.fullmatch('一二三ⅠⅡⅢ百万億⑩⑽'))
# <regex.Match object; span=(0, 11), match='一二三ⅠⅡⅢ百万億⑩⑽'>

print(p.fullmatch('123'))
# None

p = re.compile('[\u2160-\u217F]+')
print(p.fullmatch('ⅠⅡⅢ'))
# <re.Match object; span=(0, 3), match='ⅠⅡⅢ'>

p = re.compile('[〇一二三四五六七八九十百千万億兆]+')
print(p.fullmatch('三十五億'))
# <re.Match object; span=(0, 4), match='三十五億'>

p = re.compile('[\u0000-\u007F]+')
print(p.fullmatch('(abc)!_(123)?'))
# <re.Match object; span=(0, 13), match='(abc)!_(123)?'>

p = re.compile('[\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]+')
print(p.fullmatch('!_? ()[]'))
# <re.Match object; span=(0, 8), match='!_? ()[]'>

p = re.compile(r'[,\.!?\[\]\(\)]+')
print(p.fullmatch(',.!?[]()'))
# <re.Match object; span=(0, 8), match=',.!?[]()'>

p = re.compile('[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65]+')
print(p.fullmatch('！？（）［］｢｣'))
# <re.Match object; span=(0, 8), match='！？（）［］｢｣'>

p = re.compile('[\u3000-\u303F]+')
print(p.fullmatch('、。「」【】'))
# <re.Match object; span=(0, 6), match='、。「」【】'>

p = re.compile('[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]+')
print(p.fullmatch('！？（）［］｢｣、。「」【】'))
# <re.Match object; span=(0, 14), match='！？（）［］｢｣、。「」【】'>

p = re.compile('[\u3041-\u309F]+')
print(p.fullmatch('あいうえおぁぃぅぇぉ'))
# <re.Match object; span=(0, 10), match='あいうえおぁぃぅぇぉ'>

p = re.compile('[ぁ-ゟ]+')
print(p.fullmatch('あいうえおぁぃぅぇぉ'))
# <re.Match object; span=(0, 10), match='あいうえおぁぃぅぇぉ'>

p = re.compile('[\u30A1-\u30FF]+')
print(p.fullmatch('アイウエオァィゥェォ'))
# <re.Match object; span=(0, 10), match='アイウエオァィゥェォ'>

p = re.compile('[\ァ-ヿ]+')
print(p.fullmatch('アイウエオァィゥェォ'))
# <re.Match object; span=(0, 10), match='アイウエオァィゥェォ'>

p = re.compile('[\uFF66-\uFF9F]+')
print(p.fullmatch('ｱｲｳｴｵｧｨｩｪｫ'))
# <re.Match object; span=(0, 10), match='ｱｲｳｴｵｧｨｩｪｫ'>

p = re.compile('[ｦ-ﾟ]+')
print(p.fullmatch('ｱｲｳｴｵｧｨｩｪｫ'))
# <re.Match object; span=(0, 10), match='ｱｲｳｴｵｧｨｩｪｫ'>

p = regex.compile(r'\p{Script=Han}+')
print(p.fullmatch('漢字'))
# <regex.Match object; span=(0, 2), match='漢字'>

p = regex.compile(r'\p{Script_Extensions=Han}+')
print(p.fullmatch('漢字〆㈠㈱㊊㏩'))
# <regex.Match object; span=(0, 7), match='漢字〆㈠㈱㊊㏩'>

p = re.compile('[\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')
print(p.fullmatch('漢字'))
# <re.Match object; span=(0, 2), match='漢字'>

p = regex.compile(r'\p{Emoji=Yes}+')
print(p.fullmatch('💯123'))
# <regex.Match object; span=(0, 4), match='💯123'>

p = regex.compile(r'\p{Emoji_Presentation=Yes}+')
print(p.fullmatch('💯'))
# <regex.Match object; span=(0, 1), match='💯'>

# p = regex.compile(r'\p{Basic_Emoji=Yes}+')
# error: unknown property at position 19

p = re.compile('[\U0001F300-\U0001F5FF]+')
print(p.fullmatch('💯'))
# <re.Match object; span=(0, 1), match='💯'>

p = re.compile('[\U0001F600-\U0001F64F]+')
print(p.fullmatch('😀'))
# <re.Match object; span=(0, 1), match='😀'>
