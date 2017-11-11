python3 doctest_example.py

python3 doctest_example_error.py
# **********************************************************************
# File "doctest_example_error.py", line 3, in __main__.add
# Failed example:
#     add(1, 2)
# Expected:
#     3
# Got:
#     2
# **********************************************************************
# File "doctest_example_error.py", line 5, in __main__.add
# Failed example:
#     add(5, 10)
# Expected:
#     10
# Got:
#     50
# **********************************************************************
# 1 items had failures:
#    2 of   2 in __main__.add
# ***Test Failed*** 2 failures.

python3 doctest_example.py -v
# Trying:
#     add(1, 2)
# Expecting:
#     3
# ok
# Trying:
#     add(5, 10)
# Expecting:
#     15
# ok
# 1 items had no tests:
#     __main__
# 1 items passed all tests:
#    2 tests in __main__.add
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.

python3 doctest_example_verbose.py
# Trying:
#     add(1, 2)
# Expecting:
#     3
# ok
# Trying:
#     add(5, 10)
# Expecting:
#     15
# ok
# 1 items had no tests:
#     __main__
# 1 items passed all tests:
#    2 tests in __main__.add
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.

python3 doctest_example_without_import.py 3 4
# 7

python3 -m doctest doctest_example_without_import.py

python3 -m doctest -v doctest_example_without_import.py
# Trying:
#     add(1, 2)
# Expecting:
#     3
# ok
# Trying:
#     add(5, 10)
# Expecting:
#     15
# ok
# 1 items had no tests:
#     doctest_example_without_import
# 1 items passed all tests:
#    2 tests in doctest_example_without_import.add
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.

python3 doctest_example_testfile.py

python3 doctest_example_testfile.py -v
# Trying:
#     from doctest_example import add
# Expecting nothing
# ok
# Trying:
#     add(1, 2)
# Expecting:
#     3
# ok
# Trying:
#     add(5, 10)
# Expecting:
#     15
# ok
# 1 items passed all tests:
#    3 tests in doctest_text.txt
# 3 tests in 1 items.
# 3 passed and 0 failed.
# Test passed.

python3 -m doctest -v doctest_text.txt
# Trying:
#     from doctest_example import add
# Expecting nothing
# ok
# Trying:
#     add(1, 2)
# Expecting:
#     3
# ok
# Trying:
#     add(5, 10)
# Expecting:
#     15
# ok
# 1 items passed all tests:
#    3 tests in doctest_text.txt
# 3 tests in 1 items.
# 3 passed and 0 failed.
# Test passed.
