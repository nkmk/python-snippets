def if_only(n):
    if n > 0:
        print(f'{n} is positive')

if_only(100)
# 100 is positive

if_only(-100)

def if_else(n):
    if n > 0:
        print(f'{n} is positive')
    else:
        print(f'{n} is negative or zero')

if_else(100)
# 100 is positive

if_else(-100)
# -100 is negative or zero

def if_elif(n):
    if n > 0:
        print(f'{n} is positive')
    elif n == 0:
        print(f'{n} is zero')
    elif n == -1:
        print(f'{n} is minus one')

if_elif(100)
# 100 is positive

if_elif(0)
# 0 is zero

if_elif(-1)
# -1 is minus one

if_elif(-100)

def if_elif_else(n):
    if n > 0:
        print(f'{n} is positive')
    elif n == 0:
        print(f'{n} is zero')
    else:
        print(f'{n} is negative')

if_elif_else(100)
# 100 is positive

if_elif_else(0)
# 0 is zero

if_elif_else(-100)
# -100 is negative

def if_chain(n):
    if 0 < n < 100:
        print(f'0 < {n} < 100')
    else:
        print(f'{n} <= 0 or 100 <= {n}')

if_chain(50)
# 0 < 50 < 100

if_chain(1000)
# 1000 <= 0 or 100 <= 1000

def if_in(s):
    if 'a' in s:
        print(f'"a" is in "{s}"')
    else:
        print(f'"a" is NOT in "{s}"')

if_in('apple')
# "a" is in "apple"

if_in('cherry')
# "a" is NOT in "cherry"

def if_startswith(s):
    if s.startswith('a'):
        print(f'"{s}" starts with "a"')
    else:
        print(f'"{s}" does NOT starts with "a"')

if_startswith("apple")
# "apple" starts with "a"

if_startswith("banana")
# "banana" does NOT starts with "a"

if 100:
    print('True')
# True

if [0, 1, 2]:
    print('True')
# True

def if_is_empty(l):
    if l:
        print(f'{l} is NOT empty')
    else:
        print(f'{l} is empty')

if_is_empty([0, 1, 2])
# [0, 1, 2] is NOT empty

if_is_empty([])
# [] is empty

def if_and(n):
    if n > 0 and n % 2 == 0:
        print(f'{n} is positive-even')
    else:
        print(f'{n} is NOT positive-even')

if_and(10)
# 10 is positive-even

if_and(5)
# 5 is NOT positive-even

if_and(-10)
# -10 is NOT positive-even

def if_and_or(n):
    if n > 0 and n % 2 == 0 or n == 0:
        print(f'{n} is positive-even or zero')
    else:
        print(f'{n} is NOT positive-even or zero')

if_and_or(10)
# 10 is positive-even or zero

if_and_or(5)
# 5 is NOT positive-even or zero

if_and_or(0)
# 0 is positive-even or zero

def if_not(s):
    if not s.startswith('a'):
        print(f'"{s}" does NOT starts with "a"')
    else:
        print(f'"{s}" starts with "a"')

if_not("apple")
# "apple" starts with "a"

if_not("banana")
# "banana" does NOT starts with "a"

def too_long_name_function_1():
    return True

def too_long_name_function_2():
    return True

def too_long_name_function_3():
    return True

def if_no_newline():
    if too_long_name_function_1() and too_long_name_function_2() and too_long_name_function_3():
        print('True')
    else:
        print('False')

def if_backslash():
    if too_long_name_function_1() \
       and too_long_name_function_2() \
       and too_long_name_function_3():
        print('True')
    else:
        print('False')

def if_parentheses():
    if (
        too_long_name_function_1()
        and too_long_name_function_2()
        and too_long_name_function_3()
    ):
        print('True')
    else:
        print('False')

if_no_newline()
# True

if_backslash()
# True

if_parentheses()
# True
