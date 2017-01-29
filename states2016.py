__author__ = 'dainaandries'
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar

import csv

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
page = opener.open("http://www.cawp.rutgers.edu/women-state-legislature-2016")
data = page.read()

soup = BeautifulSoup(data, 'lxml')

table = soup.find_all("table")
#print table[2].prettify()

string = str(table[2])
soup2 = BeautifulSoup(string, 'lxml')

header = ['State', 'D', 'R', 'Total Women', 'Total House Seats', 'Year']

lol = []
for row in soup2.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 15:
        lst = []
        state = cells[0].text.encode('ascii', 'ignore').decode('ascii')
        no_democrats = cells[7].text.encode('ascii', 'ignore').decode('ascii')
        no_republicans = cells[8].text.encode('ascii', 'ignore').decode('ascii')
        total_women_house = cells[10].text.encode('ascii', 'ignore').decode('ascii').rstrip('/')
        total_house = cells[11].text.encode('ascii', 'ignore').decode('ascii')
        year = 2016
        lst.append(state)
        lst.append(no_democrats)
        lst.append(no_republicans)
        lst.append(total_women_house)
        lst.append(total_house)
        lst.append(year)
        lol.append(lst)

output = open('2016WomenByState.csv', 'w')
writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

writer.writerow(header)
for item in lol:
    writer.writerow(item)

output.close()


