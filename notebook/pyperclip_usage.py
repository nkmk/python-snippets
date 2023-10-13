import pyperclip

pyperclip.copy('text to be copied')
print(pyperclip.paste())
# text to be copied

print(type(pyperclip.paste()))
# <class 'str'>

s = pyperclip.paste()
print(s)
# text to be copied

pyperclip.copy('')
print(pyperclip.waitForPaste())
# some text

pyperclip.copy('original text')
print(pyperclip.waitForPaste())
# original text

pyperclip.copy('original text')
print(pyperclip.waitForNewPaste())
# new text

# pyperclip.waitForNewPaste(5)
# PyperclipTimeoutException: waitForNewPaste() timed out after 5 seconds.

try:
    s = pyperclip.waitForNewPaste(5)
except pyperclip.PyperclipTimeoutException:
    s = 'No change'

print(s)
# No change

pyperclip.copy(100)
print(pyperclip.paste())
# 100

print(type(pyperclip.paste()))
# <class 'str'>

i = int(pyperclip.paste())
print(i)
# 100

print(type(i))
# <class 'int'>
