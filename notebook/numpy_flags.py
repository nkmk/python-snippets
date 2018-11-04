import numpy as np

a = np.arange(3)

print(a)
# [0 1 2]

print(a.flags)
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : True
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
#   UPDATEIFCOPY : False

print(type(a.flags))
# <class 'numpy.flagsobj'>

print(a.flags.writeable)
# True

print(a.flags['WRITEABLE'])
# True

a[0] = 100

print(a)
# [100   1   2]

a.flags.writeable = False

# a[0] = 0
# ValueError: assignment destination is read-only

a.flags['WRITEABLE'] = False
a.setflags(write=False)

a = np.arange(3)

print(a)
# [0 1 2]

a.flags.writeable = False

a_view = a[1:]

print(a_view)
# [1 2]

print(a_view.flags.writeable)
# False

# a_view[0] = 100
# ValueError: assignment destination is read-only

# a_view.flags.writeable = True
# ValueError: cannot set WRITEABLE flag to True of this array

a.flags.writeable = True

print(a_view.flags.writeable)
# False

a_view.flags.writeable = True

a_view[0] = 100

print(a_view)
# [100   2]

print(a)
# [  0 100   2]

a_view.flags.writeable = False

# a_view[1] = 1
# ValueError: assignment destination is read-only

print(a.flags.writeable)
# True

a[1] = 1

print(a)
# [0 1 2]

print(a_view)
# [1 2]

a.flags.writeable = False

a_copy = a[1:].copy()

print(a_copy)
# [1 2]

print(a_copy.flags.writeable)
# True

a_copy[0] = 100

print(a_copy)
# [100   2]

print(a)
# [0 1 2]
