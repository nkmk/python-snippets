squares = [i**2 for i in range(5)]
print(squares)
# [0, 1, 4, 9, 16]

squares = []
for i in range(5):
    squares.append(i**2)

print(squares)
# [0, 1, 4, 9, 16]

odds = [i for i in range(10) if i % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9]

odds = []
for i in range(10):
    if i % 2 == 1:
        odds.append(i)

print(odds)
# [1, 3, 5, 7, 9]

odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
print(odd_even)
# ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

odd_even = []
for i in range(10):
    if i % 2 == 1:
        odd_even.append('odd')
    else:
        odd_even.append('even')

print(odd_even)
# ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

odd10 = [i * 10 if i % 2 == 1 else i for i in range(10)]
print(odd10)
# [0, 10, 2, 30, 4, 50, 6, 70, 8, 90]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [x for row in matrix for x in row]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

flat = []
for row in matrix:
    for x in row:
        flat.append(x)

print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

cells = [(row, col) for row in range(3) for col in range(2)]
print(cells)
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

cells = [(row, col) for row in range(3)
         for col in range(2) if col == row]
print(cells)
# [(0, 0), (1, 1)]

cells = [(row, col) for row in range(3) if row % 2 == 0
         for col in range(2) if col % 2 == 0]
print(cells)
# [(0, 0), (2, 0)]
