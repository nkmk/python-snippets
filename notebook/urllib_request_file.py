import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file, open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())
    except urllib.error.URLError as e:
        print(e)

url = 'https://www.python.org/static/img/python-logo.png'
dst_path = 'data/temp/py-logo.png'
download_file(url, dst_path)

def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))

dst_dir = 'data/temp'
download_file_to_dir(url, dst_dir)

url_error = 'https://www.python.org/static/img/python-logo_xxx.png'
download_file_to_dir(url_error, dst_dir)
# HTTP Error 404: Not Found

url_zip = 'https://github.com/nkmk/python-snippets/raw/master/notebook/data/src/sample_header.csv.zip'
download_file_to_dir(url_zip, dst_dir)

url_xlsx = 'https://github.com/nkmk/python-snippets/raw/master/notebook/data/src/sample.xlsx'
download_file_to_dir(url_xlsx, dst_dir)

url_pdf = 'https://github.com/nkmk/python-snippets/raw/master/notebook/data/src/pdf/sample1.pdf'
download_file_to_dir(url_pdf, dst_dir)

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
#     download_file_dir(url, download_dir)
    time.sleep(sleep_time_sec)
# https://example.com/basedir/base_000.jpg
# https://example.com/basedir/base_001.jpg
# https://example.com/basedir/base_002.jpg
# https://example.com/basedir/base_003.jpg
# https://example.com/basedir/base_004.jpg
