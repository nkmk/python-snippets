import csv
import glob
import os
import pprint

from bs4 import BeautifulSoup
import markdown2
import pandas as pd

def get_links_from_md(file_path, markdowner=markdown2.Markdown()):
    with open(file_path) as f:
        md = f.read()
    html = markdowner.convert(md)
    soup = BeautifulSoup(html, 'html.parser')
    l = [[file_path, a.text, a.attrs.get('href')] for a in soup.find_all('a')]
    return l

def get_links_from_md_in_list(file_path_list, markdowner=markdown2.Markdown()):
    l = []
    for path in file_path_list:
        l.extend(get_links_from_md(path, markdowner))
    return l

def get_links_from_md_in_dir(dir_path, markdowner=markdown2.Markdown()):
    return get_links_from_md_in_list(
        glob.glob(os.path.join(dir_path, '**', '*.md'), recursive=True),
        markdowner
    )

with open('data/src/md/test1.md') as f:
    print(f.read())
# [Instagram](https://www.instagram.com/) and [Twitter](https://twitter.com)
# 
# - [[Py] Python.org](https://www.python.org/)
# - [relative link](../test/)
# 

pprint.pprint(get_links_from_md('data/src/md/test1.md'))
# [['data/src/md/test1.md', 'Instagram', 'https://www.instagram.com/'],
#  ['data/src/md/test1.md', 'Twitter', 'https://twitter.com'],
#  ['data/src/md/test1.md', '[Py] Python.org', 'https://www.python.org/'],
#  ['data/src/md/test1.md', 'relative link', '../test/']]

with open('data/src/md/test1.md') as f:
    md = f.read()

markdowner = markdown2.Markdown()
html = markdowner.convert(md)
print(html)
# <p><a href="https://www.instagram.com/">Instagram</a> and <a href="https://twitter.com">Twitter</a></p>
# 
# <ul>
# <li><a href="https://www.python.org/">[Py] Python.org</a></li>
# <li><a href="../test/">relative link</a></li>
# </ul>
# 

l = BeautifulSoup(html, 'html.parser').find_all('a')
pprint.pprint(l)
# [<a href="https://www.instagram.com/">Instagram</a>,
#  <a href="https://twitter.com">Twitter</a>,
#  <a href="https://www.python.org/">[Py] Python.org</a>,
#  <a href="../test/">relative link</a>]

a = l[0]
print(type(a))
# <class 'bs4.element.Tag'>

print(a.attrs)
# {'href': 'https://www.instagram.com/'}

print(a.attrs.get('href'))
# https://www.instagram.com/

print(a.text)
# Instagram

html_en = markdowner.convert('abcde')
print(html_en)
# <p>abcde</p>
# 

print(BeautifulSoup(html_en, 'html.parser'))
# <p>abcde</p>
# 

print(BeautifulSoup(html_en, 'lxml'))
# <html><body><p>abcde</p>
# </body></html>

html_jp = markdowner.convert('あいうえお')
print(html_jp)
# <p>あいうえお</p>
# 

print(BeautifulSoup(html_jp, 'html.parser'))
# <p>あいうえお</p>
# 

print(BeautifulSoup(html_jp, 'lxml'))
# 

print(BeautifulSoup(html_jp.encode(), 'lxml'))
# <html><body><p>あいうえお</p>
# </body></html>

print(BeautifulSoup('<p>abcdeあいうえお</p>', 'lxml'))
# <html><body><p>abcdeあいうえお</p></body></html>

print(BeautifulSoup('<html>' + html_jp + '</html>', 'lxml'))
# <html><body><p>あいうえお</p>
# </body></html>

print(BeautifulSoup('abcde' + html_jp, 'lxml'))
# <html><body><p>abcde</p><p>あいうえお</p>
# </body></html>

pprint.pprint(get_links_from_md_in_list(glob.glob('data/src/md/*.md')))
# [['data/src/md/test2.md', '[Py] Python.org', 'https://www.python.org/'],
#  ['data/src/md/test2.md', 'relative link', '../test/'],
#  ['data/src/md/test1.md', 'Instagram', 'https://www.instagram.com/'],
#  ['data/src/md/test1.md', 'Twitter', 'https://twitter.com'],
#  ['data/src/md/test1.md', '[Py] Python.org', 'https://www.python.org/'],
#  ['data/src/md/test1.md', 'relative link', '../test/']]

pprint.pprint(get_links_from_md_in_dir('data/src/md/'))
# [['data/src/md/test2.md', '[Py] Python.org', 'https://www.python.org/'],
#  ['data/src/md/test2.md', 'relative link', '../test/'],
#  ['data/src/md/test1.md', 'Instagram', 'https://www.instagram.com/'],
#  ['data/src/md/test1.md', 'Twitter', 'https://twitter.com'],
#  ['data/src/md/test1.md', '[Py] Python.org', 'https://www.python.org/'],
#  ['data/src/md/test1.md', 'relative link', '../test/'],
#  ['data/src/md/sub_dir/test_sub.md', 'Instagram', 'https://www.instagram.com/'],
#  ['data/src/md/sub_dir/test_sub.md', 'Twitter', 'https://twitter.com']]

l = get_links_from_md('data/src/md/test1.md')
l.insert(0, ['file', 'anchor text', 'URL'])

with open('data/temp/md_links_csv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)

l = get_links_from_md('data/src/md/test1.md')
df = pd.DataFrame(l, columns=['file', 'anchor text', 'URL'])
print(df)
#                    file      anchor text                         URL
# 0  data/src/md/test1.md        Instagram  https://www.instagram.com/
# 1  data/src/md/test1.md          Twitter         https://twitter.com
# 2  data/src/md/test1.md  [Py] Python.org     https://www.python.org/
# 3  data/src/md/test1.md    relative link                    ../test/

df.to_csv('data/temp/md_links_df.csv', index=False)
