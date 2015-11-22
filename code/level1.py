# -*-coding:utf-8-*-
__author__ = 'Mason'

data = open('level1.txt', 'r')
string = data.read().split(' ')
for word in string:
    ans = ''
    for key in word:
        if key.isalpha() and key not in 'yz':
            ans += chr(ord(key) + 2)
        if key == 'y':
            ans += 'a'
        if key == 'z':
            ans += 'b'
    print ans,
    ans = ''
