a = 1
result = 'even' if a % 2 == 0 else 'odd'
print(result)
# odd

a = 2
result = 'even' if a % 2 == 0 else 'odd'
print(result)
# even

a = -2
result = 'negative and even' if a < 0 and a % 2 == 0 else 'positive or odd'
print(result)
# negative and even

a = -1
result = 'negative and even' if a < 0 and a % 2 == 0 else 'positive or odd'
print(result)
# positive or odd

a = 2
result = 'negative' if a < 0 else 'positive' if a > 0 else 'zero'
print(result)
# positive

a = -2
result = 'negative' if a < 0 else 'positive' if a > 0 else 'zero'
print(result)
# negative

a = 0
result = 'negative' if a < 0 else 'positive' if a > 0 else 'zero'
print(result)
# zero

l = ['even' if i % 2 == 0 else i for i in range(10)]
print(l)
# ['even', 1, 'even', 3, 'even', 5, 'even', 7, 'even', 9]

get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(1))
# odd

print(get_odd_even(2))
# even
