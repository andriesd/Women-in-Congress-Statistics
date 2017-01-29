__author__ = 'dainaandries'
# -*- coding: utf-8 -*-

import csv
from names import dct
from statedata import rdct, ddct

master = []

file_input = open('CandidateSummaryAction2008.csv', 'rU')
file_input2 = open('CandidateSummaryAction2010.csv', 'rU')
file_input3 = open('CandidateSummaryAction2012.csv', 'rU')
file_input4 = open('CandidateSummaryAction2014.csv', 'rU')
file_input5 = open('CandidateSummaryAction2016.csv', 'rU')

def filter(input):
    for line in input:
        line = line.strip()
        line = line.split(',', 2)
        line[2:] = line[2].rsplit(',', 9)
        line[2:] = map(str.strip, line[2:])
        lst = []
        candidate = line[2].strip('"')
        office = line[3]
        state = line[4]
        district = line[5]
        party = line[6]
        status = line[7]
        year = line[11]
        if office == 'H' and status == 'OPEN' and party == 'REP':
            lst.append(candidate)
            lst.append(office)
            lst.append(state)
            lst.append(district)
            lst.append(party)
            lst.append(status)
            lst.append(year)
        elif office == 'H' and status == 'OPEN' and party == 'DEM':
            lst.append(candidate)
            lst.append(office)
            lst.append(state)
            lst.append(district)
            lst.append(party)
            lst.append(status)
            lst.append(year)
        else:
            continue
        master.append(lst)

filter(input=file_input)
a = len(master)
#print a
filter(input=file_input2)
b = len(master)
#print b - a
filter(input=file_input3)
c = len(master)
#print c - b
filter(input=file_input4)
d = len(master)
#print d - c
filter(input=file_input5)
e = len(master)
#print e - d

#print len(master)

for i in master:
    names = i[0].split(',')
    if len(names) >= 2:
        name = names[1].strip()
        first = name.split()
        if first[0] > 3 and first[0] in dct:
            i.append(dct[first[0]])
        else:
            continue

unknowns = []
for i in master:
    if len(i) < 8:
        #print i
        unknowns.append(i)

#print len(unknowns)

for i in master:
    if len(i) == 8:
        if i[7] == 'female':
            i.append(1)
        elif i[7] == 'male':
            i.append(0)

manual_entries = []
manually_classified = open('knowns.csv', 'rU')
for line in manually_classified:
    line = line.strip()
    line = line.rsplit(',', 8)
    line[0] = line[0].strip('"')
    manual_entries.append(line)
del manual_entries[0]

names = {}
for i in manual_entries:
    names[i[0]] = [i[7], i[8]]

# for i in names:
#     print i, names[i][0]
#     print i, names[i][1]
for i in master:
    if i[0] in names:
        i.append(names[i[0]][0])
        i.append(names[i[0]][1])

for i in master:
    id = i[2]+i[4]+i[6]
    if id in rdct:
        i.append(rdct[id])
        i.append('republican')
    if id in ddct:
        i.append(ddct[id])
        i.append('democrat')

for i in master:
    if len(i) < 10:
        print i

header = ['Candidate','House/Senate', 'State', 'District', 'Party', 'Status', 'ElectionYear', 'Gender', 'GenderVar', 'PercentWomen']
output = open('final.csv', 'w')
writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(header)
for datum in master:
   writer.writerow(datum)

output.close()






