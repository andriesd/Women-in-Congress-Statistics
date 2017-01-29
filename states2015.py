__author__ = 'dainaandries'
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar

import csv

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
page = opener.open("http://www.ncsl.org/legislators-staff/legislators/womens-legislative-network/women-in-state-legislatures-for-2014.aspx")
data = page.read()

soup = BeautifulSoup(data, 'lxml')

table = soup.find_all("table")
# print table[0].prettify()

string = str(table[0])
soup2 = BeautifulSoup(string, 'lxml')

#headers = soup2.find('thead').text.strip().split('\n')

lol = []
for row in soup2.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 6:
        lst = []
        state = cells[0].text.strip()
        state_assembly = cells[1].text.strip()
        state_senate = cells[2].text.strip()
        total_women = cells[3].text.strip()
        total_seats = cells[4].text.strip()
        percentage = cells[5].text.strip()
        lst.append(state)
        lst.append(state_assembly)
        lst.append(state_senate)
        lst.append(total_women)
        lst.append(total_seats)
        lst.append(percentage)
        lol.append(lst)
del lol[-2]

#print table[1].prettify()
# string = str(table[1])
# soup3 = BeautifulSoup(string, 'lxml')
for row in lol:
    print row

header = ['Partisan Composition of Women in State Legislatures']
lol2 = []
# for row in soup3.find_all('thead'):
#     cells = row.find_all('th')
#     lst = []
#     lst.append(cells[0].text)
#     lst.append(cells[1].text)
#     lol2.append(lst)
# for row in soup3.find_all('tbody'):
#     for row in soup3.find_all('tr'):
#         cells = row.find_all('td')
#         lst = []
#         if len(cells) == 2:
#             lst.append(cells[0].text)
#             lst.append(cells[1].text)
#             lol2.append(lst)
#
# for row in lol:
#     print row
for row in soup2.find_all('tr'):
    cells = row.find_all('td')
    lst = []
    if len(cells) == 2:
        lst.append(cells[0].text.strip())
        lst.append(cells[1].text.strip())
        lol2.append(lst)
del lol2[-1]
for row in lol2:
    print row


output = open('2014state_legislatures.csv', 'w')
writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

# writer.writerow(headers)
for item in lol:
   writer.writerow(item)
writer.writerow('\n')
writer.writerow(header)
for item in lol2:
    writer.writerow(item)

output.close()











