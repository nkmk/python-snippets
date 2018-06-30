from janome.tokenizer import Tokenizer
import collections

t = Tokenizer()

s = '人民の人民による人民のための政治'

for token in t.tokenize(s):
    print(token)
# 人民	名詞,一般,*,*,*,*,人民,ジンミン,ジンミン
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# 人民	名詞,一般,*,*,*,*,人民,ジンミン,ジンミン
# による	助詞,格助詞,連語,*,*,*,による,ニヨル,ニヨル
# 人民	名詞,一般,*,*,*,*,人民,ジンミン,ジンミン
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# ため	名詞,非自立,副詞可能,*,*,*,ため,タメ,タメ
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# 政治	名詞,一般,*,*,*,*,政治,セイジ,セイジ

c = collections.Counter(t.tokenize(s, wakati=True))

print(type(c))
# <class 'collections.Counter'>

print(c)
# Counter({'人民': 3, 'の': 3, 'による': 1, 'ため': 1, '政治': 1})

print(c['人民'])
# 3

print(c['国民'])
# 0

mc = c.most_common()
print(mc)
# [('人民', 3), ('の', 3), ('による', 1), ('ため', 1), ('政治', 1)]

print(mc[0][0])
# 人民

print(mc[0][1])
# 3

words, counts = zip(*c.most_common())

print(words)
# ('人民', 'の', 'による', 'ため', '政治')

print(counts)
# (3, 3, 1, 1, 1)

s = '走れと言われたので走ると言った'

print(collections.Counter(t.tokenize(s, wakati=True)))
# Counter({'と': 2, 'た': 2, '走れ': 1, '言わ': 1, 'れ': 1, 'ので': 1, '走る': 1, '言っ': 1})

print(collections.Counter(token.base_form for token in t.tokenize(s)))
# Counter({'走る': 2, 'と': 2, '言う': 2, 'た': 2, 'れる': 1, 'ので': 1})

print(type(token.base_form for token in t.tokenize(s)))
# <class 'generator'>

print(collections.Counter(token.base_form for token in t.tokenize(s)
                          if token.part_of_speech.startswith('動詞,自立')))
# Counter({'走る': 2, '言う': 2})

print(collections.Counter(token.part_of_speech.split(',')[0] for token in t.tokenize(s)))
# Counter({'動詞': 5, '助詞': 3, '助動詞': 2})
