import ntpath

print(ntpath.sep)
# \

print('\\')
# \

print(ntpath.sep is '\\')
# True

file_path = 'c:\\dir\\subdir\\filename.ext'
file_path_raw = r'c:\dir\subdir\filename.ext'

print(file_path == file_path_raw)
# True

print(ntpath.basename(file_path))
# filename.ext

print(ntpath.dirname(file_path))
# c:\dir\subdir

print(ntpath.split(file_path))
# ('c:\\dir\\subdir', 'filename.ext')

print(ntpath.splitdrive(file_path))
# ('c:', '\\dir\\subdir\\filename.ext')

drive_letter = ntpath.splitdrive(file_path)[0][0]

print(drive_letter)
# c

print(ntpath.join('c:', 'dir', 'subdir', 'filename.ext'))
# c:dir\subdir\filename.ext

print(ntpath.join('c:', ntpath.sep, 'dir', 'subdir', 'filename.ext'))
# c:\dir\subdir\filename.ext

print(ntpath.join('c:\\', 'dir', 'subdir', 'filename.ext'))
# c:\dir\subdir\filename.ext
