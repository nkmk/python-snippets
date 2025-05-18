import pypdf

print(pypdf.__version__)
# 5.5.0

pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
print(pdf.is_encrypted)
# False

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter(clone_from=src_pdf)

dst_pdf.encrypt('pass_user', 'pass_owner', algorithm='AES-256-R5')
dst_pdf.write('data/temp/sample1_pass.pdf')
# (True, <_io.FileIO [closed]>)

pdf_pass = pypdf.PdfReader('data/temp/sample1_pass.pdf')
print(pdf_pass.is_encrypted)
# True

# dst_pdf = pypdf.PdfWriter(clone_from=pdf_pass)
# FileNotDecryptedError: File has not been decrypted

print(pdf_pass.decrypt('wrong-password'))
# 0

print(pdf_pass.decrypt('pass_user'))
# 1

print(pdf_pass.decrypt('pass_owner'))
# 2

dst_pdf = pypdf.PdfWriter(clone_from=pdf_pass)
dst_pdf.write('data/temp/sample1_no_pass.pdf')
# (True, <_io.FileIO [closed]>)

dst_pdf = pypdf.PdfWriter(clone_from=pdf_pass)
dst_pdf.encrypt('new_pass_user', 'new_pass_owner', algorithm='AES-256-R5')
dst_pdf.write('data/temp/sample1_new_pass.pdf')
# (True, <_io.FileIO [closed]>)
