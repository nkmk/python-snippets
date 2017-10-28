# http://docs.python.jp/3.6/library/urllib.request.html

import urllib.request

url = "https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png"
path = "data/src/lena_square.png"

result = urllib.request.urlretrieve(url, path)
print(result)
# ('data/src/lena_square.png', <http.client.HTTPMessage object at 0x10cce6cf8>)

data = urllib.request.urlopen(url).read()
with open(path, mode="wb") as f:
    f.write(data)
