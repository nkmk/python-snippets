import urllib.parse

s = '日本語'

s_quote = urllib.parse.quote(s)

print(s_quote)
# %E6%97%A5%E6%9C%AC%E8%AA%9E

print(type(s_quote))
# <class 'str'>

b = s.encode()

print(b)
# b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'

print(type(b))
# <class 'bytes'>

print(urllib.parse.quote(b))
# %E6%97%A5%E6%9C%AC%E8%AA%9E

s_quote_sj = urllib.parse.quote(s, encoding='shift-jis')

print(s_quote_sj)
# %93%FA%96%7B%8C%EA

b_sj_quote = urllib.parse.quote(s.encode('shift-jis'))

print(b_sj_quote)
# %93%FA%96%7B%8C%EA

print(s_quote_sj == b_sj_quote)
# True

print(urllib.parse.quote('http://x-y_z.com'))
# http%3A//x-y_z.com

print(urllib.parse.quote('http://x-y_z.com', safe=''))
# http%3A%2F%2Fx-y_z.com

print(urllib.parse.quote('http://x-y_z.com', safe='/:'))
# http://x-y_z.com

print(urllib.parse.quote('+ /'))
# %2B%20/

print(urllib.parse.quote_plus('+ /'))
# %2B+%2F

print(urllib.parse.quote_plus('+ /', safe='+/'))
# ++/

page_title = '日本語'

base_ja = 'https://ja.wikipedia.org/wiki/'

print(base_ja + urllib.parse.quote(page_title))
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E

full_url = 'https://ja.wikipedia.org/wiki/日本語'

print(urllib.parse.quote(full_url, safe=':/'))
# https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E

print(base_ja + urllib.parse.quote('OK コンピューター'))
# https://ja.wikipedia.org/wiki/OK%20%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC

print(base_ja + urllib.parse.quote('OK コンピューター'.replace(' ', '_')))
# https://ja.wikipedia.org/wiki/OK_%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC

print(s_quote)
# %E6%97%A5%E6%9C%AC%E8%AA%9E

print(urllib.parse.unquote(s_quote))
# 日本語

print(s_quote_sj)
# %93%FA%96%7B%8C%EA

print(urllib.parse.unquote(s_quote_sj))
# ���{��

print(urllib.parse.unquote(s_quote_sj, 'shift-jis'))
# 日本語

print(urllib.parse.unquote('a+b'))
# a+b

print(urllib.parse.unquote_plus('a+b'))
# a b

b_unquote = urllib.parse.unquote_to_bytes(s_quote)

print(b_unquote)
# b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'

print(b_unquote.decode())
# 日本語

b_unquote_sj = urllib.parse.unquote_to_bytes(s_quote_sj)

print(b_unquote_sj)
# b'\x93\xfa\x96{\x8c\xea'

print(b_unquote_sj.decode('shift-jis'))
# 日本語
