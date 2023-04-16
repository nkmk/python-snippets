import pypdf

def split_pdf_pages(src_path, dst_basepath):
    src_pdf = pypdf.PdfReader(src_path)
    for i, page in enumerate(src_pdf.pages):
        dst_pdf = pypdf.PdfWriter()
        dst_pdf.add_page(page)
        dst_pdf.write(f'{dst_basepath}_{i}.pdf')

split_pdf_pages('data/src/pdf/sample1.pdf', 'data/temp/sample1')
