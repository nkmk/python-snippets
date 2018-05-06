import xlrd
import pprint

wb = xlrd.open_workbook('data/src/sample.xlsx')

print(type(wb))
# <class 'xlrd.book.Book'>

print(wb.sheet_names())
# ['sheet1', 'sheet2']

sheets = wb.sheets()

print(type(sheets))
# <class 'list'>

print(type(sheets[0]))
# <class 'xlrd.sheet.Sheet'>

sheet = wb.sheet_by_name('sheet1')

print(type(sheet))
# <class 'xlrd.sheet.Sheet'>

cell = sheet.cell(1, 2)

print(cell)
# number:12.0

print(type(cell))
# <class 'xlrd.sheet.Cell'>

print(cell.value)
# 12.0

print(sheet.cell_value(1, 2))
# 12.0

col = sheet.col(1)

print(col)
# [text:'A', number:11.0, number:21.0, number:31.0]

print(type(col[0]))
# <class 'xlrd.sheet.Cell'>

col_values = sheet.col_values(1)

print(col_values)
# ['A', 11.0, 21.0, 31.0]

print(sheet.row_values(1))
# ['one', 11.0, 12.0, 13.0]

pprint.pprint([sheet.row_values(x) for x in range(4)])
# [['', 'A', 'B', 'C'],
#  ['one', 11.0, 12.0, 13.0],
#  ['two', 21.0, 22.0, 23.0],
#  ['three', 31.0, 32.0, 33.0]]

def get_list_2d(sheet, start_row, end_row, start_col, end_col):
    return [sheet.row_values(row, start_col, end_col + 1) for row in range(start_row, end_row + 1)]

l_2d = get_list_2d(sheet, 2, 3, 1, 2)
print(l_2d)
# [[21.0, 22.0], [31.0, 32.0]]

print(sheet.nrows)
# 4

def get_list_2d_all(sheet):
    return [sheet.row_values(row) for row in range(sheet.nrows)]

l_2d_all = get_list_2d_all(sheet)
pprint.pprint(l_2d_all)
# [['', 'A', 'B', 'C'],
#  ['one', 11.0, 12.0, 13.0],
#  ['two', 21.0, 22.0, 23.0],
#  ['three', 31.0, 32.0, 33.0]]

print(l_2d_all[1][0])
# one
