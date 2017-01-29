__author__ = 'dainaandries'
# -*- coding: utf-8 -*-

from names import dct
name = raw_input("What's your name?" ).upper()

x = name.strip()
print 'Name: ', x
if x in dct:
    print 'In US Census data?: ', 'yes'
    print 'Gender: ', dct[x]
else:
    print 'In US Census data: ', 'no'



