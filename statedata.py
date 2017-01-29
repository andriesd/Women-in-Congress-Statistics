__author__ = 'dainaandries'
# -*- coding: utf-8 -*-

master= []

file_input=open('2008WomenByState.csv', 'rU')
for line in file_input:
    line = line.strip()
    lst = line.split(',')
    lst.append('2008')
    lst[0] = lst[0].upper().strip().strip('*')
    nl = []
    nl.append(lst[0].upper())
    nl.append(lst[1])
    nl.append(lst[2])
    nl.append(lst[3])
    nl.append(lst[4])
    nl.append(lst[8])
    master.append(nl)
del master[0:3]

lol =[]
file_input2=open('2010WomenByState.csv', 'rU')
for line in file_input2:
    line = line.strip()
    lst = line.split(',')
    lst.append('2010')
    lst[0] = lst[0].upper().strip().strip('*')
    nl = []
    nl.append(lst[0])
    nl.append(lst[1])
    nl.append(lst[2])
    nl.append(lst[3])
    nl.append(lst[4])
    nl.append(lst[8])
    lol.append(nl)
del lol[0:3]
for i in lol:
    master.append(i)

lol =[]
file_input3=open('2012WomenByState.csv','rU')
for line in file_input3:
    line = line.strip()
    lst = line.split(',')
    lst.append('2012')
    lst[0] = lst[0].upper().strip().strip('*')
    nl = []
    nl.append(lst[0])
    nl.append(lst[1])
    nl.append(lst[2])
    nl.append(lst[3])
    nl.append(lst[4])
    nl.append(lst[8])
    lol.append(nl)
del lol[0:3]
for i in lol:
    master.append(i)

lol = []
file_input4=open('2014WomenByState.csv','rU')
for line in file_input4:
    line = line.strip()
    lst = line.split(',')
    lst[0] = lst[0].upper().strip()
    nl = []
    nl.append(lst[0])
    nl.append(lst[2])
    nl.append(lst[3])
    nl.append(lst[4])
    nl.append(lst[5])
    nl.append('2014')
    lol.append(nl)
del lol[0:2]
for i in lol:
    master.append(i)

lol = []
file_input5=open('2016WomenByState.csv', 'rU')
for line in file_input5:
    line = line.strip()
    lst = line.split(',')
    lst[0] = lst[0].upper().strip().strip('"').strip('*')
    lst[1] = lst[1].strip().strip('"')
    lst[2] = lst[2].strip().strip('"')
    lst[3] = lst[3].strip().strip('"')
    lst[4] = lst[4].strip().strip('"')
    lst[5] = lst[5].strip().strip('"')
    nl = []
    nl.append(lst[0])
    nl.append(lst[1])
    nl.append(lst[2])
    nl.append(lst[3])
    nl.append(lst[4])
    nl.append(lst[5])
    lol.append(nl)
del lol[0]
del lol[-1]
for i in lol:
    master.append(i)

for i in master:
    if i[0] == 'NE':
        i[3] = float(i[3])
        i[4] = float(i[4])
    else:
        i[1] = float(i[1])
        i[2] = float(i[2])
        i[3] = float(i[3])
        i[4] = float(i[4])

rlol = []
dlol = []
for i in master:
    rep = []
    dem = []
    if i[0] != 'NE':
        d = i[1]/i[4] * 100
        dem.append(i[0])
        dem.append(i[5])
        dem.append('DEM')
        dem.append(d)
        dlol.append(dem)
        r = i[2]/i[4] * 100
        rep.append(i[0])
        rep.append(i[5])
        rep.append('REP')
        rep.append(r)
        rlol.append(rep)
    else:
        d = i[3]/i[4] * 100
        dem.append(i[0])
        dem.append(i[5])
        dem.append('DEM')
        dem.append(d)
        dlol.append(dem)
        r = i[3]/i[4] * 100
        rep.append(i[0])
        rep.append(i[5])
        rep.append('REP')
        rep.append(r)
        rlol.append(rep)

rdct = {}
ddct = {}
for i in rlol:
    rdct[i[0]+i[2]+i[1]] = i[3]
for i in dlol:
    ddct[i[0]+i[2]+i[1]] = i[3]
#
# for i in master:
#     if i[0] == 'RI':
#         print i
for i in rdct:
    print i