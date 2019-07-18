import mod1

mod1.func()
# -- mod1.func is called

from mod1 import func

func()
# -- mod1.func is called

import dir_for_mod.mod2

dir_for_mod.mod2.func()
# -- dir_for_mod.mod2.func is called

from dir_for_mod import mod2

mod2.func()
# -- dir_for_mod.mod2.func is called

from dir_for_mod.mod2 import func

func()
# -- dir_for_mod.mod2.func is called
