import pypdf

print(pypdf.__version__)
# 5.5.0

writer = pypdf.PdfWriter()

writer.append('data/src/pdf/sample1.pdf', pages=(0, 1))
writer.append('data/src/pdf/sample2.pdf', pages=(2, 4))
writer.merge(2, 'data/src/pdf/sample3.pdf', pages=(0, 3, 2))

writer.write('data/temp/sample_merge_page.pdf')
# (True, <_io.FileIO [closed]>)

writer = pypdf.PdfWriter()

writer.append('data/src/pdf/sample1.pdf', pages=pypdf.PageRange('-1'))
writer.append('data/src/pdf/sample2.pdf', pages=pypdf.PageRange('2:'))
writer.merge(2, 'data/src/pdf/sample3.pdf', pages=pypdf.PageRange('::-1'))

writer.write('data/temp/sample_merge_pagerange.pdf')
# (True, <_io.FileIO [closed]>)

reader1 = pypdf.PdfReader('data/src/pdf/sample1.pdf')
reader2 = pypdf.PdfReader('data/src/pdf/sample2.pdf')

writer = pypdf.PdfWriter()

writer.add_page(reader1.pages[0])
writer.add_page(reader2.pages[2])

writer.write('data/temp/sample_merge_wr.pdf')
# (True, <_io.FileIO [closed]>)
