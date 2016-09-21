# -*-coding:utf-8-*-
__author__ = 'Mason'
import urllib2
import re

r = re.compile(r'(\d+)$')
nextnothing = '12345'
i = 0
while (1):
    try:
        f = urllib2.urlopen('http://www.PythonChallenge.com/pc/def/linkedlist.php?nothing=%s' % nextnothing)
        result = f.read()
        f.close()
        print result
        oldnextnothing = nextnothing
        nextnothing = r.search(result).group()
        if nextnothing == '16044':
            num = int(nextnothing)
            num = num / 2
            nextnothing = str(num)
        i += 1

    except:
        nextnothing = oldnextnothing
