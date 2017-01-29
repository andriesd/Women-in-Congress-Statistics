__author__ = 'dainaandries'
# -*- coding: utf-8 -*-

import csv
from urban import final_master

input = open('final_wRegions.csv', 'rU')

lst = []
for line in input:
    line = line.strip()
    line = line.rsplit(',', 20)
    line[0] = line[0].strip('"')
    lst.append(line)

header = lst[0]

data = lst[1:]
# for i in final_master:
#     if i[0] == 'AL':
#         print i


district_dct = {}
for i in final_master:
    join = i[0] + i[1] + str(i[3])
    district_dct[join] = i[2]

all_districts = {}
for i in district_dct:
    if i.endswith('2016'):
        all_districts[i] = district_dct[i]
        all_districts[i[:-4]+'2014'] = district_dct[i]
    # account for nominees running for 113th (during redrawing of districts for 112th)
    if i == 'TX332016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i == 'TX342016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i == 'TX352016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i == 'TX362016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i == 'NV42016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i == 'AZ92016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i == 'UT42016':
        all_districts[i[:-4]+'2012'] = district_dct[i]
    if i.endswith('2012'):
        all_districts[i] = district_dct[i]
        all_districts[i[:-4]+'2010'] = district_dct[i]
        all_districts[i[:-4]+'2008'] = district_dct[i]

# dct ={}
# for i in all_districts:
#     if i.startswith('MT'):
#         dct[i] = all_districts[i]
#         print i, all_districts[i]
# print len(dct)

for i in data:
    join = i[2]+i[3] + i[6]
    i.append(join)

# for i in all_districts:
#     print i
for i in data:
    if i[-1] in all_districts:
        i.append(all_districts[i[-1]])

# loss = []
# for i in data:
#     if len(i) < 23:
#         print i
#         loss.append(i)
# print len(loss)

header = header + ['urb_district_id', 'urbanPercent']
print header
for i in data:
    print i

output = open('final_wUrbanPercent.csv', 'w')
writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

writer.writerow(header)
for row in data:
    writer.writerow(row)

output.close()

