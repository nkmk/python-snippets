import os
import pathlib
import datetime
import time
import platform

p = pathlib.Path('data/temp/test.txt')

p.write_text('test')

time.sleep(10)

p.write_text('update')
# 6

print(p.stat())
# os.stat_result(st_mode=33188, st_ino=8728494137, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1549094615, st_mtime=1549094615, st_ctime=1549094615)

print(type(p.stat()))
# <class 'os.stat_result'>

print(os.stat('data/temp/test.txt'))
# os.stat_result(st_mode=33188, st_ino=8728494137, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1549094615, st_mtime=1549094615, st_ctime=1549094615)

print(type(os.stat('data/temp/test.txt')))
# <class 'os.stat_result'>

print(os.stat(p))
# os.stat_result(st_mode=33188, st_ino=8728494137, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=6, st_atime=1549094615, st_mtime=1549094615, st_ctime=1549094615)

print(type(os.stat(p)))
# <class 'os.stat_result'>

print(p.stat() == os.stat('data/temp/test.txt') == os.stat(p))
# True

st = p.stat()

print(st.st_atime)
# 1549094615.972488

print(st.st_mtime)
# 1549094615.9723485

print(st.st_ctime)
# 1549094615.9723485

print(st.st_birthtime)
# 1549094605.9650702

print(type(st.st_ctime))
# <class 'float'>

print(st.st_ctime_ns)
# 1549094615972348510

print(type(st.st_ctime_ns))
# <class 'int'>

print(os.path.getatime('data/temp/test.txt'))
# 1549094615.972488

print(os.path.getmtime('data/temp/test.txt'))
# 1549094615.9723485

print(os.path.getctime('data/temp/test.txt'))
# 1549094615.9723485

print(os.path.getctime(p))
# 1549094615.9723485

print(os.path.getctime(p) == p.stat().st_ctime)
# True

dt = datetime.datetime.fromtimestamp(p.stat().st_ctime)

print(dt)
# 2019-02-02 17:03:35.972348

print(type(dt))
# <class 'datetime.datetime'>

print(dt.strftime('%Y年%m月%d日 %H:%M:%S'))
# 2019年02月02日 17:03:35

print(dt.isoformat())
# 2019-02-02T17:03:35.972348

print(os.path.getmtime('data/temp/test.txt'))
# 1549094615.9723485

print(p.stat().st_mtime)
# 1549094615.9723485

print(datetime.datetime.fromtimestamp(p.stat().st_mtime))
# 2019-02-02 17:03:35.972348

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

print(creation_date(p))
# 1549094605.9650702

print(datetime.datetime.fromtimestamp(creation_date(p)))
# 2019-02-02 17:03:25.965070
