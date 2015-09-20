import re

data = open('level3.txt', 'r')
word = data.read()
ans = ''
pattern = '[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]'
for match in re.findall(pattern, word):
    ans += match[4]
print ans
