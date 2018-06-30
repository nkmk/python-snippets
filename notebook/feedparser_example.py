import feedparser
import pprint
import time

print(feedparser.__version__)
# 5.2.1

d_atom = feedparser.parse('http://gihyo.jp/feed/atom')

print(type(d_atom))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(d_atom, depth=1)
# {'bozo': 0,
#  'encoding': 'UTF-8',
#  'entries': [...],
#  'feed': {...},
#  'headers': {...},
#  'href': 'http://gihyo.jp/feed/atom',
#  'namespaces': {...},
#  'status': 200,
#  'updated': 'Sat, 30 Jun 2018 07:22:01 GMT',
#  'updated_parsed': time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=7, tm_min=22, tm_sec=1, tm_wday=5, tm_yday=181, tm_isdst=0),
#  'version': 'atom10'}

print(d_atom['encoding'])
# UTF-8

print(d_atom.get('encoding'))
# UTF-8

print(list(d_atom.keys()))
# ['feed', 'entries', 'bozo', 'headers', 'updated', 'updated_parsed', 'href', 'status', 'encoding', 'version', 'namespaces']

d_rss1 = feedparser.parse('http://gihyo.jp/feed/rss1')

print(type(d_rss1))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(d_rss1, depth=1)
# {'bozo': 0,
#  'encoding': 'UTF-8',
#  'entries': [...],
#  'feed': {...},
#  'headers': {...},
#  'href': 'http://gihyo.jp/feed/rss1',
#  'namespaces': {...},
#  'status': 200,
#  'updated': 'Sat, 30 Jun 2018 07:22:01 GMT',
#  'updated_parsed': time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=7, tm_min=22, tm_sec=1, tm_wday=5, tm_yday=181, tm_isdst=0),
#  'version': 'rss10'}

d_rss2 = feedparser.parse('http://gihyo.jp/feed/rss2')

print(type(d_rss2))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(d_rss2, depth=1)
# {'bozo': 0,
#  'encoding': 'UTF-8',
#  'entries': [...],
#  'feed': {...},
#  'headers': {...},
#  'href': 'http://gihyo.jp/feed/rss2',
#  'namespaces': {},
#  'status': 200,
#  'updated': 'Sat, 30 Jun 2018 07:22:01 GMT',
#  'updated_parsed': time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=7, tm_min=22, tm_sec=1, tm_wday=5, tm_yday=181, tm_isdst=0),
#  'version': 'rss20'}

feed = feedparser.parse('http://gihyo.jp/feed/atom')['feed']

print(type(feed))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(feed)
# {'author': '技術評論社',
#  'author_detail': {'name': '技術評論社'},
#  'authors': [{'name': '技術評論社'}],
#  'guidislink': True,
#  'icon': 'http://gihyo.jp/assets/templates/gihyojp2007/image/header_logo_gihyo.gif',
#  'id': 'http://gihyo.jp/',
#  'link': 'http://gihyo.jp/',
#  'links': [{'href': 'http://gihyo.jp/',
#             'rel': 'alternate',
#             'type': 'text/html'}],
#  'rights': '技術評論社 2018',
#  'rights_detail': {'base': 'http://gihyo.jp/feed/atom',
#                    'language': None,
#                    'type': 'text/plain',
#                    'value': '技術評論社 2018'},
#  'subtitle': 'gihyo.jp（総合）の更新情報をお届けします',
#  'subtitle_detail': {'base': 'http://gihyo.jp/feed/atom',
#                      'language': None,
#                      'type': 'text/plain',
#                      'value': 'gihyo.jp（総合）の更新情報をお届けします'},
#  'title': 'gihyo.jp：総合',
#  'title_detail': {'base': 'http://gihyo.jp/feed/atom',
#                   'language': None,
#                   'type': 'text/plain',
#                   'value': 'gihyo.jp：総合'},
#  'updated': '2018-06-30T16:22:01+09:00',
#  'updated_parsed': time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=7, tm_min=22, tm_sec=1, tm_wday=5, tm_yday=181, tm_isdst=0)}

