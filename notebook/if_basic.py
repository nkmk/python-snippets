def if_test(num):
    if num > 100:
        print('100 < num')
    elif num > 50:
        print('50 < num <= 100')
    elif num > 0:
        print('0 < num <= 50')
    elif num == 0:
        print('num == 0')
    else:
        print('num < 0')

if_test(1000)
# 100 < num

if_test(70)
# 50 < num <= 100

if_test(0)
# num == 0

if_test(-100)
# num < 0

def if_test2(num):
    if 50 < num < 100:
        print('50 < num < 100')
    else:
        print('num <= 50 or num >= 100')

if_test2(70)
# 50 < num < 100

if_test2(0)
# num <= 50 or num >= 100

def if_test_in(s):
    if 'a' in s:
        print('a is in string')
    else:
        print('a is NOT in string')

if_test_in('apple')
# a is in string

if_test_in('melon')
# a is NOT in string

if 10:
    print('True')
# True

if [0, 1, 2]:
    print('True')
# True

print(bool(10))
# True

print(bool(0.0))
# False

print(bool([]))
# False

print(bool('False'))
# True

def if_test_list(l):
    if l:
        print('list is NOT empty')
    else:
        print('list is empty')

if_test_list([0, 1, 2])
# list is NOT empty

if_test_list([])
# list is empty

def if_test_and_not(num):
    if num >= 0 and not num % 2 == 0:
        print('num is positive odd')
    else:
        print('num is NOT positive odd')

if_test_and_not(5)
# num is positive odd

if_test_and_not(10)
# num is NOT positive odd

if_test_and_not(-10)
# num is NOT positive odd

def if_test_and_not_or(num):
    if num >= 0 and not num % 2 == 0 or num == -10:
        print('num is positive odd or -10')
    else:
        print('num is NOT positive odd or -10')

if_test_and_not_or(5)
# num is positive odd or -10

if_test_and_not_or(10)
# num is NOT positive odd or -10

if_test_and_not_or(-10)
# num is positive odd or -10

def if_test_and_backslash(num):
    if num >= 0 \
       and not num % 2 == 0:
        print('num is positive odd')
    else:
        print('num is NOT positive odd')

if_test_and_backslash(5)
# num is positive odd

def if_test_and_brackets(num):
    if (num >= 0
        and not num % 2 == 0):
        print('num is positive odd')
    else:
        print('num is NOT positive odd')

if_test_and_brackets(5)
# num is positive odd
