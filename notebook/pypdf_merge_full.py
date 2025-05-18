import pypdf

print(pypdf.__version__)
# 5.5.0

writer = pypdf.PdfWriter()

writer.append('data/src/pdf/sample1.pdf')
writer.append('data/src/pdf/sample2.pdf')
writer.append('data/src/pdf/sample3.pdf')

writer.write('data/temp/sample_merge.pdf')
# (True, <_io.FileIO [closed]>)

writer = pypdf.PdfWriter()

writer.append('data/src/pdf/sample1.pdf')
writer.merge(2, 'data/src/pdf/sample2.pdf')
writer.merge(4, 'data/src/pdf/sample3.pdf')

writer.write('data/temp/sample_insert.pdf')
# (True, <_io.FileIO [closed]>)

writer = pypdf.PdfWriter()

writer.append('data/src/pdf/sample1.pdf')
writer.append('data/src/pdf/sample2.pdf')

writer.add_metadata(pypdf.PdfReader('data/src/pdf/sample1.pdf').metadata)
writer.add_metadata({'/Title': 'merged file'})

writer.write('data/temp/sample_merge_meta.pdf')
# (True, <_io.FileIO [closed]>)
