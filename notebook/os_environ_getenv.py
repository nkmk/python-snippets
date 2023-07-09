import os
import subprocess

print(type(os.environ))
# <class 'os._Environ'>

# print(os.environ)

print(os.environ['LANG'])
# ja_JP.UTF-8

# print(os.environ['NEW_KEY'])
# KeyError: 'NEW_KEY'

print(os.environ.get('LANG'))
# ja_JP.UTF-8

print(os.environ.get('NEW_KEY'))
# None

print(os.environ.get('NEW_KEY', 'default'))
# default

print(os.getenv('LANG'))
# ja_JP.UTF-8

print(os.getenv('NEW_KEY'))
# None

print(os.getenv('NEW_KEY', 'default'))
# default

os.environ['NEW_KEY'] = 'test'

print(os.environ['NEW_KEY'])
# test

os.environ['NEW_KEY'] = 'test2'

print(os.environ['NEW_KEY'])
# test2

# os.environ['NEW_KEY'] = 100
# TypeError: str expected, not int

os.environ['NEW_KEY'] = '100'

print(os.environ.pop('NEW_KEY'))
# 100

print(os.getenv('NEW_KEY'))
# None

# print(os.environ.pop('NEW_KEY'))
# KeyError: 'NEW_KEY'

print(os.environ.pop('NEW_KEY', None))
# None

os.environ['NEW_KEY'] = '100'

del os.environ['NEW_KEY']

print(os.getenv('NEW_KEY'))
# None

# del os.environ['NEW_KEY']
# KeyError: 'NEW_KEY'

print(os.getenv('LANG'))
# ja_JP.UTF-8

print(subprocess.check_output('date', encoding='utf-8'))
# 2023年 7月 9日 日曜日 22時47分58秒 JST
# 

os.environ['LANG'] = 'en_US'

print(subprocess.check_output('date', encoding='utf-8'))
# Sun Jul  9 22:47:58 JST 2023
# 

os.environ['LANG'] = 'ja_JP'

if os.getenv('LANG').startswith('ja'):
    print('こんにちは')
else:
    print('Hello')
# こんにちは

os.environ['LANG'] = 'en_US'

if os.getenv('LANG').startswith('ja'):
    print('こんにちは')
else:
    print('Hello')
# Hello
