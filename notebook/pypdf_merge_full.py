import pypdf

print(pypdf.__version__)
# 3.7.1

merger = pypdf.PdfMerger()

merger.append('data/src/pdf/sample1.pdf')
merger.append('data/src/pdf/sample2.pdf')
merger.append('data/src/pdf/sample3.pdf')

merger.write('data/temp/sample_merge.pdf')
merger.close()

merger = pypdf.PdfMerger()

merger.append('data/src/pdf/sample1.pdf')
merger.merge(2, 'data/src/pdf/sample2.pdf')
merger.merge(4, 'data/src/pdf/sample3.pdf')

merger.write('data/temp/sample_insert.pdf')
merger.close()

merger = pypdf.PdfMerger()

merger.append('data/src/pdf/sample1.pdf')
merger.append('data/src/pdf/sample2.pdf')

d = pypdf.PdfReader('data/src/pdf/sample1.pdf').metadata
d = {k: d[k] for k in d.keys()}
d['/Title'] = 'merged file'

merger.add_metadata(d)

merger.write('data/temp/sample_merge_meta.pdf')
merger.close()
