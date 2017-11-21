import os
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

url = 'https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png'
dst_path = 'data/src/lena_square.png'
# dst_dir = 'data/src'
# dst_path = os.path.join(dst_dir, os.path.basename(url))
download_image(url, dst_path)

error_url = 'https://upload.wikimedia.org/wikipedia/en/2/24/Lenna_xxx.png'
download_image(error_url, dst_path)
# HTTP Error 404: Not Found

url_list = []
for i in range(5):
    url = 'http://example.com/basedir/base_{:03}.jpg'.format(i)
    url_list.append(url)

download_dir = 'temp/dir'
sleep_time_sec = 1

for url in url_list:
    filename = os.path.basename(url)
    dst_path = os.path.join(download_dir, filename)
    time.sleep(sleep_time_sec)
    print(url, dst_path)
    # download_image(url, dst_path)
# http://example.com/basedir/base_000.jpg temp/dir/base_000.jpg
# http://example.com/basedir/base_001.jpg temp/dir/base_001.jpg
# http://example.com/basedir/base_002.jpg temp/dir/base_002.jpg
# http://example.com/basedir/base_003.jpg temp/dir/base_003.jpg
# http://example.com/basedir/base_004.jpg temp/dir/base_004.jpg
