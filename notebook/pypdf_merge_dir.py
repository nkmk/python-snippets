import pypdf

print(pypdf.__version__)
# 3.7.1

import glob
import os

def merge_pdf_in_dir(dir_path, dst_path):
    l = glob.glob(os.path.join(dir_path, '*.pdf'))
    l.sort()

    merger = pypdf.PdfMerger()
    for p in l:
        if not pypdf.PdfReader(p).is_encrypted:
            merger.append(p)

    merger.write(dst_path)
    merger.close()

merge_pdf_in_dir('data/src/pdf', 'data/temp/sample_dir.pdf')
