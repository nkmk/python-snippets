import numpy as np

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

from PIL import Image

array = get_gradient_3d(512, 256, (0, 0, 0), (255, 255, 255), (True, True, True))
Image.fromarray(np.uint8(array)).save('data/dst/gray_gradient_h.jpg', quality=95)

# ![](data/dst/gray_gradient_h.jpg)

array = get_gradient_3d(512, 256, (0, 0, 0), (255, 255, 255), (False, False, False))
Image.fromarray(np.uint8(array)).save('data/dst/gray_gradient_v.jpg', quality=95)

# ![](data/dst/gray_gradient_v.jpg)

array = get_gradient_3d(512, 256, (0, 0, 192), (255, 255, 64), (True, False, False))
Image.fromarray(np.uint8(array)).save('data/dst/color_gradient.jpg', quality=95)

# ![](data/dst/color_gradient.jpg)
