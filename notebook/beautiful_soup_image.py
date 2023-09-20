import os
import time
import urllib.request

os.makedirs('data/temp/yahoo', exist_ok=True)

def download_file_to_dir(url, dst_dir):
    urllib.request.urlretrieve(url, os.path.join(dst_dir, os.path.basename(url)))

from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/list/'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/116.0.0.0 Safari/537.36'

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)

soup = BeautifulSoup(html, "html.parser")

dst_dir = 'data/temp/yahoo'
sleep_time_sec = 1

for img in soup.find(class_='newsFeed_list').find_all('img'):
    url = img.get('src')
    download_file_to_dir(url, dst_dir)
    time.sleep(sleep_time_sec)
