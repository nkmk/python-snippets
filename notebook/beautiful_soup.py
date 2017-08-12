import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.yahoo.co.jp/'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")

li_list = soup.find(id='yahooservice').find_all('li')
# li_list = soup.find('div', attrs={'id': 'yahooservice'}).find_all('li')
# li_list = soup.select('div#yahooservice > ul > li')

for li in li_list:
    print(li.find('a').text)
# ショッピング
# ヤフオク!
# LOHACO
# 旅行、ホテル予約
# 一休.com
# 一休.comレストラン
# ニュース
# 天気
# スポーツナビ
# ファイナンス
# テレビ
# GYAO!
# ゲーム
# Yahoo!モバゲー
# 地図
# 路線
# 食べログ
# 求人、アルバイト
# 不動産
# 自動車
# 掲示板
# ブログ
# 美容、ダイエット
# 恋愛、婚活
