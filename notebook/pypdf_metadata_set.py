import pypdf

print(pypdf.__version__)
# 3.7.1

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter()

dst_pdf.clone_reader_document_root(src_pdf)

d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}

d['/Title'] = 'new title'
d['/Producer'] = 'new producer'
d['/XXX'] = 'special data'

dst_pdf.add_metadata(d)
dst_pdf.write('data/temp/sample1_new_meta.pdf')

print(pypdf.PdfReader('data/temp/sample1_new_meta.pdf').metadata)
# {'/Producer': 'new producer', '/Title': 'new title', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'", '/XXX': 'special data'}

def update_metadata(src_path, dst_path, metadata):
    src_pdf = pypdf.PdfReader(src_path)
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)

    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
    d.update(metadata)

    dst_pdf.add_metadata(d)
    dst_pdf.write(dst_path)

update_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_new_meta.pdf',
                {'/Title': 'new title', '/Author': 'new author', '/Producer': ''})
print(pypdf.PdfReader('data/temp/sample1_new_meta.pdf').metadata)
# {'/Producer': '', '/Title': 'new title', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'", '/Author': 'new author'}

def set_metadata(src_path, dst_path, metadata):
    src_pdf = pypdf.PdfReader(src_path)
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)
    dst_pdf.add_metadata(metadata)
    dst_pdf.write(dst_path)

set_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_new_meta.pdf',
             {'/Title': 'new title', '/Author': 'new author', '/Producer': ''})
print(pypdf.PdfReader('data/temp/sample1_new_meta.pdf').metadata)
# {'/Producer': '', '/Title': 'new title', '/Author': 'new author'}
