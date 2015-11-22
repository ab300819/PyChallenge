__author__ = 'Mason'

import re
import zipfile

z = zipfile.ZipFile('channel.zip', mode='r')
number = '90052'
comments = []
while True:
    text = z.read(number + '.txt')
    number = re.findall('([0-9]+)', text)
    print number
    try:
        number = number[0]
        comments.append(z.getinfo(number + '.txt').comment)
    except:
        break
print ''.join(comments)
