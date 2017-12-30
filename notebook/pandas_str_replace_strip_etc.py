import pandas as pd

s = pd.Series([' a-a-x ', ' b-x-b ', ' x-c-c '])
print(s)
# 0     a-a-x 
# 1     b-x-b 
# 2     x-c-c 
# dtype: object

s_new = s.str.replace('x', 'z')
print(s_new)
# 0     a-a-z 
# 1     b-z-b 
# 2     z-c-c 
# dtype: object

df = pd.DataFrame([[' a-a-x-1 ', ' a-a-x-2 '],
                   [' b-x-b-1 ', ' b-x-b-2 '],
                   [' x-c-c-1 ', ' x-c-c-2 ']],
                  columns=['col1', 'col2'])
print(df)
#         col1       col2
# 0   a-a-x-1    a-a-x-2 
# 1   b-x-b-1    b-x-b-2 
# 2   x-c-c-1    x-c-c-2 

df['col1'] = df['col1'].str.replace('x', 'z')
print(df)
#         col1       col2
# 0   a-a-z-1    a-a-x-2 
# 1   b-z-b-1    b-x-b-2 
# 2   z-c-c-1    x-c-c-2 

s_new = s.str.strip()
print(s_new)
# 0    a-a-x
# 1    b-x-b
# 2    x-c-c
# dtype: object

s_new = s.str.strip(' x')
print(s_new)
# 0     a-a-
# 1    b-x-b
# 2     -c-c
# dtype: object

df['col1'] = df['col1'].str.strip()
print(df)
#       col1       col2
# 0  a-a-z-1   a-a-x-2 
# 1  b-z-b-1   b-x-b-2 
# 2  z-c-c-1   x-c-c-2 

s_new = s.str.lstrip()
print(s_new)
# 0    a-a-x 
# 1    b-x-b 
# 2    x-c-c 
# dtype: object

s_new = s.str.rstrip()
print(s_new)
# 0     a-a-x
# 1     b-x-b
# 2     x-c-c
# dtype: object

s = pd.Series(['Hello World', 'hello world', 'HELLO WORLD'])
print(s)
# 0    Hello World
# 1    hello world
# 2    HELLO WORLD
# dtype: object

s_new = s.str.lower()
print(s_new)
# 0    hello world
# 1    hello world
# 2    hello world
# dtype: object

s_new = s.str.upper()
print(s_new)
# 0    HELLO WORLD
# 1    HELLO WORLD
# 2    HELLO WORLD
# dtype: object

s_new = s.str.capitalize()
print(s_new)
# 0    Hello world
# 1    Hello world
# 2    Hello world
# dtype: object

s_new = s.str.title()
print(s_new)
# 0    Hello World
# 1    Hello World
# 2    Hello World
# dtype: object
