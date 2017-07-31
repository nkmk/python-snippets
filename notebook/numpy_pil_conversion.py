import numpy as np
from PIL import Image

src_path = "data/src/lenna.jpg"
img = Image.open(src_path).convert('RGB')

# ![lenna](data/src/lenna.jpg)

print(type(img))
# <class 'PIL.Image.Image'>

print(img.size)  # (width, height)
# (400, 225)

# PIL Image to ndarray
arr = np.array(img)
print(type(arr))
# <class 'numpy.ndarray'>

print(arr.shape)  # (height, width, channel)
# (225, 400, 3)

# ndarray to PIL Image
img2 = Image.fromarray(np.uint8(arr))
print(type(img2))
# <class 'PIL.Image.Image'>