print(feed['updated'])
# 2018-06-30T16:22:01+09:00

print(type(feed['updated']))
# <class 'str'>

t = feed['updated_parsed']

print(t)
# time.struct_time(tm_year=2018, tm_mon=6, tm_mday=30, tm_hour=7, tm_min=22, tm_sec=1, tm_wday=5, tm_yday=181, tm_isdst=0)

print(type(t))
# <class 'time.struct_time'>

print(t.tm_year)
# 2018

print(t.tm_mon)
# 6

print(t.tm_mday)
# 30

print(time.strftime('%Y-%m-%d %H:%M:%S', t))
# 2018-06-30 07:22:01

entries = feedparser.parse('http://gihyo.jp/feed/atom')['entries']

print(type(entries))
# <class 'list'>

print(len(entries))
# 20

entry = entries[0]

print(type(entry))
# <class 'feedparser.FeedParserDict'>

pprint.pprint(entry)
# {'author': '階戸アキラ',
#  'author_detail': {'name': '階戸アキラ'},
#  'authors': [{'name': '階戸アキラ'}],
#  'guidislink': False,
#  'id': 'http://gihyo.jp/admin/clip/01/linux_dt/201806/29',
#  'link': 'http://gihyo.jp/admin/clip/01/linux_dt/201806/29',
#  'links': [{'href': 'http://gihyo.jp/admin/clip/01/linux_dt/201806/29',
#             'rel': 'alternate',
#             'type': 'text/html'}],
#  'published': '2018-06-29T15:46:00+09:00',
#  'published_parsed': time.struct_time(tm_year=2018, tm_mon=6, tm_mday=29, tm_hour=6, tm_min=46, tm_sec=0, tm_wday=4, tm_yday=180, tm_isdst=0),
#  'summary': 'Gentoo '
#             'Linuxは6月28日（世界標準時），同日20時20分に正体不明の何者かによってGitHubのページのコントロールが奪われたことを明らかにした。',
#  'summary_detail': {'base': 'http://gihyo.jp/feed/atom',
#                     'language': None,
#                     'type': 'text/plain',
#                     'value': 'Gentoo '
#                              'Linuxは6月28日（世界標準時），同日20時20分に正体不明の何者かによってGitHubのページのコントロールが奪われたことを明らかにした。'},
#  'tags': [{'label': None,
#            'scheme': 'http://gihyo.jp/admin/clip/01/linux_dt',
#            'term': 'Linux Daily Topics'}],
#  'title': '2018年6月29日\u3000Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics',
#  'title_detail': {'base': 'http://gihyo.jp/feed/atom',
#                   'language': None,
#                   'type': 'text/plain',
#                   'value': '2018年6月29日\u3000Gentoo，GitHubリポジトリを不正ハックされる ── '
#                            'Linux Daily Topics'},
#  'updated': '2018-06-29T15:46:00+09:00',
#  'updated_parsed': time.struct_time(tm_year=2018, tm_mon=6, tm_mday=29, tm_hour=6, tm_min=46, tm_sec=0, tm_wday=4, tm_yday=180, tm_isdst=0)}

d = feedparser.parse('http://gihyo.jp/feed/atom')

urls = [entry['link'] for entry in d['entries']]

