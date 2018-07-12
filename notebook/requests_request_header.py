import requests

url = 'https://www.yahoo.co.jp/'

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

headers = {'User-Agent': ua}

r_ua = requests.get(url, headers=headers)
