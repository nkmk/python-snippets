import PyPDF2

src_pdf = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')
dst_pdf = PyPDF2.PdfFileWriter()

dst_pdf.cloneReaderDocumentRoot(src_pdf)

d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}

d['/Title'] = 'new title'
d['/Author'] = 'new author'
d['/XXX'] = 'special data'

dst_pdf.addMetadata(d)

with open('data/temp/sample1_new_meta.pdf', 'wb') as f:
    dst_pdf.write(f)

print(PyPDF2.PdfFileReader('data/temp/sample1_new_meta.pdf').documentInfo)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'new title', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'", '/Author': 'new author', '/XXX': 'special data'}

def update_metadata(src_path, dst_path, metadata):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    d.update(metadata)

    dst_pdf.addMetadata(d)
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

update_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_new_meta.pdf',
                {'/Title': 'new title', '/Author': 'new author', '/Producer': ''})
print(PyPDF2.PdfFileReader('data/temp/sample1_new_meta.pdf').documentInfo)
# {'/Producer': '', '/Title': 'new title', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'", '/Author': 'new author'}

def set_metadata(src_path, dst_path, metadata):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    dst_pdf.addMetadata(metadata)
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

set_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_new_meta.pdf',
             {'/Title': 'new title', '/Author': 'new author', '/Producer': ''})
print(PyPDF2.PdfFileReader('data/temp/sample1_new_meta.pdf').documentInfo)
# {'/Producer': '', '/Title': 'new title', '/Author': 'new author'}
