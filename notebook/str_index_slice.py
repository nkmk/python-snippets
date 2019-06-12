s = 'abcde'

print(s[0])
# a

print(s[4])
# e

print(s[-1])
# e

print(s[-5])
# a

# print(s[5])
# IndexError: string index out of range

# print(s[-6])
# IndexError: string index out of range

s = 'abcde'

print(s[1:3])
# bc

print(s[:3])
# abc

print(s[1:])
# bcde

print(s[-4:-2])
# bc

print(s[:-2])
# abc

print(s[-4:])
# bcde

print(s[3:1])
# 

print(s[3:1] == '')
# True

print(s[-100:100])
# abcde

print(s[1:4:2])
# bd

print(s[::2])
# ace

print(s[::3])
# ad

print(s[::-1])
# edcba

print(s[::-2])
# eca

s = 'abcdefghi'

print(len(s))
# 9

# print(s[len(s) / 2])
# TypeError: string indices must be integers

print(s[len(s) // 2])
# e

print(s[:len(s) // 2])
# abcd

print(s[len(s) // 2:])
# efghi

s = 'abcあいう'

print(len(s))
# 6

print(s[4])
# い

print(s[1:5])
# bcあい
