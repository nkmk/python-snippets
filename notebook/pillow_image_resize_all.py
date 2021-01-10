import os
import glob
from PIL import Image

dst_dir = 'data/temp/images_half'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('./data/temp/images/*.jpg')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((img.width // 2, img.height // 2))
    root, ext = os.path.splitext(f)
    basename = os.path.basename(root)
    img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))

files = glob.glob('./data/temp/images/*')

for f in files:
    root, ext = os.path.splitext(f)
    if ext in ['.jpg', '.png']:
        img = Image.open(f)
        img_resize = img.resize((img.width // 2, img.height // 2))
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))

files = glob.glob('./data/temp/images/*')

for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((img.width // 2, img.height // 2))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_half' + ext))
    except OSError as e:
        pass
