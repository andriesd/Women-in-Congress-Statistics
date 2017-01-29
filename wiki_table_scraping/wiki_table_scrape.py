# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import wikipedia

import csv

women = wikipedia.page('Women in the United States House of Representatives')
#print women.url
#print women.content

page = women.html()
soup = BeautifulSoup(page, 'lxml')
table = soup.find_all("table")
#print table[3].prettify()
string = str(table[3])
soup2 = BeautifulSoup(string, 'lxml')

lol =[]
for row in soup2.find_all('tr'):
    cells = row.find_all('td')
    #print len(cells)
    if len(cells) == 5:
        lst = []
        name = cells[0].text
        name = name.strip().encode('utf-8', 'replace')
        #print name
        party = cells[1].text
        party = party.strip().encode('utf-8')
        #print party
        district = cells[2].text
        district = district.strip().encode('utf-8')
        #print district
        dates_in_office = cells[3].text
        dates_in_office = dates_in_office.strip().encode('utf-8')
        #print dates
        lst.append(name)
        lst.append(party)
        lst.append(district)
        lst.append(dates_in_office)
        lol.append(lst)
    if len(cells) == 2:
        lst2=[]
        district = cells[0].text
        district = district.strip().encode('utf-8')
        #print district
        dates_in_office = cells[1].text
        dates_in_office = dates_in_office.strip().encode('utf-8')
        #print dates
        lst2.append(name)
        lst2.append(party)
        lst2.append(district)
        lst2.append(dates_in_office)
        lol.append(lst2)

output = open('ladies_in_congress.csv', 'w')
writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for i in lol:
    date_range = i[3].replace(' \xe2\x80\x93', '-')
    i.append(date_range)
    del i[3]

for i in lol:
    print i

for item in lol:
   writer.writerow(item)

output.close()
















