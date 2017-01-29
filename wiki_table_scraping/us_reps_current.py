# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import wikipedia

import csv

reps = wikipedia.page('Current members of the United States House of Representatives')
page = reps.html()
soup = BeautifulSoup(page, 'lxml')
table = soup.find_all("table")
#print table[6].prettify()
string = str(table[6])
soup2 = BeautifulSoup(string, 'lxml')

ladies = []
input = open('ladies_in_congress.csv', 'rU')
for line in input:
    line = line.strip()
    data = line.split(',')
    ladies.append(data[0][1:-1])

ladies = list(set(ladies))

lol =[]
for row in soup2.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) == 10:
        lst = []
        district = cells[1].text.encode('utf-8').strip()
        #print district
        name = cells[3].find('a').text.encode('utf-8').strip()
        #print name
        party = cells[4].text.encode('utf-8').strip()
        #print party
        assumed_office = int(cells[8].text.encode('utf-8','replace').strip().replace('*', ''))
        #print assumed_office
        born = int(cells[9].text.encode('utf-8').strip())
        age_elected = assumed_office - born
        #print born
        lst.append(district)
        lst.append(name)
        lst.append(party)
        lst.append(assumed_office)
        lst.append(born)
        lst.append(age_elected)
        lol.append(lst)


for i in lol:
    if i[1] in ladies:
        i.append('Female')
    else:
        i.append('Male')

for i in lol:
    print i

output = open('current_us_house_of_reps.csv', 'w')
writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for item in lol:
   writer.writerow(item)

output.close()
