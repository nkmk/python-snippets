import textwrap

s = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages"

s_wrap_list = textwrap.wrap(s, 40)
print(s_wrap_list)
# ['Python can be easy to pick up whether', "you're a first time programmer or you're", 'experienced with other languages']

print('\n'.join(s_wrap_list))
# Python can be easy to pick up whether
# you're a first time programmer or you're
# experienced with other languages

print(textwrap.fill(s, 40))
# Python can be easy to pick up whether
# you're a first time programmer or you're
# experienced with other languages

print(textwrap.wrap(s, 40, max_lines=2))
# ['Python can be easy to pick up whether', "you're a first time programmer or [...]"]

print(textwrap.fill(s, 40, max_lines=2))
# Python can be easy to pick up whether
# you're a first time programmer or [...]

print(textwrap.fill(s, 40, max_lines=2, placeholder=' ~'))
# Python can be easy to pick up whether
# you're a first time programmer or ~

print(textwrap.fill(s, 40, max_lines=2, placeholder=' ~', initial_indent='  '))
#   Python can be easy to pick up whether
# you're a first time programmer or ~

s = 'あいうえお、かきくけこ、12345,67890, さしすせそ、abcde'

print(textwrap.fill(s, 12))
# あいうえお、かきくけこ、
# 12345,67890,
# さしすせそ、abcde

s = 'Python is powerful'

print(textwrap.shorten(s, 12))
# Python [...]

print(textwrap.shorten(s, 12, placeholder=' ~'))
# Python is ~

s = 'Pythonについて。Pythonは汎用のプログラミング言語である。'

print(textwrap.shorten(s, 20))
# [...]

s_short = s[:12] + '...'
print(s_short)
# Pythonについて。P...

tw = textwrap.TextWrapper(width=30, max_lines=3, placeholder=' ~', initial_indent='  ')

s = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages"

print(tw.wrap(s))
# ['  Python can be easy to pick', "up whether you're a first time", "programmer or you're ~"]

print(tw.fill(s))
#   Python can be easy to pick
# up whether you're a first time
# programmer or you're ~

tw.placeholder = ' ...'
tw.initial_indent = ''

print(tw.fill(s))
# Python can be easy to pick up
# whether you're a first time
# programmer or you're ...
