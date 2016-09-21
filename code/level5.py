# -*-coding:utf-8-*-
__author__ = 'Mason'

import urllib2
import cPickle as pickle
import pprint

f = urllib2.urlopen('http://www.PythonChallenge.com/pc/def/banner.p')
result = pickle.Unpickler(f).load()
pprint.pprint(result)
output = open('level5_out.txt', 'w')
for line in result:
    print >> output, ''.join([c[0] * c[1] for c in line])
output.close()
