import pypdf

print(pypdf.__version__)
# 3.7.1

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter()

dst_pdf.clone_reader_document_root(src_pdf)
dst_pdf.write('data/temp/sample1_no_meta.pdf')
# (True, <_io.FileIO [closed]>)

print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': 'pypdf'}

dst_pdf.add_metadata({'/Producer': ''})
dst_pdf.write('data/temp/sample1_no_meta.pdf')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': ''}

def remove_all_metadata(src_path, dst_path, producer=''):
    src_pdf = pypdf.PdfReader(src_path)
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)
    dst_pdf.add_metadata({'/Producer': producer})
    dst_pdf.write(dst_path)

remove_all_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': ''}

src_pdf = pypdf.PdfReader('data/src/pdf/sample1.pdf')
dst_pdf = pypdf.PdfWriter()
dst_pdf.clone_reader_document_root(src_pdf)

d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
print(d)
# {'/Title': 'sample1', '/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Creator': 'Keynote', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

d.pop('/Creator')
d.pop('/Producer')
print(d)
# {'/Title': 'sample1', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

dst_pdf.add_metadata(d)
dst_pdf.write('data/temp/sample1_remove_meta.pdf')
# (True, <_io.FileIO [closed]>)

print(pypdf.PdfReader('data/temp/sample1_remove_meta.pdf').metadata)
# {'/Producer': 'pypdf', '/Title': 'sample1', '/CreationDate': "D:20190114072947Z00'00'", '/ModDate': "D:20190114072947Z00'00'"}

def remove_metadata(src_path, dst_path, *args, producer=''):
    src_pdf = pypdf.PdfReader(src_path)
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)

    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()
         if key not in args}
    d.setdefault('/Producer', producer)

    dst_pdf.add_metadata(d)
    dst_pdf.write(dst_path)

remove_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Creator', '/ModDate', '/CreationDate')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'sample1'}

remove_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Creator', '/ModDate', '/CreationDate', '/Producer')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': '', '/Title': 'sample1'}

remove_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Creator', '/ModDate', '/CreationDate', '/Producer',
                producer='XXX')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': 'XXX', '/Title': 'sample1'}

def select_metadata(src_path, dst_path, *args, producer=''):
    src_pdf = pypdf.PdfReader(src_path)
    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_reader_document_root(src_pdf)

    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()
         if key in args}
    d.setdefault('/Producer', producer)

    dst_pdf.add_metadata(d)
    dst_pdf.write(dst_path)

select_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Title', '/ModDate')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': '', '/Title': 'sample1', '/ModDate': "D:20190114072947Z00'00'"}

select_metadata('data/src/pdf/sample1.pdf', 'data/temp/sample1_no_meta.pdf',
                '/Title', '/Producer')
print(pypdf.PdfReader('data/temp/sample1_no_meta.pdf').metadata)
# {'/Producer': 'macOS バージョン10.14.2（ビルド18C54） Quartz PDFContext', '/Title': 'sample1'}
