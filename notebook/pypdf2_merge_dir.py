import PyPDF2
import glob
import os

def merge_pdf_in_dir(dir_path, dst_path):
    l = glob.glob(os.path.join(dir_path, '*.pdf'))
    l.sort()
    
    merger = PyPDF2.PdfFileMerger()
    for p in l:
        if not PyPDF2.PdfFileReader(p).isEncrypted:
            merger.append(p)
    
    merger.write(dst_path)
    merger.close()

merge_pdf_in_dir('data/src/pdf', 'data/temp/sample_dir.pdf')
