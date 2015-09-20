data = open('level2.txt', 'r')
ans = ''
word = data.read()
for tmp in word:
    if tmp.isalpha():
        ans += tmp
print ans