pprint.pprint(urls)
# ['http://gihyo.jp/admin/clip/01/linux_dt/201806/29',
#  'http://gihyo.jp/admin/clip/01/ubuntu-topics/201806/29',
#  'http://gihyo.jp/book/pickup/2018/0044',
#  'http://gihyo.jp/book/pickup/2018/0043',
#  'http://gihyo.jp/news/info/2018/06/2801',
#  'http://gihyo.jp/news/nr/2018/06/2801',
#  'http://gihyo.jp/dev/serial/01/continue-power/0012',
#  'http://gihyo.jp/lifestyle/clip/01/awt/201806/28',
#  'http://gihyo.jp/design/clip/01/weekly-web-tech/201806/28',
#  'http://gihyo.jp/book/pickup/2018/0042',
#  'http://gihyo.jp/book/pickup/2018/0041',
#  'http://gihyo.jp/admin/serial/01/ubuntu-recipe/0525',
#  'http://gihyo.jp/dev/serial/01/funny-play-pb/0007',
#  'http://gihyo.jp/book/pickup/2018/0040',
#  'http://gihyo.jp/book/pickup/2018/0039',
#  'http://gihyo.jp/news/info/2018/06/36908',
#  'http://gihyo.jp/news/info/2018/06/36903',
#  'http://gihyo.jp/admin/clip/01/linux_dt/201806/26',
#  'http://gihyo.jp/lifestyle/serial/01/ganshiki-soushi/0099',
#  'http://gihyo.jp/dev/serial/01/mysql-road-construction-news/0074']

titles = [entry['title'] for entry in d['entries']]

pprint.pprint(titles)
# ['2018年6月29日\u3000Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics',
#  '2018年6月29日号\u3000CanonicalのUbuntu Desktop調査，Spectre/Meltdown対策さらにさらにその後・AMD編 '
#  '── Ubuntu Weekly Topics',
#  'Alexaスキル開発の勘所―進化し続けるAlexaの“今”を知る！ ── 新刊ピックアップ',
#  'IT技術変革の軌跡～変わることと変わらないこと～ ── 新刊ピックアップ',
#  '「Python Boot Camp」7/21に茨城県つくば市で開催 ── インフォメーション',
#  'ヌーラボ，オンライン描画ツール「Cacoo」のUIを全面刷新――全世界300万人のユーザから得たUXリサーチ結果を反映 ── ニュースリリース',
#  '最終回\u3000エンジニアはどこに行くのか ── 継続は力なり―大器晩成エンジニアを目指して',
#  '2018年6月第5週\u3000Googleがポッドキャストへ再参入 ── Android Weekly Topics',
#  '2018年6月第4週号 '
#  '1位は，デザイン作業の段階に分けておすすめのUXツールを紹介，気になるネタは，Instagram、YouTubeに対抗する長尺動画サービス「IGTV」提供開始 '
#  '── 週刊Webテク通信',
#  'デジ絵をはじめるなら「クリスタ」で決まり！ ── 新刊ピックアップ',
#  'ほぼほぼ理解！ ブロックチェーンの何が「スゴイ」のか？ ── 新刊ピックアップ',
#  '第525回\u3000Ubuntu 18.04 LTSリリース記念オフラインミーティング フォトレポート ── Ubuntu Weekly Recipe',
#  'File.#007\u3000社内プチミステリ（連載第69回） ── きたみりゅうじの聞かせて珍プレー プレイバック',
#  '正しいコードの書き方とは？～ウェブ業界の即戦力となるHTMLとCSSの記述方法を身につけよう！ ── 新刊ピックアップ',
#  '小さな会社やお店の販促ツールが無料で作れる！ Canvaを始めよう！ ── 新刊ピックアップ',
#  '書籍『統計思考の世界』『系統体系学の世界』刊行記念トークイベント， 7月20日にゲンロンカフェで開催 ── インフォメーション',
#  'Ruby bizグランプリ2018募集開始\u3000応募は9月14日まで ── インフォメーション',
#  '2018年6月26日\u3000Kubernetesこそ未来 ―GitLab，プラットフォームをAzureからGCPへ移行 ── Linux Daily '
#  'Topics',
#  '第99回\u3000Plamo-7.0とSysvinit ── 玩式草子─ソフトウェアとたわむれる日々',
#  '第74回\u3000さまざまなMySQLのバージョンを試す ── MySQL道普請便り']

dicts = [{'url': e['link'], 'title': e['title']} for e in d['entries']]

