import qrcode

img = qrcode.make('test text')

print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

img.save('data/dst/qrcode_test.png')

qr = qrcode.QRCode()
qr.add_data('test text')
qr.make()
img = qr.make_image()
img.save('data/dst/qrcode_test2.png')

qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)
qr.add_data('test text')
qr.make()
img = qr.make_image(fill_color="red", back_color="#23dda0")
img.save('data/dst/qrcode_test2_2.png')
