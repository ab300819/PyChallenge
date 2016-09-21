# -*-coding:utf-8-*-
__author__ = 'Mason'

from PIL import Image
import re

img = Image.open('level7.png')

# left,top,right,bottom,切除黑白条
box = (0, 43, 606, 51)
belt = img.crop(box)

pixels = belt.getdata()

print('mode:%s' % img.mode)
print('amount of pixel:%d' % len(pixels))
print(pixels[0])

# convert mode RGBA to mode L
lBelt = belt.convert('L')

# get a sequence object containing pixel values
lPixels = lBelt.getdata()

# 黑白条中的像素点有规律：每一行的像素点都是一样的，并且一行中也有相同的像素。
# 但有一点不好处理的是：字母间可以通过能否组成单词来判断是否有重复值，但数字
# 就不能通过这种方法来判断了
str = []

for i in range(0, 608, 7):
    str.append(chr(lPixels[i]))
    x = lPixels[i]

result = ''.join(str)
print (result)

num = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(x) for x in num))