pprint.pprint(dicts)
# [{'title': '2018年6月29日\u3000Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics',
#   'url': 'http://gihyo.jp/admin/clip/01/linux_dt/201806/29'},
#  {'title': '2018年6月29日号\u3000CanonicalのUbuntu '
#            'Desktop調査，Spectre/Meltdown対策さらにさらにその後・AMD編 ── Ubuntu Weekly Topics',
#   'url': 'http://gihyo.jp/admin/clip/01/ubuntu-topics/201806/29'},
#  {'title': 'Alexaスキル開発の勘所―進化し続けるAlexaの“今”を知る！ ── 新刊ピックアップ',
#   'url': 'http://gihyo.jp/book/pickup/2018/0044'},
#  {'title': 'IT技術変革の軌跡～変わることと変わらないこと～ ── 新刊ピックアップ',
#   'url': 'http://gihyo.jp/book/pickup/2018/0043'},
#  {'title': '「Python Boot Camp」7/21に茨城県つくば市で開催 ── インフォメーション',
#   'url': 'http://gihyo.jp/news/info/2018/06/2801'},
#  {'title': 'ヌーラボ，オンライン描画ツール「Cacoo」のUIを全面刷新――全世界300万人のユーザから得たUXリサーチ結果を反映 ── '
#            'ニュースリリース',
#   'url': 'http://gihyo.jp/news/nr/2018/06/2801'},
#  {'title': '最終回\u3000エンジニアはどこに行くのか ── 継続は力なり―大器晩成エンジニアを目指して',
#   'url': 'http://gihyo.jp/dev/serial/01/continue-power/0012'},
#  {'title': '2018年6月第5週\u3000Googleがポッドキャストへ再参入 ── Android Weekly Topics',
#   'url': 'http://gihyo.jp/lifestyle/clip/01/awt/201806/28'},
#  {'title': '2018年6月第4週号 '
#            '1位は，デザイン作業の段階に分けておすすめのUXツールを紹介，気になるネタは，Instagram、YouTubeに対抗する長尺動画サービス「IGTV」提供開始 '
#            '── 週刊Webテク通信',
#   'url': 'http://gihyo.jp/design/clip/01/weekly-web-tech/201806/28'},
#  {'title': 'デジ絵をはじめるなら「クリスタ」で決まり！ ── 新刊ピックアップ',
#   'url': 'http://gihyo.jp/book/pickup/2018/0042'},
#  {'title': 'ほぼほぼ理解！ ブロックチェーンの何が「スゴイ」のか？ ── 新刊ピックアップ',
#   'url': 'http://gihyo.jp/book/pickup/2018/0041'},
#  {'title': '第525回\u3000Ubuntu 18.04 LTSリリース記念オフラインミーティング フォトレポート ── Ubuntu '
#            'Weekly Recipe',
#   'url': 'http://gihyo.jp/admin/serial/01/ubuntu-recipe/0525'},
#  {'title': 'File.#007\u3000社内プチミステリ（連載第69回） ── きたみりゅうじの聞かせて珍プレー プレイバック',
#   'url': 'http://gihyo.jp/dev/serial/01/funny-play-pb/0007'},
#  {'title': '正しいコードの書き方とは？～ウェブ業界の即戦力となるHTMLとCSSの記述方法を身につけよう！ ── 新刊ピックアップ',
#   'url': 'http://gihyo.jp/book/pickup/2018/0040'},
#  {'title': '小さな会社やお店の販促ツールが無料で作れる！ Canvaを始めよう！ ── 新刊ピックアップ',
#   'url': 'http://gihyo.jp/book/pickup/2018/0039'},
#  {'title': '書籍『統計思考の世界』『系統体系学の世界』刊行記念トークイベント， 7月20日にゲンロンカフェで開催 ── インフォメーション',
#   'url': 'http://gihyo.jp/news/info/2018/06/36908'},
#  {'title': 'Ruby bizグランプリ2018募集開始\u3000応募は9月14日まで ── インフォメーション',
#   'url': 'http://gihyo.jp/news/info/2018/06/36903'},
#  {'title': '2018年6月26日\u3000Kubernetesこそ未来 ―GitLab，プラットフォームをAzureからGCPへ移行 ── '
#            'Linux Daily Topics',
#   'url': 'http://gihyo.jp/admin/clip/01/linux_dt/201806/26'},
#  {'title': '第99回\u3000Plamo-7.0とSysvinit ── 玩式草子─ソフトウェアとたわむれる日々',
#   'url': 'http://gihyo.jp/lifestyle/serial/01/ganshiki-soushi/0099'},
#  {'title': '第74回\u3000さまざまなMySQLのバージョンを試す ── MySQL道普請便り',
#   'url': 'http://gihyo.jp/dev/serial/01/mysql-road-construction-news/0074'}]

