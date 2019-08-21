s = 'one two one two one'

print(s.replace('one', 'two').replace('two', 'one'))
# one one one one one

print(s.replace('one', 'X').replace('two', 'one').replace('X', 'two'))
# two one two one two

def swap_str(s_org, s1, s2, temp='*q@w-e~r^'):
    return s_org.replace(s1, temp).replace(s2, s1).replace(temp, s2)

print(swap_str(s, 'one', 'two'))
# two one two one two

print(s.replace('o', 't').replace('t', 'o'))
# one owo one owo one

print(s.translate(str.maketrans({'o': 't', 't': 'o'})))
# tne owt tne owt tne

print(s.translate(str.maketrans('ot', 'to')))
# tne owt tne owt tne
