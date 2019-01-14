import PyPDF2

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf', pages=(0, 1))
merger.append('data/src/pdf/sample2.pdf', pages=(2, 4))
merger.merge(2, 'data/src/pdf/sample3.pdf', pages=(0, 3, 2))

merger.write('data/temp/sample_merge_page.pdf')
merger.close()

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf', pages=PyPDF2.pagerange.PageRange('-1'))
merger.append('data/src/pdf/sample2.pdf', pages=PyPDF2.pagerange.PageRange('2:'))
merger.merge(2, 'data/src/pdf/sample3.pdf', pages=PyPDF2.pagerange.PageRange('::-1'))

merger.write('data/temp/sample_merge_pagerange.pdf')
merger.close()

reader1 = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')
reader2 = PyPDF2.PdfFileReader('data/src/pdf/sample2.pdf')

writer = PyPDF2.PdfFileWriter()

writer.addPage(reader1.getPage(0))
writer.addPage(reader2.getPage(2))

with open('data/temp/sample_merge_wr.pdf', 'wb') as f:
    writer.write(f)
