__author__ = 'dainaandries'
# -*- coding: utf-8 -*-

import csv
import urllib2

url = "https://raw.githubusercontent.com/Bemmu/gender-from-name/master/gender.py"
webpage = urllib2.urlopen(url)
datareader = csv.reader(webpage.read().splitlines())

data = []
for row in datareader:
  data.append(row)

d = data[1]
d[0] = d[0].split('=')
del d[0][0]
d[0] = d[0][0][2:]
#print len(d)
d[len(d)-1] = d[len(d)-1][:-1]

lst = []
for pair in d:
    l = []
    pair = pair.split(':')
    for i in pair:
        i = i.strip()
    for i in pair[::2]:
        i = i[3:-1]
        l.append(i)
    for i in pair[1::2]:
        i = i[2:-1]
        l.append(i)
    pair = tuple(l)
    lst.append(pair)

nl = []
for i in lst:
    if len(i) == 1:
        del i
    else:
        nl.append(i)
dct = dict(nl)
# print dct['KIM']
# print dct['ALEX']
dct.pop('KIM')
dct.pop('ALEX')

# if 'KIM' in dct:
#     print 'yes'
# else:
#     print 'not here anymore'
#
# if 'ALEX' in dct:
#     print 'yes'
# else:
#     print 'not here anymore'



