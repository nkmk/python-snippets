def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

l = [0, 1, 2, 3, 4, 5]

print(convert_1d_to_2d(l, 2))
# [[0, 1], [2, 3], [4, 5]]

print(convert_1d_to_2d(l, 3))
# [[0, 1, 2], [3, 4, 5]]

print(convert_1d_to_2d(l, 4))
# [[0, 1, 2, 3], [4, 5]]

def convert_1d_to_2d_rows(l, rows):
    return convert_1d_to_2d(l, len(l) // rows)

print(convert_1d_to_2d_rows(l, 2))
# [[0, 1, 2], [3, 4, 5]]

print(convert_1d_to_2d_rows(l, 3))
# [[0, 1], [2, 3], [4, 5]]

print(convert_1d_to_2d_rows(l, 4))
# [[0], [1], [2], [3], [4], [5]]
