import os
import time
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/list/'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)

soup = BeautifulSoup(html, "html.parser")

url_list = [img.get('data-src') for img in soup.find(class_='list').find_all('img')]

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file, open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)

def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))

download_dir = 'data/temp'
sleep_time_sec = 1

for url in url_list:
#     print(url)
#     download_file_to_dir(url, download_dir)
    time.sleep(sleep_time_sec)