print(dicts[0]['url'])
# http://gihyo.jp/admin/clip/01/linux_dt/201806/29

print(dicts[0]['title'])
# 2018年6月29日　Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics

print('\u3000' == '　')
# True

title = d['entries'][0]['title']

print(repr(title))
# '2018年6月29日\u3000Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics'

print(title)
# 2018年6月29日　Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics

print(title.replace('\u3000', ' '))
# 2018年6月29日 Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics

titles_space = [entry['title'].replace('\u3000', ' ') for entry in d['entries']]

pprint.pprint(titles_space)
# ['2018年6月29日 Gentoo，GitHubリポジトリを不正ハックされる ── Linux Daily Topics',
#  '2018年6月29日号 CanonicalのUbuntu Desktop調査，Spectre/Meltdown対策さらにさらにその後・AMD編 ── '
#  'Ubuntu Weekly Topics',
#  'Alexaスキル開発の勘所―進化し続けるAlexaの“今”を知る！ ── 新刊ピックアップ',
#  'IT技術変革の軌跡～変わることと変わらないこと～ ── 新刊ピックアップ',
#  '「Python Boot Camp」7/21に茨城県つくば市で開催 ── インフォメーション',
#  'ヌーラボ，オンライン描画ツール「Cacoo」のUIを全面刷新――全世界300万人のユーザから得たUXリサーチ結果を反映 ── ニュースリリース',
#  '最終回 エンジニアはどこに行くのか ── 継続は力なり―大器晩成エンジニアを目指して',
#  '2018年6月第5週 Googleがポッドキャストへ再参入 ── Android Weekly Topics',
#  '2018年6月第4週号 '
#  '1位は，デザイン作業の段階に分けておすすめのUXツールを紹介，気になるネタは，Instagram、YouTubeに対抗する長尺動画サービス「IGTV」提供開始 '
#  '── 週刊Webテク通信',
#  'デジ絵をはじめるなら「クリスタ」で決まり！ ── 新刊ピックアップ',
#  'ほぼほぼ理解！ ブロックチェーンの何が「スゴイ」のか？ ── 新刊ピックアップ',
#  '第525回 Ubuntu 18.04 LTSリリース記念オフラインミーティング フォトレポート ── Ubuntu Weekly Recipe',
#  'File.#007 社内プチミステリ（連載第69回） ── きたみりゅうじの聞かせて珍プレー プレイバック',
#  '正しいコードの書き方とは？～ウェブ業界の即戦力となるHTMLとCSSの記述方法を身につけよう！ ── 新刊ピックアップ',
#  '小さな会社やお店の販促ツールが無料で作れる！ Canvaを始めよう！ ── 新刊ピックアップ',
#  '書籍『統計思考の世界』『系統体系学の世界』刊行記念トークイベント， 7月20日にゲンロンカフェで開催 ── インフォメーション',
#  'Ruby bizグランプリ2018募集開始 応募は9月14日まで ── インフォメーション',
#  '2018年6月26日 Kubernetesこそ未来 ―GitLab，プラットフォームをAzureからGCPへ移行 ── Linux Daily '
#  'Topics',
#  '第99回 Plamo-7.0とSysvinit ── 玩式草子─ソフトウェアとたわむれる日々',
#  '第74回 さまざまなMySQLのバージョンを試す ── MySQL道普請便り']
