import glob

print(glob.glob('temp/*.txt'))
# ['temp/abc.txt', 'temp/012.txt']

print(glob.glob('temp/**', recursive=True))
# ['temp/', 'temp/file.text', 'temp/abc.txt', 'temp/012.txt', 'temp/dir', 'temp/dir/xyz.text', 'temp/dir/789.txt']

print(glob.glob('temp/**/*.txt', recursive=True))
# ['temp/abc.txt', 'temp/012.txt', 'temp/dir/789.txt']

print(glob.glob('temp/**/*.text', recursive=True))
# ['temp/file.text', 'temp/dir/xyz.text']

print(glob.glob('temp/**/???.text', recursive=True))
# ['temp/dir/xyz.text']

print(glob.glob('temp/**/[0-9][0-9][0-9].txt', recursive=True))
# ['temp/012.txt', 'temp/dir/789.txt']
