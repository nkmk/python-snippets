l = ['Alice', 'Bob', 'Charlie']

print([s.strip('bce') for s in l])
# ['Ali', 'Bo', 'Charli']

print([s[:2] for s in l])
# ['Al', 'Bo', 'Ch']

s = 'Alice\nBob\nCharlie'
print(s)
# Alice
# Bob
# Charlie

print(s.replace('li', ''))
# Ace
# Bob
# Chare

print(s.strip('bce'))
# Alice
# Bob
# Charli

print(s[2:-2])
# ice
# Bob
# Charl

l_s = s.splitlines()
print(l_s)
# ['Alice', 'Bob', 'Charlie']

l_s_strip = [line.strip('bce') for line in l_s]
print(l_s_strip)
# ['Ali', 'Bo', 'Charli']

s_line_strip = '\n'.join(l_s_strip)
print(s_line_strip)
# Ali
# Bo
# Charli

print('\n'.join([line[:2] for line in s.splitlines()]))
# Al
# Bo
# Ch

l_remove = [line for line in s.splitlines() if not line.startswith('B')]
print(l_remove)
# ['Alice', 'Charlie']

s_line_remove = '\n'.join(l_remove)
print(s_line_remove)
# Alice
# Charlie

print('\n'.join([line for line in s.splitlines() if 'li' in line]))
# Alice
# Charlie
