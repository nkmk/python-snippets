import pypdf

print(pypdf.__version__)
# 5.5.0

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter(clone_from=src_pdf)

dst_pdf.metadata = None

dst_pdf.write('data/temp/sample1_no_meta.pdf')
# (True, <_io.FileIO [closed]>)

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter(clone_from=src_pdf)

metadata = dict(src_pdf.metadata)

print(metadata.keys())
# dict_keys(['/Title', '/Producer', '/Creator', '/CreationDate', '/ModDate'])

metadata.pop('/Creator')
del metadata['/Producer']

print(metadata.keys())
# dict_keys(['/Title', '/CreationDate', '/ModDate'])

dst_pdf.metadata = metadata
dst_pdf.write('data/temp/sample1_remove_meta.pdf')
# (True, <_io.FileIO [closed]>)
