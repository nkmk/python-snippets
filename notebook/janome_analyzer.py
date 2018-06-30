from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *

t = Tokenizer()

s = '<div>PythonとＰＹＴＨＯＮとパイソンとﾊﾟｲｿﾝ</div>'

for token in t.tokenize(s):
    print(token)
# <	名詞,サ変接続,*,*,*,*,<,*,*
# div	名詞,一般,*,*,*,*,div,*,*
# >	名詞,サ変接続,*,*,*,*,>,*,*
# Python	名詞,一般,*,*,*,*,Python,*,*
# と	助詞,並立助詞,*,*,*,*,と,ト,ト
# ＰＹＴＨＯＮ	名詞,固有名詞,組織,*,*,*,ＰＹＴＨＯＮ,*,*
# と	助詞,並立助詞,*,*,*,*,と,ト,ト
# パイソン	名詞,一般,*,*,*,*,パイソン,*,*
# と	助詞,並立助詞,*,*,*,*,と,ト,ト
# ﾊﾟｲｿﾝ	名詞,一般,*,*,*,*,ﾊﾟｲｿﾝ,*,*
# </	名詞,サ変接続,*,*,*,*,</,*,*
# div	名詞,一般,*,*,*,*,div,*,*
# >	名詞,サ変接続,*,*,*,*,>,*,*

char_filters = [UnicodeNormalizeCharFilter(),
                RegexReplaceCharFilter('<.*?>', '')]

token_filters = [POSKeepFilter(['名詞']),
                 LowerCaseFilter(),
                 ExtractAttributeFilter('surface')]

a = Analyzer(char_filters=char_filters, token_filters=token_filters)

for token in a.analyze(s):
    print(token)
# python
# python
# パイソン
# パイソン

s = '自然言語処理による日本国憲法の形態素解析'

for token in t.tokenize(s):
    print(token)
# 自然	名詞,形容動詞語幹,*,*,*,*,自然,シゼン,シゼン
# 言語	名詞,一般,*,*,*,*,言語,ゲンゴ,ゲンゴ
# 処理	名詞,サ変接続,*,*,*,*,処理,ショリ,ショリ
# による	助詞,格助詞,連語,*,*,*,による,ニヨル,ニヨル
# 日本国	名詞,固有名詞,地域,国,*,*,日本国,ニッポンコク,ニッポンコク
# 憲法	名詞,一般,*,*,*,*,憲法,ケンポウ,ケンポー
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# 形態素	名詞,一般,*,*,*,*,形態素,ケイタイソ,ケイタイソ
# 解析	名詞,サ変接続,*,*,*,*,解析,カイセキ,カイセキ

a = Analyzer(token_filters=[CompoundNounFilter()])

for token in a.analyze(s):
    print(token)
# 自然言語処理	名詞,複合,*,*,*,*,自然言語処理,シゼンゲンゴショリ,シゼンゲンゴショリ
# による	助詞,格助詞,連語,*,*,*,による,ニヨル,ニヨル
# 日本国憲法	名詞,複合,*,*,*,*,日本国憲法,ニッポンコクケンポウ,ニッポンコクケンポー
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# 形態素解析	名詞,複合,*,*,*,*,形態素解析,ケイタイソカイセキ,ケイタイソカイセキ

s = '人民の人民による人民のための政治'

a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])

g_count = a.analyze(s)
print(type(g_count))
# <class 'generator'>

for i in g_count:
    print(i)
# ('人民', 3)
# ('ため', 1)
# ('政治', 1)

l_count = list(a.analyze(s))
print(type(l_count))
# <class 'list'>

print(l_count)
# [('人民', 3), ('ため', 1), ('政治', 1)]

d_count = dict(a.analyze(s))
print(type(d_count))
# <class 'dict'>

print(d_count)
# {'人民': 3, 'ため': 1, '政治': 1}

print(d_count['人民'])
# 3

# print(d_count['国民'])
# KeyError: '国民'

print(d_count.get('国民', 0))
# 0

s = '走れと言われたので走ると言った'

a = Analyzer(token_filters=[TokenCountFilter()])

print(list(a.analyze(s)))
# [('走れ', 1), ('と', 2), ('言わ', 1), ('れ', 1), ('た', 2), ('ので', 1), ('走る', 1), ('言っ', 1)]

a = Analyzer(token_filters=[TokenCountFilter(att='base_form')])

print(list(a.analyze(s)))
# [('走る', 2), ('と', 2), ('言う', 2), ('れる', 1), ('た', 2), ('ので', 1)]

a = Analyzer(token_filters=[TokenCountFilter(att='part_of_speech')])

print(list(a.analyze(s)))
# [('動詞,自立,*,*', 4), ('助詞,格助詞,引用,*', 2), ('動詞,接尾,*,*', 1), ('助動詞,*,*,*', 2), ('助詞,接続助詞,*,*', 1)]

s = '吾輩は猫である'

a = Analyzer(token_filters=[POSKeepFilter('助動詞')])

for token in a.analyze(s):
    print(token)
# は	助詞,係助詞,*,*,*,*,は,ハ,ワ
# で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
# ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル

a = Analyzer(token_filters=[POSKeepFilter(['助動詞'])])

for token in a.analyze(s):
    print(token)
# で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
# ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
