import pypdf

print(pypdf.__version__)
# 5.5.0

import glob
import os

def merge_pdf_in_dir(dir_path, dst_path):
    l = glob.glob(os.path.join(dir_path, '*.pdf'))
    l.sort()

    writer = pypdf.PdfWriter()
    for p in l:
        if not pypdf.PdfReader(p).is_encrypted:
            writer.append(p)

    writer.write(dst_path)

merge_pdf_in_dir('data/src/pdf', 'data/temp/sample_dir.pdf')
