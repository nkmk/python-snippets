from . import mod1
from .sub_package1 import sub_mod1


def func_same():
    print('from mod2')
    mod1.func()


def func_sub():
    print('from mod2')
    sub_mod1.func()


if __name__ == '__main__':
    func_sub()
