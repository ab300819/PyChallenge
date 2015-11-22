__author__ = 'Mason'

data = open('level2.txt', 'r')
ans = ''
word = data.read()
for tmp in word:
    if tmp.isalpha():
        ans += tmp
    ans += ' '
print ans
