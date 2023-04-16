import PyPDF2

pdf = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')

print(pdf.isEncrypted)
# False

src_pdf = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')

dst_pdf = PyPDF2.PdfFileWriter()

dst_pdf.cloneReaderDocumentRoot(src_pdf)

print(src_pdf.documentInfo)
# {'/Title': IndirectObject(33, 0), '/Producer': IndirectObject(34, 0), '/Creator': IndirectObject(35, 0), '/CreationDate': IndirectObject(36, 0), '/ModDate': IndirectObject(36, 0)}

# dst_pdf.addMetadata(src_pdf.documentInfo)
# TypeError: createStringObject should have str or unicode arg

d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}

print(d)
# {'/Title': 'sample1', '/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

dst_pdf.addMetadata(d)

dst_pdf.encrypt('password')

with open('data/temp/sample1_pass.pdf', 'wb') as f:
    dst_pdf.write(f)

def set_password(src_path, dst_path, password):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    dst_pdf.addMetadata(d)
    
    dst_pdf.encrypt(password)
    
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

set_password('data/src/pdf/sample1.pdf', 'data/temp/sample1_pass.pdf', 'password')

pdf_rc4 = PyPDF2.PdfFileReader('data/src/pdf/sample1_pass_rc4.pdf')

print(pdf_rc4.isEncrypted)
# True

# print(pdf_rc4.documentInfo)
# PdfReadError: file has not been decrypted

print(pdf_rc4.decrypt('wrong-password'))
# 0

print(pdf_rc4.decrypt('password'))
# 1

print(pdf_rc4.documentInfo)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'sample1', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

pdf_aes = PyPDF2.PdfFileReader('data/src/pdf/sample1_pass_aes.pdf')

# print(pdf_aes.decrypt('password'))
# NotImplementedError: only algorithm code 1 and 2 are supported

def change_password(src_path, dst_path, src_password, dst_password=None):
    src_pdf = PyPDF2.PdfFileReader(src_path)
    src_pdf.decrypt(src_password)
    
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    dst_pdf.addMetadata(d)
    
    if dst_password:
        dst_pdf.encrypt(dst_password)
    
    with open(dst_path, 'wb') as f:
        dst_pdf.write(f)

change_password('data/src/pdf/sample1_pass_rc4.pdf', 'data/temp/sample1_no_pass.pdf', 'password')

change_password('data/src/pdf/sample1_pass_rc4.pdf', 'data/temp/sample1_new_pass.pdf',
                'password', 'new_password')
