import os
import time
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/photo/'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)

soup = BeautifulSoup(html, "html.parser")

img_list = soup.find(class_='headline').find_all('img')
url_list = []
for img in img_list:
    url_list.append(img.get('src'))

def download_image(url, dst_path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode='wb') as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

download_dir = 'data/temp'
sleep_time_sec = 1

for url in url_list:
    filename = os.path.basename(url)
    dst_path = os.path.join(download_dir, filename)
    time.sleep(sleep_time_sec)
    print(url, dst_path)
    download_image(url, dst_path)
# https://giwiz-newstop.c.yimg.jp/im_siggecJNKV0BleHsiAnBMXsewQ---x223-y122-n0-pril-exp30d/q/amd/20171121-00010002-esquire-000-1-view.jpg data/temp/20171121-00010002-esquire-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggric32PEeS_iH0vtb0LCUZQ---x192-y122-n0-pril-exp30d/q/amd/20171121-00010006-mensplus-000-1-view.jpg data/temp/20171121-00010006-mensplus-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggdu75GDeqZ7B_Eh0pxdKKeg---x161-y122-n0-pril-exp30d/q/amd/20171121-00000023-mnet-000-0-thumb.jpg data/temp/20171121-00000023-mnet-000-0-thumb.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggWLXlL2dWHrPr.mrrLLkL9w---x192-y108-n0-pril-exp30d/q/amd/20171121-00000006-ignjapan-000-1-view.jpg data/temp/20171121-00000006-ignjapan-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggeyzG3wHHU0NxUvrp0xPvPg---x192-y108-n0-pril-exp30d/q/amd/20171121-00010006-giz-000-1-view.jpg data/temp/20171121-00010006-giz-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggXn_6JufQa4Orbdr3IEWONA---x192-y108-n0-pril-exp30d/q/amd/20171121-00010003-biz_lifeh-000-1-view.jpg data/temp/20171121-00010003-biz_lifeh-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggSGvaG83y7pmaqZg2Bsxl4Q---x213-y120-n0-pril-exp30d/q/amd/20171121-00010021-abema-000-1-view.jpg data/temp/20171121-00010021-abema-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_sigg7rXGpJA7JHwJHGSJzWPBRA---x180-y120-n0-pril-exp30d/q/amd/20171121-00010003-binsider-000-1-view.jpg data/temp/20171121-00010003-binsider-000-1-view.jpg
# https://giwiz-newstop.c.yimg.jp/im_siggbZPC5gZWE944mVVJ7w2xEw---x179-y119-n0-pril-exp30d/q/amd/20171121-00085892-esse-000-1-view.jpg data/temp/20171121-00085892-esse-000-1-view.jpg
