import pyzbar

print(pyzbar.__version__)
# 0.1.9

from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol

img = Image.open('data/src/barcode_qrcode.jpg')

decoded_list = decode(img)

print(type(decoded_list))
# <class 'list'>

print(len(decoded_list))
# 3

print(type(decoded_list[0]))
# <class 'pyzbar.pyzbar.Decoded'>

print(decoded_list[0])
# Decoded(data=b'QR Code Example', type='QRCODE', rect=Rect(left=8, top=6, width=159, height=160), polygon=[Point(x=8, y=66), Point(x=66, y=166), Point(x=167, y=109), Point(x=108, y=6)], quality=1, orientation='UP')

print(decoded_list[1])
# Decoded(data=b'1923055034006', type='EAN13', rect=Rect(left=161, top=217, width=175, height=32), polygon=[Point(x=161, y=229), Point(x=239, y=249), Point(x=330, y=248), Point(x=332, y=242), Point(x=335, y=226), Point(x=336, y=220), Point(x=336, y=218), Point(x=248, y=217), Point(x=165, y=217), Point(x=164, y=219), Point(x=162, y=225)], quality=37, orientation='UP')

print(decoded_list[2])
# Decoded(data=b'9784873117980', type='EAN13', rect=Rect(left=196, top=128, width=158, height=26), polygon=[Point(x=196, y=137), Point(x=267, y=151), Point(x=348, y=154), Point(x=349, y=152), Point(x=352, y=138), Point(x=354, y=128), Point(x=199, y=129), Point(x=197, y=133)], quality=25, orientation='UP')

print(decoded_list[0].data)
# b'QR Code Example'

print(type(decoded_list[0].data))
# <class 'bytes'>

print(decoded_list[0].data.decode())
# QR Code Example

print(decoded_list[0].type)
# QRCODE

print(decoded_list[1].type)
# EAN13

print(decoded_list[0].rect)
# Rect(left=8, top=6, width=159, height=160)

print(decoded_list[0].polygon)
# [Point(x=8, y=66), Point(x=66, y=166), Point(x=167, y=109), Point(x=108, y=6)]

print(len(decode(img, symbols=[ZBarSymbol.QRCODE])))
# 1

print(len(decode(img, symbols=[ZBarSymbol.EAN13])))
# 2

print(len(decode(img, symbols=[ZBarSymbol.QRCODE, ZBarSymbol.EAN13])))
# 3

for s in ZBarSymbol:
    print(s)
# ZBarSymbol.NONE
# ZBarSymbol.PARTIAL
# ZBarSymbol.EAN2
# ZBarSymbol.EAN5
# ZBarSymbol.EAN8
# ZBarSymbol.UPCE
# ZBarSymbol.ISBN10
# ZBarSymbol.UPCA
# ZBarSymbol.EAN13
# ZBarSymbol.ISBN13
# ZBarSymbol.COMPOSITE
# ZBarSymbol.I25
# ZBarSymbol.DATABAR
# ZBarSymbol.DATABAR_EXP
# ZBarSymbol.CODABAR
# ZBarSymbol.CODE39
# ZBarSymbol.PDF417
# ZBarSymbol.QRCODE
# ZBarSymbol.SQCODE
# ZBarSymbol.CODE93
# ZBarSymbol.CODE128
