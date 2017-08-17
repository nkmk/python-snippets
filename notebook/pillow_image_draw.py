from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGB", (512, 512), (128, 128, 128))

draw = ImageDraw.Draw(im)

draw.line((0, im.height, im.width, 0), fill=(255, 0, 0), width=8)
draw.rectangle((100, 100, 200, 200), fill=(0, 255, 0))
draw.ellipse((250, 300, 450, 400), fill=(0, 0, 255))

font = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 48)
draw.multiline_text((0, 0), 'Pillow sample', fill=(0, 0, 0), font=font)

im.save('data/dst/pillow_iamge_draw.jpg', quality=95)

# ![pillow_image_draw](data/dst/pillow_iamge_draw.jpg)
