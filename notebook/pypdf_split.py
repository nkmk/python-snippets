import pypdf

print(pypdf.__version__)
# 5.5.0

writer = pypdf.PdfWriter()
writer.append('data/src/pdf/sample1.pdf', pages=pypdf.PageRange(':2'))
writer.write('data/temp/sample_split1.pdf')

writer = pypdf.PdfWriter()
writer.append('data/src/pdf/sample1.pdf', pages=pypdf.PageRange('2:'))
writer.write('data/temp/sample_split2.pdf')
# (True, <_io.FileIO [closed]>)
