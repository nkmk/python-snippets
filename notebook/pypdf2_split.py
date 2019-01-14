import PyPDF2

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf', pages=PyPDF2.pagerange.PageRange(':2'))

merger.write('data/temp/sample_split1.pdf')
merger.close()

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf', pages=PyPDF2.pagerange.PageRange('2:'))

merger.write('data/temp/sample_split2.pdf')
merger.close()
