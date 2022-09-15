import PIL

print(PIL.__version__)
# 9.2.0

from PIL import Image, ImageDraw, ImageFont

img = Image.open('data/src/astronaut_rect.bmp')

draw = ImageDraw.Draw(img)
draw.text((75, 50), 'Astronaut', 'red')

img.save('data/dst/pillow_imagedraw_text.jpg')

img = Image.open('data/src/astronaut_rect.bmp')

draw = ImageDraw.Draw(img)
draw.text((75, 50), 'I am an\nAstronaut', (255, 0, 0), spacing=10, align='right')

img.save('data/dst/pillow_imagedraw_text_multiline.jpg')

font = ImageFont.truetype('Arial.ttf', 24)

img = Image.open('data/src/astronaut_rect.bmp')

draw = ImageDraw.Draw(img)
draw.text((75, 50), 'I am an\nAstronaut', '#FF0000', font=font)

img.save('data/dst/pillow_imagedraw_text_arial.jpg')

print(ImageFont.truetype('Helvetica.ttc').getname())
# ('Helvetica', 'Regular')

print(ImageFont.truetype('Helvetica.ttc', index=0).getname())
# ('Helvetica', 'Regular')

print(ImageFont.truetype('Helvetica.ttc', index=1).getname())
# ('Helvetica', 'Bold')

print(ImageFont.truetype('Helvetica.ttc', index=2).getname())
# ('Helvetica', 'Oblique')

img = Image.open('data/src/astronaut_rect.bmp')

draw = ImageDraw.Draw(img)
draw.text((75, 50), 'I am an\nAstronaut', '#FF0000', font=font, anchor='md')

img.save('data/dst/pillow_imagedraw_text_anchor.jpg')

img = Image.open('data/src/astronaut_rect.bmp')

draw = ImageDraw.Draw(img)

print(draw.textbbox((75, 50), 'I am an\nAstronaut', font=font, anchor='md'))
# (23.0, 1, 127.0, 44)

draw.text((75, 50), 'I am an\nAstronaut', '#FF0000', font=font, anchor='md')
draw.rectangle(draw.textbbox((75, 50), 'I am an\nAstronaut', font=font, anchor='md'), outline='white', width=2)

img.save('data/dst/pillow_imagedraw_text_textbbox.jpg')

print(draw.textbbox((75, 50), 'I am an\nAstronaut', font=font, anchor='rd'))
# (-29.0, 1, 75.0, 44)

img = Image.open('data/src/astronaut_rect.bmp')

font = ImageFont.truetype('ヒラギノ丸ゴ ProN W4.ttc', 24)

draw = ImageDraw.Draw(img)
draw.text((100, 50), '私は', 'red', font=font, direction='ttb')
draw.text((75, 50), '宇宙飛行士', 'red', font=font, direction='ttb')

img.save('data/dst/pillow_imagedraw_text_ja.jpg')

# draw.text((100, 50), '私は\n宇宙飛行士', 'black', font=font, direction='ttb')
# ValueError: ttb direction is unsupported for multiline text
