# http://docs.python.jp/3.6/library/urllib.parse.html

import urllib.parse

values = {'key1': 'value1', 'key2': 'バリュー2'}
print(urllib.parse.urlencode(values))
# key1=value1&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

base = 'http://example.com/sub1/index.html'
print(urllib.parse.urljoin(base, 'index2.html'))
print(urllib.parse.urljoin(base, '../../sub2/index.html'))
print(urllib.parse.urljoin(base, 'https://google.com'))
print(urllib.parse.urljoin(base, '//google.com'))
# http://example.com/sub1/index2.html
# http://example.com/sub2/index.html
# https://google.com
# http://google.com

url = 'http://example.com/sub1/index.html?key=value'
o = urllib.parse.urlparse(url)
print(o)
print(o.scheme, o.netloc, o.path)
# ParseResult(scheme='http', netloc='example.com', path='/sub1/index.html', params='', query='key=value', fragment='')
# http example.com /sub1/index.html

relative_url = 'sub/index.html'
o = urllib.parse.urlparse(relative_url)
print(o)
# ParseResult(scheme='', netloc='', path='sub/index.html', params='', query='', fragment='')
