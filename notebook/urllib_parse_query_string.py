import urllib.parse

url = 'https://example.com?key1=value1&key2=value2'

print(urllib.parse.urlparse(url))
# ParseResult(scheme='https', netloc='example.com', path='', params='', query='key1=value1&key2=value2', fragment='')

qs = urllib.parse.urlparse(url).query
print(qs)
# key1=value1&key2=value2

print(type(qs))
# <class 'str'>

qs = 'key1=value1&key2=value2%201&key2=value2%2F2'

qs_d = urllib.parse.parse_qs(qs)
print(qs_d)
# {'key1': ['value1'], 'key2': ['value2 1', 'value2/2']}

print(type(qs_d))
# <class 'dict'>

qs_l = urllib.parse.parse_qsl(qs)
print(qs_l)
# [('key1', 'value1'), ('key2', 'value2 1'), ('key2', 'value2/2')]

print(type(qs_l))
# <class 'list'>

d = {'key1': 'value=1', 'key2': 'value=2'}

d_qs = urllib.parse.urlencode(d)
print(d_qs)
# key1=value%3D1&key2=value%3D2

print(type(d_qs))
# <class 'str'>

l = [('key1', 'value=1'), ('key2', 'value=2')]

l_qs = urllib.parse.urlencode(l)
print(l_qs)
# key1=value%3D1&key2=value%3D2

print(type(l_qs))
# <class 'str'>

d = {'key1': 'value 1', 'key2': 'value/2'}

print(urllib.parse.urlencode(d))
# key1=value+1&key2=value%2F2

print(urllib.parse.urlencode(d, quote_via=urllib.parse.quote))
# key1=value%201&key2=value%2F2

print(urllib.parse.urlencode(d, safe='/'))
# key1=value+1&key2=value/2

print(urllib.parse.urlencode(d, safe='/', quote_via=urllib.parse.quote))
# key1=value%201&key2=value/2

qs = 'key1=value1&key2=value2_1&key2=value2_2'

qs_d = urllib.parse.parse_qs(qs)
print(qs_d)
# {'key1': ['value1'], 'key2': ['value2_1', 'value2_2']}

print(urllib.parse.urlencode(qs_d))
# key1=%5B%27value1%27%5D&key2=%5B%27value2_1%27%2C+%27value2_2%27%5D

print(urllib.parse.urlencode(qs_d, doseq=True))
# key1=value1&key2=value2_1&key2=value2_2

def update_query(url, key, new_val):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    d[key] = new_val
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

url = 'https://example.com?k1=v1&k2=v2_1&k2=v2_2'

print(update_query(url, 'k1', 'v100'))
# https://example.com?k1=v100&k2=v2_1&k2=v2_2

print(update_query(url, 'k2', 'v2'))
# https://example.com?k1=v1&k2=v2

print(update_query(url, 'k2', ['v2_100', 'v2_200']))
# https://example.com?k1=v1&k2=v2_100&k2=v2_200

print(update_query(url, 'k3', 'v3'))
# https://example.com?k1=v1&k2=v2_1&k2=v2_2&k3=v3

def remove_query(url, key):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    d.pop(key, None)
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

url = 'https://example.com?k1=v1&k2=v2_1&k2=v2_2'

print(remove_query(url, 'k1'))
# https://example.com?k2=v2_1&k2=v2_2

print(remove_query(url, 'k2'))
# https://example.com?k1=v1

print(remove_query(url, 'k3'))
# https://example.com?k1=v1&k2=v2_1&k2=v2_2

def remove_all_queries(url):
    return urllib.parse.urlunparse(urllib.parse.urlparse(url)._replace(query=None))

url = 'https://example.com?k1=v1&k2=v2_1&k2=v2_2'

print(remove_all_queries(url))
# https://example.com
