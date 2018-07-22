from my_package import mod2
from my_package.sub_package2 import sub_mod2

mod2.func_same()
# from mod2
# mod1, func

mod2.func_sub()
# from mod2
# sub mod1, func1

sub_mod2.func_parent()
# from sub mod2
# mod1, func

sub_mod2.func_parent_sub()
# from sub mod2
# sub mod1, func1
