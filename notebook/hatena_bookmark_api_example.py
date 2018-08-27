import requests

url = 'https://note.nkmk.me'

hb_count = 'http://api.b.st-hatena.com/entry.count'

r = requests.get(hb_count, params={'url': url})

print(r.url)
# http://api.b.st-hatena.com/entry.count?url=https%3A%2F%2Fnote.nkmk.me

print(r.text)
# 5

print(type(r.text))
# <class 'str'>

print(int(r.text))
# 5

print(type(int(r.text)))
# <class 'int'>

hb_counts = 'http://api.b.st-hatena.com/entry.counts'

r = requests.get(hb_counts, params={'url': ['https://www.google.co.jp', 'https://www.yahoo.co.jp']})

print(r.url)
# http://api.b.st-hatena.com/entry.counts?url=https%3A%2F%2Fwww.google.co.jp&url=https%3A%2F%2Fwww.yahoo.co.jp

j = r.json()

print(j)
# {'https://www.google.co.jp': 1385, 'https://www.yahoo.co.jp': 313}

print(type(j))
# <class 'dict'>

hb_total_count = 'http://api.b.st-hatena.com/entry.total_count'

r = requests.get(hb_total_count, params={'url': url})

print(r.url)
# http://api.b.st-hatena.com/entry.total_count?url=https%3A%2F%2Fnote.nkmk.me

j = r.json()

print(j)
# {'url': 'https://note.nkmk.me', 'total_bookmarks': 324}

print(j['total_bookmarks'])
# 324

hb_entry = 'http://b.hatena.ne.jp/entry/jsonlite/'

r = requests.get(hb_entry, params={'url': url})

print(r.url)
# http://b.hatena.ne.jp/entry/jsonlite/?url=https%3A%2F%2Fnote.nkmk.me

j = r.json()

import pprint

pprint.pprint(j)
# {'bookmarks': [{'comment': '',
#                 'tags': ['*Python'],
#                 'timestamp': '2018/06/02 10:52',
#                 'user': 'pkdick'},
#                {'comment': '',
#                 'tags': [],
#                 'timestamp': '2018/05/22 16:24',
#                 'user': 'ilford400'},
#                {'comment': '',
#                 'tags': ['python'],
#                 'timestamp': '2018/05/02 14:12',
#                 'user': 'yem3399op'}],
#  'count': 5,
#  'eid': '356280517',
#  'entry_url': 'http://b.hatena.ne.jp/entry/s/note.nkmk.me/',
#  'screenshot': 'http://b.hatena.ne.jp/images/v4/public/common/noimage.png',
#  'title': 'nkmk note',
#  'url': 'https://note.nkmk.me/'}

print(type(j['bookmarks']))
# <class 'list'>

print(type(j['bookmarks'][0]))
# <class 'dict'>

for b in j['bookmarks']:
    print(b['timestamp'])
# 2018/06/02 10:52
# 2018/05/22 16:24
# 2018/05/02 14:12
