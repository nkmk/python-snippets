for i in range(3):
    print(i)
# 0
# 1
# 2

def test(n):
    for i in range(n):
        if i % 2:
            print(i * 10)
        else:
            print(i)
    print('FINISH')

test(5)
# 0
# 10
# 2
# 30
# 4
# FINISH

def test(n):
 for i in range(n):
   if i % 2:
                print(i * 10)
   else:
    print(i)
 print('FINISH')

test(5)
# 0
# 10
# 2
# 30
# 4
# FINISH

# def test(n):
#  for i in range(n):
#    if i % 2:
#                 print(i * 10)
#      else:
#        print(i)
#  print('FINISH')
# IndentationError: unindent does not match any outer indentation level

def test(n):
    print(n)

test(5)
# 5

def test(n):print(n)

test(5)
# 5

def test(n):
    n += 10
    print(n)
    print('FINISH')

test(5)
# 15
# FINISH

def test(n):n += 10;print(n);print('FINISH')

test(5)
# 15
# FINISH

def test(n):
    for i in range(n):
        print(i)

test(3)
# 0
# 1
# 2

# def test(n):for i in range(n):print(i)
# SyntaxError: invalid syntax

def test(n):
    for i in range(n):print(i)

test(3)
# 0
# 1
# 2
