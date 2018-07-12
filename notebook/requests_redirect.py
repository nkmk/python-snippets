import requests

url = 'https://en.wikipedia.org'

r = requests.get(url)

print(r.url)
# https://en.wikipedia.org/wiki/Main_Page

print(r.status_code)
# 200

print(r.history)
# [<Response [301]>]

print(len(r.history))
# 1

print(type(r.history[0]))
# <class 'requests.models.Response'>

print(r.history[0].url)
# https://en.wikipedia.org/

print(r.history[0].status_code)
# 301

print([response.url for response in r.history])
# ['https://en.wikipedia.org/']

r_not_redirect = requests.get(url, allow_redirects=False)

print(r_not_redirect.url)
# https://en.wikipedia.org/

print(r_not_redirect.status_code)
# 301
