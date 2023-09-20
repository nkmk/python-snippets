import urllib.request

url = 'https://www.python.org/static/img/python-logo.png'
dst_path = 'data/temp/py-logo.png'

urllib.request.urlretrieve(url, dst_path)
# ('data/temp/py-logo.png', <http.client.HTTPMessage at 0x102199550>)

def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        with open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())

url = 'https://www.python.org/static/img/python-logo.png'
dst_path = 'data/temp/py-logo.png'

download_file(url, dst_path)

def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file, open(dst_path, 'wb') as local_file:
        local_file.write(web_file.read())

download_file(url, dst_path)

import os

def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))

url = 'https://www.python.org/static/img/python-logo.png'
dst_dir = 'data/temp'

download_file_to_dir(url, dst_dir)

url_error = 'https://www.python.org/static/img/python-logo-abc.png'
dst_path = 'data/temp/py-logo.png'

# download_file(url_error, dst_path)
# HTTPError: HTTP Error 404: Not Found

import urllib.error

try:
    download_file(url_error, dst_path)
except urllib.error.HTTPError as e:
    print(e)
# HTTP Error 404: Not Found

url = 'https://www.python.org/static/img/python-logo.png'
dst_path_error = 'data/not_exist/py-logo.png'

try:
    download_file(url, dst_path_error)
except (urllib.error.HTTPError, FileNotFoundError) as e:
    print(e)
# [Errno 2] No such file or directory: 'data/not_exist/py-logo.png'

url_zip = 'https://github.com/nkmk/python-snippets/raw/master/notebook/data/src/sample_header.csv.zip'
download_file_to_dir(url_zip, dst_dir)

url_pdf = 'https://github.com/nkmk/python-snippets/raw/master/notebook/data/src/pdf/sample1.pdf'
download_file_to_dir(url_pdf, dst_dir)

import time

url_list = ['url_0', 'url_1', 'url_2', 'url_3', 'url_4']
dst_dir = 'data/temp'
sleep_time_sec = 1

for url in url_list:
#     download_file_to_dir(url, dst_dir)
    time.sleep(sleep_time_sec)

dst_dir = 'data/temp'
sleep_time_sec = 1

for i in range(5):
    url = f'https://example.com/dir/base_{i:03}.jpg'
    print(url)
#     download_file_to_dir(url, dst_dir)
    time.sleep(sleep_time_sec)
# https://example.com/dir/base_000.jpg
# https://example.com/dir/base_001.jpg
# https://example.com/dir/base_002.jpg
# https://example.com/dir/base_003.jpg
# https://example.com/dir/base_004.jpg
