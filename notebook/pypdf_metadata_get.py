import PyPDF2

pdf = PyPDF2.PdfFileReader('data/src/pdf/sample1.pdf')

print(type(pdf.documentInfo))
# <class 'PyPDF2.pdf.DocumentInformation'>

print(isinstance(pdf.documentInfo, dict))
# True

print(pdf.documentInfo)
# {'/Title': IndirectObject(33, 0), '/Producer': IndirectObject(34, 0), '/Creator': IndirectObject(35, 0), '/CreationDate': IndirectObject(36, 0), '/ModDate': IndirectObject(36, 0)}

print(pdf.documentInfo['/Title'])
# sample1

for k in pdf.documentInfo.keys():
    print(k, ':', pdf.documentInfo[k])
# /Title : sample1
# /Producer : macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext
# /Creator : Keynote
# /CreationDate : D:20190114072947Z00'00'
# /ModDate : D:20190114072947Z00'00'
