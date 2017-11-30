from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

im.save('data/dst/pillow_imagedraw.jpg', quality=95)

# ![imagedraw](data/dst/pillow_imagedraw.jpg)

im = Image.new('RGB', (500, 250), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.line(((30, 200), (130, 100), (80, 50)), fill=(255, 255, 0))
draw.line(((80, 200), (180, 100), (130, 50)), fill=(255, 255, 0), width=10)
draw.polygon(((200, 200), (300, 100), (250, 50)), fill=(255, 255, 0), outline=(0, 0, 0))
draw.point(((350, 200), (450, 100), (400, 50)), fill=(255, 255, 0))

im.save('data/dst/pillow_imagedraw2.jpg', quality=95)

# ![imagedraw2](data/dst/pillow_imagedraw2.jpg)

im = Image.new('RGB', (600, 250), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.arc((25, 50, 175, 200), start=30, end=270, fill=(255, 255, 0))
draw.chord((225, 50, 375, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))
draw.pieslice((425, 50, 575, 200), start=30, end=270, fill=(255, 255, 0), outline=(0, 0, 0))

im.save('data/dst/pillow_imagedraw3.jpg', quality=95)

# ![imagedraw3](data/dst/pillow_imagedraw3.jpg)

im = Image.open('data/src/lena.jpg')
draw = ImageDraw.Draw(im)

draw.pieslice((15, 50, 140, 175), start=30, end=330, fill=(255, 255, 0))

im.save('data/dst/pillow_imagedraw_lena.jpg', quality=95)

# ![imagedraw_lena](data/dst/pillow_imagedraw_lena.jpg)
