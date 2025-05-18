import pypdf

print(pypdf.__version__)
# 5.5.0

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter(clone_from=src_pdf)

new_metadata = {
    '/Title': 'new title',
    '/Producer': 'new producer',
    '/NewItem': 'special data'
}

dst_pdf.add_metadata(new_metadata)
dst_pdf.write('data/temp/sample1_new_meta.pdf')

print(pypdf.PdfReader('data/temp/sample1_new_meta.pdf').metadata)
# {'/Title': 'new title', '/Producer': 'new producer', '/Creator': IndirectObject(35, 0, 4398476304), '/CreationDate': IndirectObject(36, 0, 4398476304), '/ModDate': IndirectObject(36, 0, 4398476304), '/NewItem': 'special data'}

dst_pdf.metadata = new_metadata
dst_pdf.write('data/temp/sample1_new_meta_replace.pdf')

print(pypdf.PdfReader('data/temp/sample1_new_meta_replace.pdf').metadata)
# {'/Title': 'new title', '/Producer': 'new producer', '/NewItem': 'special data'}
