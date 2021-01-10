import os
import glob
from PIL import Image
import joblib

dst_dir = 'data/temp/joblib/dst_img'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('data/temp/joblib/src_img/*')

for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((img.width // 2, img.height // 2))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))
    except OSError as e:
        pass

def func(f):
    try:
        img = Image.open(f)
        img_resize = img.resize((img.width // 2, img.height // 2))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))
    except OSError as e:
        pass

_ = joblib.Parallel(n_jobs=-1)(joblib.delayed(func)(f) for f in files)
