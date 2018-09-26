import glob
import re

print(glob.glob('temp/**', recursive=True))
# ['temp/', 'temp/file.text', 'temp/abc.txt', 'temp/012.txt', 'temp/dir', 'temp/dir/xyz.text', 'temp/dir/789.txt']

print([p for p in glob.glob('temp/**', recursive=True) if re.search('\d+.txt', p)])
# ['temp/012.txt', 'temp/dir/789.txt']

print([p for p in glob.glob('temp/**', recursive=True) if re.search('/\D{3}.(txt|text)', p)])
# ['temp/abc.txt', 'temp/dir/xyz.text']
