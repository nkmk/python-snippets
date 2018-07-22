from .. import mod1
from ..sub_package1 import sub_mod1


def func_parent():
    print('from sub mod2')
    mod1.func()


def func_parent_sub():
    print('from sub mod2')
    sub_mod1.func()
