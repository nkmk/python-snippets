import urllib.parse

url = 'https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch'

print(urllib.parse.urlparse(url))
# ParseResult(scheme='https', netloc='www.google.co.jp', path='/search', params='', query='q=%E6%A1%9C&tbm=isch', fragment='')

qs = urllib.parse.urlparse(url).query

print(qs)
# q=%E6%A1%9C&tbm=isch

print(type(qs))
# <class 'str'>

qs_d = urllib.parse.parse_qs(qs)

print(qs_d)
# {'q': ['桜'], 'tbm': ['isch']}

print(type(qs_d))
# <class 'dict'>

print(qs_d['q'])
# ['桜']

print(type(qs_d['q']))
# <class 'list'>

print(qs_d['q'][0])
# 桜

print(type(qs_d['q'][0]))
# <class 'str'>

qs_l = urllib.parse.parse_qsl(qs)

print(qs_l)
# [('q', '桜'), ('tbm', 'isch')]

print(type(qs_l))
# <class 'list'>

print(qs_l[0])
# ('q', '桜')

print(type(qs_l[0]))
# <class 'tuple'>

print(qs_l[0][1])
# 桜

print(type(qs_l[0][1]))
# <class 'str'>

d = {'key1': 'value / one', 'key2': 'バリュー2'}

d_qs = urllib.parse.urlencode(d)

print(d_qs)
# key1=value+%2F+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(type(d_qs))
# <class 'str'>

l = [('key1', 'value / one'), ('key2', 'バリュー2')]

l_qs = urllib.parse.urlencode(l)

print(l_qs)
# key1=value+%2F+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(type(l_qs))
# <class 'str'>

print(urllib.parse.urlencode(d))
# key1=value+%2F+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(urllib.parse.urlencode(d, quote_via=urllib.parse.quote))
# key1=value%20%2F%20one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(urllib.parse.urlencode(d, safe='/'))
# key1=value+/+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(urllib.parse.urlencode(d, safe='/', quote_via=urllib.parse.quote))
# key1=value%20/%20one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(qs_d)
# {'q': ['桜'], 'tbm': ['isch']}

print(urllib.parse.urlencode(qs_d))
# q=%5B%27%E6%A1%9C%27%5D&tbm=%5B%27isch%27%5D

print(urllib.parse.urlencode(qs_d, doseq=True))
# q=%E6%A1%9C&tbm=isch

print(url)
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch

print(url.replace('isch', 'vid'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=vid

def update_query(url, key, org_val, new_val):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    l = d.get(key)
    if l:
        d[key] = [new_val if v == org_val else v for v in l]
    else:
        d[key] = new_val
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

print(update_query(url, 'tbm', 'isch', 'vid'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=vid

print(update_query(url, 'q', '桜', '梅'))
# https://www.google.co.jp/search?q=%E6%A2%85&tbm=isch

print(update_query(url, 'new-key', 'xxx', 'yyy'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch&new-key=yyy

def remove_query(url, key):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    d.pop(key, None)
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

print(remove_query(url, 'tbm'))
# https://www.google.co.jp/search?q=%E6%A1%9C

print(remove_query(url, 'new-key'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch

def remove_all_query(url):
    return urllib.parse.urlunparse(urllib.parse.urlparse(url)._replace(query=None))

print(remove_all_query(url))
# https://www.google.co.jp/search
