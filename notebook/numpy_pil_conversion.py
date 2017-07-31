import numpy as np
from PIL import Image

src_path = "data/src/lenna.jpg"
img = Image.open(src_path).convert('RGB')

# ![lenna](data/src/lenna.jpg)

type(img)
# PIL.Image.Image

img.size  # (width, height)
# (400, 225)

# PIL Image to ndarray
arr = np.array(img)
type(arr)
# numpy.ndarray

arr.shape  # (height, width, channel)
# (225, 400, 3)

# ndarray to PIL Image
img2 = Image.fromarray(np.uint8(arr))
type(img2)
# PIL.Image.Image
