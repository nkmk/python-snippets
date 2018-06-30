from janome.tokenizer import Tokenizer

t = Tokenizer()

s = 'すもももももももものうち'

print(type(t.tokenize(s)))
# <class 'list'>

print(type(t.tokenize(s)[0]))
# <class 'janome.tokenizer.Token'>

for token in t.tokenize(s):
    print(token)
# すもも	名詞,一般,*,*,*,*,すもも,スモモ,スモモ
# も	助詞,係助詞,*,*,*,*,も,モ,モ
# もも	名詞,一般,*,*,*,*,もも,モモ,モモ
# も	助詞,係助詞,*,*,*,*,も,モ,モ
# もも	名詞,一般,*,*,*,*,もも,モモ,モモ
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# うち	名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ

print(type(t.tokenize(s, stream=True)))
# <class 'generator'>

for token in t.tokenize(s, stream=True):
    print(token)
# すもも	名詞,一般,*,*,*,*,すもも,スモモ,スモモ
# も	助詞,係助詞,*,*,*,*,も,モ,モ
# もも	名詞,一般,*,*,*,*,もも,モモ,モモ
# も	助詞,係助詞,*,*,*,*,も,モ,モ
# もも	名詞,一般,*,*,*,*,もも,モモ,モモ
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# うち	名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ

token = t.tokenize('走れ')[0]

print(type(token))
# <class 'janome.tokenizer.Token'>

print(token)
# 走れ	動詞,自立,*,*,五段・ラ行,命令ｅ,走る,ハシレ,ハシレ

print(token.surface)
# 走れ

print(token.part_of_speech)
# 動詞,自立,*,*

print(token.part_of_speech.split(','))
# ['動詞', '自立', '*', '*']

print(token.part_of_speech.split(',')[0])
# 動詞

print(token.infl_type)
# 五段・ラ行

print(token.infl_form)
# 命令ｅ

print(token.base_form)
# 走る

print(token.reading)
# ハシレ

print(token.phonetic)
# ハシレ

s = '走れと言われたので走ると言った'

for token in t.tokenize(s):
    print(token)
# 走れ	動詞,自立,*,*,五段・ラ行,命令ｅ,走る,ハシレ,ハシレ
# と	助詞,格助詞,引用,*,*,*,と,ト,ト
# 言わ	動詞,自立,*,*,五段・ワ行促音便,未然形,言う,イワ,イワ
# れ	動詞,接尾,*,*,一段,連用形,れる,レ,レ
# た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
# ので	助詞,接続助詞,*,*,*,*,ので,ノデ,ノデ
# 走る	動詞,自立,*,*,五段・ラ行,基本形,走る,ハシル,ハシル
# と	助詞,格助詞,引用,*,*,*,と,ト,ト
# 言っ	動詞,自立,*,*,五段・ワ行促音便,連用タ接続,言う,イッ,イッ
# た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ

print(t.tokenize(s, wakati=True))
# ['走れ', 'と', '言わ', 'れ', 'た', 'ので', '走る', 'と', '言っ', 'た']

t_wakati = Tokenizer(wakati=True)

print(t_wakati.tokenize(s))
# ['走れ', 'と', '言わ', 'れ', 'た', 'ので', '走る', 'と', '言っ', 'た']

print([token.surface for token in t.tokenize(s)])
# ['走れ', 'と', '言わ', 'れ', 'た', 'ので', '走る', 'と', '言っ', 'た']

print([token.base_form for token in t.tokenize(s)])
# ['走る', 'と', '言う', 'れる', 'た', 'ので', '走る', 'と', '言う', 'た']

print([token.part_of_speech.split(',')[0] for token in t.tokenize(s)])
# ['動詞', '助詞', '動詞', '動詞', '助動詞', '助詞', '動詞', '助詞', '動詞', '助動詞']

print([token.surface for token in t.tokenize(s)
       if token.part_of_speech.startswith('動詞')])
# ['走れ', '言わ', 'れ', '走る', '言っ']

print([token.surface for token in t.tokenize(s)
       if not token.part_of_speech.startswith('動詞')])
# ['と', 'た', 'ので', 'と', 'た']

print([token.surface for token in t.tokenize(s)
       if token.part_of_speech.startswith('動詞,自立')])
# ['走れ', '言わ', '走る', '言っ']

print([token.surface for token in t.tokenize(s)
       if token.part_of_speech.split(',')[0] in ['動詞', '助動詞']])
# ['走れ', '言わ', 'れ', 'た', '走る', '言っ', 'た']
