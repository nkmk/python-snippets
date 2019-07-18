from my_package.mod2 import func_same, func_sub
from my_package.sub_package2.sub_mod2 import func_parent, func_parent_sub

func_same()
# from mod2
# -- mod1.func is called

func_sub()
# from mod2
# -- sub_mod1.func1 is called

func_parent()
# from sub_mod2
# -- mod1.func is called

func_parent_sub()
# from sub_mod2
# -- sub_mod1.func1 is called
