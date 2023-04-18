import pypdf

print(pypdf.__version__)
# 3.7.1

pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
print(pdf.is_encrypted)
# False

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter()
dst_pdf.clone_reader_document_root(src_pdf)

print(src_pdf.metadata)
# {'/Title': IndirectObject(33, 0, 4435217808), '/Producer': IndirectObject(34, 0, 4435217808), '/Creator': IndirectObject(35, 0, 4435217808), '/CreationDate': IndirectObject(36, 0, 4435217808), '/ModDate': IndirectObject(36, 0, 4435217808)}

# dst_pdf.add_metadata(src_pdf.metadata)
# TypeError: create_string_object should have str or unicode arg

d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
print(d)
# {'/Title': 'sample1', '/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

dst_pdf.add_metadata(d)

dst_pdf.encrypt('pass_u', 'pass_o')
dst_pdf.write('data/temp/sample1_pass.pdf')
# /opt/homebrew/lib/python3.11/site-packages/pypdf/_writer.py:1056: UserWarning: pypdf only implements RC4 encryption so far. The RC4 algorithm is insecure. Either use a library that supports AES for encryption or put the PDF in an encrypted container, for example an encrypted ZIP file.
#   warnings.warn(
# 
# (True, <_io.FileIO [closed]>)

def set_password(src_path, dst_path, user_password, owner_password=None):
    src_pdf = pypdf.PdfReader(src_path)
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)

    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
    dst_pdf.add_metadata(d)

    dst_pdf.encrypt(user_password, owner_password)
    dst_pdf.write(dst_path)

set_password('data/src/pdf/sample1.pdf', 'data/temp/sample1_pass.pdf',
             'pass_u', 'pass_o')

pdf_pass = pypdf.PdfReader('data/temp/sample1_pass.pdf')
print(pdf_pass.is_encrypted)
# True

# print(pdf_pass.metadata)
# FileNotDecryptedError: File has not been decrypted

print(pdf_pass.decrypt('wrong-password'))
# 0

print(pdf_pass.decrypt('pass_u'))
# 1

print(pdf_pass.decrypt('pass_o'))
# 2

print(pdf_pass.metadata)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'sample1', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

def change_password(
    src_path, dst_path, src_password, dst_user_password=None, dst_owner_password=None
):
    src_pdf = pypdf.PdfReader(src_path)
    src_pdf.decrypt(src_password)

    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)

    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
    dst_pdf.add_metadata(d)

    if dst_user_password is not None:
        dst_pdf.encrypt(dst_user_password, dst_owner_password)

    dst_pdf.write(dst_path)

change_password('data/temp/sample1_pass.pdf', 'data/temp/sample1_no_pass.pdf',
                'pass_u')

change_password('data/temp/sample1_pass.pdf', 'data/temp/sample1_new_pass.pdf',
                'pass_u', 'new_pass_u', 'new_pass_o')
