import pypdf

print(pypdf.__version__)
# 3.7.1

merger = pypdf.PdfMerger()
merger.append('data/src/pdf/sample1.pdf', pages=pypdf.PageRange(':2'))
merger.write('data/temp/sample_split1.pdf')
merger.close()

merger = pypdf.PdfMerger()
merger.append('data/src/pdf/sample1.pdf', pages=pypdf.PageRange('2:'))
merger.write('data/temp/sample_split2.pdf')
merger.close()
