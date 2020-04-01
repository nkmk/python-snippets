s = '0123456789'

print(s[3:7])
# 3456

print(s[3:-3])
# 3456

print(s[:5])
# 01234

print(s[5:])
# 56789

print(s[:3] + s[6:])
# 0126789

def remove_str_start_end(s, start, end):
    return s[:start] + s[end + 1:]

print(remove_str_start_end(s, 3, 5))
# 0126789

def remove_str_start_length(s, start, length):
    return s[:start] + s[start + length:]

print(remove_str_start_length(s, 3, 5))
# 01289
