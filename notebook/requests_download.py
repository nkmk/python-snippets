import requests
import os

url_image = 'https://www.python.org/static/community_logos/python-logo.png'

r_image = requests.get(url_image)

print(r_image.headers['Content-Type'])
# image/png

filename_image = os.path.basename(url_image)
print(filename_image)
# python-logo.png

with open('data/temp/' + filename_image, 'wb') as f:
    f.write(r_image.content)

url_zip = 'http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/13tokyo.zip'

r_zip = requests.get(url_zip)

print(r_zip.headers['Content-Type'])
# application/zip

filename_zip = os.path.basename(url_zip)
print(filename_zip)
# 13tokyo.zip

with open('data/temp/' + filename_zip, 'wb') as f:
    f.write(r_zip.content)
