import PyPDF2

pdf = PyPDF2.PdfFileReader('data/temp/Simple PDF 2.0 file.pdf')

print(pdf.documentInfo)
# None

print(type(pdf.xmpMetadata))
# <class 'PyPDF2.xmp.XmpInformation'>

print(pdf.xmpMetadata.dc_title)
# {'x-default': 'A simple PDF 2.0 example file'}

print(pdf.xmpMetadata.pdf_keywords)
# PDF 2.0 sample example

print(pdf.xmpMetadata.xmp_metadataDate)
# 2017-07-11 07:55:11
