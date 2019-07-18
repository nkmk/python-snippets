import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import mod1
from dir_for_mod import mod2

mod1.func()
mod2.func()
