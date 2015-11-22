# -*-coding:utf-8-*-
__author__ = 'Mason'

from PIL import Image
import re

img = Image.open('7.png')

box = (0, 43, 608, 52)
belt = img.crop(box)

pixels = belt.getdata()

print('mode:%s' % img.mode)
print('amount of pixel:%d' % len(pixels))
print(pixels[0])

lBelt = belt.convert('L')

lPixels = lBelt.getdata()

str = []

for i in range(0, 608, 7):
    str.append(chr(lPixels[i]))
    x = lPixels[i]

result = ''.join(str)
print (result)

# rule = re.compile(r'^\d+\d$')
# match = rule.search(result)
# if match:
#     num = match.group()
#     print num
# else:
#     print 'Nothing!'


num = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print(''.join(chr(x) for x in num))
