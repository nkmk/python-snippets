import pprint
import re

def get_links_from_md_regex(file_path, p=re.compile(r'\[(.+?)\]\((.+?)\)')):
    l = []
    with open(file_path) as f:
        for i, line in enumerate(f):
            for result in p.findall(line):
                l.append([file_path, i + 1, result[0], result[1]])
    return l

pprint.pprint(get_links_from_md_regex('data/src/md/test1.md'))
# [['data/src/md/test1.md', 1, 'Instagram', 'https://www.instagram.com/'],
#  ['data/src/md/test1.md', 1, 'Twitter', 'https://twitter.com'],
#  ['data/src/md/test1.md', 3, '[Py] Python.org', 'https://www.python.org/'],
#  ['data/src/md/test1.md', 4, 'relative link', '../test/']]

s = '[text](URL_with())'

p1 = re.compile(r'\[(.+?)\]\((.+?)\)')
print(p1.findall(s))
# [('text', 'URL_with(')]

p2 = re.compile(r'\[(.+?)\]\((.+)\)')
print(p2.findall(s))
# [('text', 'URL_with()')]

s_inline = '[text](URL_with()) and [text2](URL2)'

print(p2.findall(s_inline))
# [('text', 'URL_with()) and [text2](URL2')]

p3 = re.compile(r"\[(.+?)\]\(([a-zA-Z0-9-._~:/?#@!$&'()*+,;=%]+)\)")
print(p3.findall(s))
# [('text', 'URL_with()')]

print(p3.findall(s_inline))
# [('text', 'URL_with()'), ('text2', 'URL2')]

s_jp = '[text](日本語URL)'

print(p1.findall(s_jp))
# [('text', '日本語URL')]

print(p2.findall(s_jp))
# [('text', '日本語URL')]

print(p3.findall(s_jp))
# []

p4 = re.compile(r"\[(.+?)\]\(([a-zA-Z0-9-._~:/?#@!$&'()*+,;=%\w]+)\)")
print(p4.findall(s_jp))
# [('text', '日本語URL')]

s_jp_inline = '[text](日本語URL)と括弧(xxx)。'

print(p1.findall(s_jp_inline))
# [('text', '日本語URL')]

print(p2.findall(s_jp_inline))
# [('text', '日本語URL)と括弧(xxx')]

print(p3.findall(s_jp_inline))
# []

print(p4.findall(s_jp_inline))
# [('text', '日本語URL)と括弧(xxx')]

p_title = re.compile(r'\[(.+?)\]\(([a-zA-Z0-9-._~:/?#@!$&\'()*+,;=%\w]+)( "(.+)")?\)')

print(p_title.findall('[text](URL "title")'))
# [('text', 'URL', ' "title"', 'title')]

print(p_title.findall('[text](URL)'))
# [('text', 'URL', '', '')]
