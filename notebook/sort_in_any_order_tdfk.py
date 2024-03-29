import pprint

l = ['沖縄県', '東京都', '北海道', '京都府']

print(sorted(l))
# ['京都府', '北海道', '東京都', '沖縄県']

tdfk = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
        '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
        '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県',
        '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県',
        '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県',
        '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県',
        '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']

print(sorted(l, key=tdfk.index))
# ['北海道', '東京都', '京都府', '沖縄県']

d_tdfk = {x: i for i, x in enumerate(tdfk)}
print(d_tdfk)
# {'北海道': 0, '青森県': 1, '岩手県': 2, '宮城県': 3, '秋田県': 4, '山形県': 5, '福島県': 6, '茨城県': 7, '栃木県': 8, '群馬県': 9, '埼玉県': 10, '千葉県': 11, '東京都': 12, '神奈川県': 13, '新潟県': 14, '富山県': 15, '石川県': 16, '福井県': 17, '山梨県': 18, '長野県': 19, '岐阜県': 20, '静岡県': 21, '愛知県': 22, '三重県': 23, '滋賀県': 24, '京都府': 25, '大阪府': 26, '兵庫県': 27, '奈良県': 28, '和歌山県': 29, '鳥取県': 30, '島根県': 31, '岡山県': 32, '広島県': 33, '山口県': 34, '徳島県': 35, '香川県': 36, '愛媛県': 37, '高知県': 38, '福岡県': 39, '佐賀県': 40, '長崎県': 41, '熊本県': 42, '大分県': 43, '宮崎県': 44, '鹿児島県': 45, '沖縄県': 46}

print(sorted(l, key=lambda x: d_tdfk[x]))
# ['北海道', '東京都', '京都府', '沖縄県']

l = ['沖縄県', '東京都', '北海道', '京都府', 'xxx']

# print(sorted(l, key=tdfk.index))
# ValueError: 'xxx' is not in list

print(sorted(l, key=lambda x: tdfk.index(x) if x in tdfk else -1))
# ['xxx', '北海道', '東京都', '京都府', '沖縄県']

print(sorted(l, key=lambda x: tdfk.index(x) if x in tdfk else float('inf')))
# ['北海道', '東京都', '京都府', '沖縄県', 'xxx']

print(sorted(l, key=lambda x: d_tdfk.get(x, -1)))
# ['xxx', '北海道', '東京都', '京都府', '沖縄県']

print(sorted(l, key=lambda x: d_tdfk.get(x, float('inf'))))
# ['北海道', '東京都', '京都府', '沖縄県', 'xxx']

l = ['沖縄県', '東京', '北海道', '京都府']

# print(sorted(l, key=tdfk.index))
# ValueError: '東京' is not in list

tdfk2 = [s[:2] for s in tdfk]
pprint.pprint(tdfk2, compact=True)
# ['北海', '青森', '岩手', '宮城', '秋田', '山形', '福島', '茨城', '栃木', '群馬', '埼玉', '千葉', '東京',
#  '神奈', '新潟', '富山', '石川', '福井', '山梨', '長野', '岐阜', '静岡', '愛知', '三重', '滋賀', '京都',
#  '大阪', '兵庫', '奈良', '和歌', '鳥取', '島根', '岡山', '広島', '山口', '徳島', '香川', '愛媛', '高知',
#  '福岡', '佐賀', '長崎', '熊本', '大分', '宮崎', '鹿児', '沖縄']

d_tdfk2 = {x[:2]: i for i, x in enumerate(tdfk)}

print(sorted(l, key=lambda x: tdfk2.index(x[:2])))
# ['北海道', '東京', '京都府', '沖縄県']

print(sorted(l, key=lambda x: d_tdfk2[x[:2]]))
# ['北海道', '東京', '京都府', '沖縄県']

l = ['沖縄県', '東京', '北海道', '京都府', 'xxx']

print(sorted(l, key=lambda x: tdfk2.index(x[:2]) if x[:2] in tdfk2 else -1))
# ['xxx', '北海道', '東京', '京都府', '沖縄県']

print(sorted(l, key=lambda x: d_tdfk2.get(x[:2], -1)))
# ['xxx', '北海道', '東京', '京都府', '沖縄県']

l = ['沖縄県', '東京', '東京都', '北海道', '京都府']
print(sorted(l, key=lambda x: tdfk2.index(x[:2])))
# ['北海道', '東京', '東京都', '京都府', '沖縄県']

l = ['沖縄県', '東京都', '東京', '北海道', '京都府']
print(sorted(l, key=lambda x: tdfk2.index(x[:2])))
# ['北海道', '東京都', '東京', '京都府', '沖縄県']

tdfk3 = sorted(tdfk + [s[:-1] for s in tdfk], key=lambda x: tdfk2.index(x[:2]))
tdfk3.remove('北海')
pprint.pprint(tdfk3, compact=True)
# ['北海道', '青森県', '青森', '岩手県', '岩手', '宮城県', '宮城', '秋田県', '秋田', '山形県', '山形', '福島県',
#  '福島', '茨城県', '茨城', '栃木県', '栃木', '群馬県', '群馬', '埼玉県', '埼玉', '千葉県', '千葉', '東京都',
#  '東京', '神奈川県', '神奈川', '新潟県', '新潟', '富山県', '富山', '石川県', '石川', '福井県', '福井', '山梨県',
#  '山梨', '長野県', '長野', '岐阜県', '岐阜', '静岡県', '静岡', '愛知県', '愛知', '三重県', '三重', '滋賀県',
#  '滋賀', '京都府', '京都', '大阪府', '大阪', '兵庫県', '兵庫', '奈良県', '奈良', '和歌山県', '和歌山', '鳥取県',
#  '鳥取', '島根県', '島根', '岡山県', '岡山', '広島県', '広島', '山口県', '山口', '徳島県', '徳島', '香川県',
#  '香川', '愛媛県', '愛媛', '高知県', '高知', '福岡県', '福岡', '佐賀県', '佐賀', '長崎県', '長崎', '熊本県',
#  '熊本', '大分県', '大分', '宮崎県', '宮崎', '鹿児島県', '鹿児島', '沖縄県', '沖縄']

l = ['沖縄県', '東京', '東京都', '北海道', '京都府']
print(sorted(l, key=tdfk3.index))
# ['北海道', '東京都', '東京', '京都府', '沖縄県']

l = ['沖縄県', '東京都', '東京', '北海道', '京都府']
print(sorted(l, key=tdfk3.index))
# ['北海道', '東京都', '東京', '京都府', '沖縄県']
