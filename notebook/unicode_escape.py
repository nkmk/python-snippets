s = 'あいうえお'

b = s.encode('unicode-escape')

print(b)
# b'\\u3042\\u3044\\u3046\\u3048\\u304a'

print(type(b))
# <class 'bytes'>

s_from_b = b.decode('unicode-escape')

print(s_from_b)
# あいうえお

print(type(s_from_b))
# <class 'str'>

s_from_b_error = b.decode('utf-8')

print(s_from_b_error)
# \u3042\u3044\u3046\u3048\u304a

print(type(s_from_b_error))
# <class 'str'>

s_from_s = s_from_b_error.encode().decode('unicode-escape')

print(s_from_s)
# あいうえお

print(type(s_from_s))
# <class 'str'>

import codecs

s_from_s_codecs = codecs.decode(s_from_b_error, 'unicode-escape')

print(s_from_s_codecs)
# あいうえお

print(type(s_from_s_codecs))
# <class 'str'>

s_ascii = ascii('あ')

print(s_ascii)
# '\u3042'

print(type(s_ascii))
# <class 'str'>

print(s_ascii[0])
# '

print(s_ascii[-1])
# '

print(len(s_ascii))
# 8

print(ascii('あ') == "'\\u3042'")
# True

s_unicode_escape = ascii('あ')[1:-1]

print(s_unicode_escape)
# \u3042

print(type(s_unicode_escape))
# <class 'str'>

print(s_unicode_escape == '\\u3042')
# True

print('\u3042')
# あ

print(len('\u3042'))
# 1

print('\u3042' == 'あ')
# True

print('\\u3042')
# \u3042

print(r'\u3042')
# \u3042

print(len(r'\u3042'))
# 6

with open('data/src/unicode_escape.txt') as f:
    s = f.read()
    print(s)
    print(type(s))
    print(len(s))
# \u3042\u3044\u3046\u3048\u304a
# <class 'str'>
# 30

with open('data/src/unicode_escape.txt', encoding='unicode-escape') as f:
    s = f.read()
    print(s)
    print(type(s))
    print(len(s))
# あいうえお
# <class 'str'>
# 5

b_json = b'{"a": "\u3042"}'

print(b_json)
# b'{"a": "\\u3042"}'

print(b_json.decode())
# {"a": "\u3042"}

print(b_json.decode('unicode-escape'))
# {"a": "あ"}

import json

print(json.loads(b_json.decode()))
# {'a': 'あ'}

print(type(json.loads(b_json.decode())))
# <class 'dict'>

print(json.loads(b_json))
# {'a': 'あ'}
