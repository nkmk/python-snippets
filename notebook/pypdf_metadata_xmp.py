import pypdf

print(pypdf.__version__)
# 5.5.0

pdf = pypdf.PdfReader('data/temp/Simple PDF 2.0 file.pdf')
print(pdf.metadata)
# None

print(type(pdf.xmp_metadata))
# <class 'pypdf.xmp.XmpInformation'>

print(pdf.xmp_metadata.dc_title)
# {'x-default': 'A simple PDF 2.0 example file'}

print(pdf.xmp_metadata.pdf_keywords)
# PDF 2.0 sample example

print(pdf.xmp_metadata.xmp_metadata_date)
# 2017-07-11 07:55:11
