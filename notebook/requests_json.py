import requests
import pprint
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

params = {'city': 130010}

r = requests.get(url, params=params)

print(r.headers['Content-Type'])
# application/json; charset=utf-8

json_data = r.json()

print(type(json_data))
# <class 'dict'>

pprint.pprint(json_data, depth=2, compact=True)
# {'copyright': {'image': {...},
#                'link': 'http://weather.livedoor.com/',
#                'provider': [...],
#                'title': '(C) LINE Corporation'},
#  'description': {'publicTime': '2018-07-12T18:33:00+0900',
#                  'text': ' 日本の東には高気圧があって東に進んでいます。また、日本の南にも高気\n'
#                          '圧があり停滞しています。関東甲信地方は、高気圧の間で気圧の谷になって\n'
#                          'います。\n'
#                          '\n'
#                          '【関東甲信地方】\n'
#                          ' 関東甲信地方はおおむね曇りで、雷を伴い非常に激しい雨の降っている所\n'
#                          'があります。\n'
#                          '\n'
#                          ' 12日は、気圧の谷や湿った空気の影響により曇りで、所により雷を伴い\n'
#                          '非常に激しく降る所がある見込みです。\n'
#                          '\n'
#                          ' 13日は、上空の気圧の谷や湿った空気の影響で曇りますが、昼頃から次\n'
#                          '第に晴れるでしょう。朝晩は雨の降る所がある見込みです。\n'
#                          '\n'
#                          ' 関東近海では、13日にかけてうねりを伴って波がやや高いでしょう。ま\n'
#                          'た、所々で霧が発生する見込みです。船舶は視程障害に注意してください。\n'
#                          '\n'
#                          '【東京地方】\n'
#                          ' 12日は、曇りですが、夜のはじめ頃まで雷を伴って激しく降る所がある\n'
#                          'でしょう。\n'
#                          ' 13日は、曇りで昼過ぎから晴れますが、明け方まで雨の降る所がある見\n'
#                          '込みです。'},
#  'forecasts': [{...}, {...}, {...}],
#  'link': 'http://weather.livedoor.com/area/forecast/130010',
#  'location': {'area': '関東', 'city': '東京', 'prefecture': '東京都'},
#  'pinpointLocations': [{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...},
#                        {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...},
#                        {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...},
#                        {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...},
#                        {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...},
#                        {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...},
#                        {...}, {...}, {...}, {...}, {...}],
#  'publicTime': '2018-07-12T17:00:00+0900',
#  'title': '東京都 東京 の天気'}

print(json_data['description']['text'])
#  日本の東には高気圧があって東に進んでいます。また、日本の南にも高気
# 圧があり停滞しています。関東甲信地方は、高気圧の間で気圧の谷になって
# います。
# 
# 【関東甲信地方】
#  関東甲信地方はおおむね曇りで、雷を伴い非常に激しい雨の降っている所
# があります。
# 
#  12日は、気圧の谷や湿った空気の影響により曇りで、所により雷を伴い
# 非常に激しく降る所がある見込みです。
# 
#  13日は、上空の気圧の谷や湿った空気の影響で曇りますが、昼頃から次
# 第に晴れるでしょう。朝晩は雨の降る所がある見込みです。
# 
#  関東近海では、13日にかけてうねりを伴って波がやや高いでしょう。ま
# た、所々で霧が発生する見込みです。船舶は視程障害に注意してください。
# 
# 【東京地方】
#  12日は、曇りですが、夜のはじめ頃まで雷を伴って激しく降る所がある
# でしょう。
#  13日は、曇りで昼過ぎから晴れますが、明け方まで雨の降る所がある見
# 込みです。

pprint.pprint(json_data['forecasts'][0])
# {'date': '2018-07-12',
#  'dateLabel': '今日',
#  'image': {'height': 31,
#            'title': '曇り',
#            'url': 'http://weather.livedoor.com/img/icon/8.gif',
#            'width': 50},
#  'telop': '曇り',
#  'temperature': {'max': None, 'min': None}}

with open('data/temp/download.json', 'w') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
