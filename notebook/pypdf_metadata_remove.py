import PyPDF2

src_pdf = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')
dst_pdf = PyPDF2.PdfFileWriter()

dst_pdf.cloneReaderDocumentRoot(src_pdf)

with open('data/temp/sample1_no_meta.pdf', 'wb') as f:
    dst_pdf.write(f)

print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': 'PyPDF2'}

dst_pdf.addMetadata({'/Producer': ''})

with open('data/temp/sample1_no_meta.pdf', 'wb') as f:
    dst_pdf.write(f)

print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': ''}

def remove_all_metadata(src_path, dst_path, producer=''):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    dst_pdf.addMetadata({'/Producer': producer})
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

remove_all_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf')
print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': ''}

src_pdf = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')
dst_pdf = PyPDF2.PdfFileWriter()

d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}

print(d)
# {'/Title': 'sample1', '/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

d.pop('/Creator')
d.pop('/Producer')

print(d)
# {'/Title': 'sample1', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

dst_pdf.addMetadata(d)

with open('data/temp/sample1_remove_meta.pdf', 'wb') as f:
    dst_pdf.write(f)

print(PyPDF2.PdfFileReader('data/temp/sample1_remove_meta.pdf').documentInfo)
# {'/Producer': 'PyPDF2', '/Title': 'sample1', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

def remove_metadata(src_path, dst_path, *args, producer=''):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()
         if key not in args}
    
    d.setdefault('/Producer', producer)
    
    dst_pdf.addMetadata(d)
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

remove_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Creator', '/ModDate', '/CreationDate')
print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'sample1'}

remove_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Creator', '/ModDate', '/CreationDate', '/Producer')
print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': '', '/Title': 'sample1'}

remove_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Creator', '/ModDate', '/CreationDate', '/Producer', producer='XXX')
print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': 'XXX', '/Title': 'sample1'}

def select_metadata(src_path, dst_path, *args, producer=''):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()
         if key in args}
    
    d.setdefault('/Producer', producer)
    
    dst_pdf.addMetadata(d)
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

select_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Title', '/ModDate')
print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': '', '/Title': 'sample1', '/ModDate': "D:20190114072947Z00'00'"}

select_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Title', '/Producer')
print(PyPDF2.PdfFileReader('data/temp/sample1_no_meta.pdf').documentInfo)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'sample1'}
