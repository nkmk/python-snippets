import xlwt

wb = xlwt.Workbook()

print(type(wb))
# <class 'xlwt.Workbook.Workbook'>

sheet = wb.add_sheet('sheet1')

print(type(sheet))
# <class 'xlwt.Worksheet.Worksheet'>

sheet.write(0, 0, 'A')
sheet.write(0, 1, 'B')
sheet.write(1, 0, 10)
sheet.write(1, 1, 20)

# sheet.write(0, 0, 'A')
# Exception: Attempt to overwrite cell: sheetname='sheet1' rowx=0 colx=0

wb.save('data/dst/xlwt_sample.xls')

sheet2 = wb.add_sheet('sheet2')

def write_list_1d(sheet, l, start_row, start_col):
    for i, val in enumerate(l):
        sheet.write(start_row, start_col + i, val)

def write_list_2d(sheet, l_2d, start_row, start_col):
    for i, l in enumerate(l_2d):
        write_list_1d(sheet, l, start_row + i, start_col)

l_2d = [['A', 'B', 'C'], [1, 2, 3]]
write_list_2d(sheet2, l_2d, 1, 2)

wb.save('data/dst/xlwt_sample.xls')
