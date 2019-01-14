import PyPDF2

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf')
merger.append('data/src/pdf/sample2.pdf')
merger.append('data/src/pdf/sample3.pdf')

merger.write('data/temp/sample_merge.pdf')
merger.close()

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf')
merger.merge(2, 'data/src/pdf/sample2.pdf')
merger.merge(4, 'data/src/pdf/sample3.pdf')

merger.write('data/temp/sample_insert.pdf')
merger.close()

merger = PyPDF2.PdfFileMerger()

merger.append('data/src/pdf/sample1.pdf')
merger.append('data/src/pdf/sample2.pdf')

d = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf').documentInfo
d = {k: d[k] for k in d.keys()}
d['/Title'] = 'merged file'

merger.addMetadata(d)

merger.write('data/temp/sample_merge_meta.pdf')
merger.close()
