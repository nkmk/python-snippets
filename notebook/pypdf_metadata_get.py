import pypdf

print(pypdf.__version__)
# 3.7.1

pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')

print(type(pdf.metadata))
# <class 'pypdf._reader.DocumentInformation'>

print(isinstance(pdf.metadata, dict))
# True

print(pdf.metadata)
# {'/Title': IndirectObject(33, 0, 4360812432), '/Producer': IndirectObject(34, 0, 4360812432), '/Creator': IndirectObject(35, 0, 4360812432), '/CreationDate': IndirectObject(36, 0, 4360812432), '/ModDate': IndirectObject(36, 0, 4360812432)}

print(pdf.metadata['/Title'])
# sample1

for k in pdf.metadata.keys():
    print(k, ':', pdf.metadata[k])
# /Title : sample1
# /Producer : macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext
# /Creator : Keynote
# /CreationDate : D:20190114072947Z00'00'
# /ModDate : D:20190114072947Z00'00'
