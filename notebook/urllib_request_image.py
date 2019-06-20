import os
import pprint
import time
import urllib.error
import urllib.request

def download_image(url, dst_path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

url = 'https://www.python.org/static/img/python-logo.png'
dst_path = 'data/temp/py-logo.png'

download_image(url, dst_path)

def download_image_dir(url, dst_dir):
    download_image(url, os.path.join(dst_dir, os.path.basename(url)))

dst_dir = 'data/temp'

download_image_dir(url, dst_dir)

error_url = 'https://www.python.org/static/img/python-logo_xxx.png'
download_image(error_url, dst_path)
# HTTP Error 404: Not Found

url_list = ['https://example.com/basedir/base_{:03}.jpg'.format(i) for i in range(5)]

pprint.pprint(url_list)
# ['https://example.com/basedir/base_000.jpg',
#  'https://example.com/basedir/base_001.jpg',
#  'https://example.com/basedir/base_002.jpg',
#  'https://example.com/basedir/base_003.jpg',
#  'https://example.com/basedir/base_004.jpg']

download_dir = 'data/temp'
sleep_time_sec = 1

for url in url_list:
    print(url)
#     download_image_dir(url, download_dir)
    time.sleep(sleep_time_sec)
# https://example.com/basedir/base_000.jpg
# https://example.com/basedir/base_001.jpg
# https://example.com/basedir/base_002.jpg
# https://example.com/basedir/base_003.jpg
# https://example.com/basedir/base_004.jpg
