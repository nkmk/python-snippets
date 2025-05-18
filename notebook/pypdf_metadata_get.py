import pypdf

print(pypdf.__version__)
# 5.5.0

pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')

print(type(pdf.metadata))
# <class 'pypdf._doc_common.DocumentInformation'>

print(pdf.metadata.title)
# sample1

print(isinstance(pdf.metadata, dict))
# True

print(pdf.metadata)
# {'/Title': IndirectObject(33, 0, 4424533392), '/Producer': IndirectObject(34, 0, 4424533392), '/Creator': IndirectObject(35, 0, 4424533392), '/CreationDate': IndirectObject(36, 0, 4424533392), '/ModDate': IndirectObject(36, 0, 4424533392)}

print(pdf.metadata['/Title'])
# sample1

for k, v in pdf.metadata.items():
    print(f'{k}: {v}')
# /Title: sample1
# /Producer: macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext
# /Creator: Keynote
# /CreationDate: D:20190114072947Z00'00'
# /ModDate: D:20190114072947Z00'00'
