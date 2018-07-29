python3 test_main.py
# This is test_main.py
# test_module.__name__ is test_module
# ---
# call test_module.func()
#     This is func() in test_module.py
#     __name__ is test_module

python3 test_module.py
# Start if __name__ == '__main__'
# call func()
#     This is func() in test_module.py
#     __name__ is __main__

python3 -m test_module
# Start if __name__ == '__main__'
# call func()
#     This is func() in test_module.py
#     __name__ is __main__

python3 hello.py

python3 hello_if_name.py
# Hello!
# __name__ is __main__

python3 add_module.py 1.2 3.4
# 4.6

python3 add_module_command.py 1.2 3.4
# 4.6

python3 add_module_argparse.py 1.2 3.4
# 4.6

python3 hello_main.py
# Hello!

python3 hello_direct.py
# Hello!
