__author__ = 'dainaandries'
# -*- coding: utf-8 -*-

import urllib2
from cookielib import CookieJar
from bs4 import BeautifulSoup

def transform(data):
    new_data = data[4:]
    new_data = new_data[:-2]
    new = []
    for i in new_data:
        lst = i.strip().split(' ')
        l = []
        for i in lst:
            if i == '':
                pass
            else:
                l.append(i)
        new.append(l)
    return new

def specials(new_data):
    new = []
    for i in new_data:
        lst = i.strip().split(' ')
        l = []
        for i in lst:
            if i == '':
                pass
            else:
                l.append(i)
        new.append(l)
    return new

districts = []

# dictionary for looking up state codes
code_dct = {}

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


page = opener.open('https://www.census.gov/geo/maps-data/data/cd_state.html')
data = page.read()

# 109th Congress
soup = BeautifulSoup(data, 'lxml')
urls_109 = soup.find("select", {"id": "ur109State"})
urls = []
for row in urls_109.find_all('option'):
    url = row.get('value')
    urls.append(url)
del urls[0]

for url in urls[0:11]:
    lst = url.split('/')
    state_code = lst[6]
    page = opener.open(url)
    data = page.readlines()
    n = transform(data)
    for i in n:
        code_dct[i[0]] = state_code
        d = []
        state = state_code
        district = i[1].lstrip('0')
        urban = i[5]
        congress = '109'
        d.append(state)
        d.append(district)
        d.append(urban)
        d.append(congress)
        districts.append(d)


for url in urls[12:14]:
    lst = url.split('/')
    state_code = lst[6]
    page = opener.open(url)
    data = page.readlines()
    n = transform(data)
    for i in n:
        code_dct[i[0]] = state_code
        d = []
        state = state_code
        district = i[1].lstrip('0')
        urban = i[5]
        congress = '109'
        d.append(state)
        d.append(district)
        d.append(urban)
        d.append(congress)
        districts.append(d)

for url in urls[15:33]:
    lst = url.split('/')
    state_code = lst[6]
    page = opener.open(url)
    data = page.readlines()
    n = transform(data)
    for i in n:
        code_dct[i[0]] = state_code
        d = []
        state = state_code
        district = i[1].lstrip('0')
        urban = i[5]
        congress = '109'
        d.append(state)
        d.append(district)
        d.append(urban)
        d.append(congress)
        districts.append(d)

for url in urls[34:42]:
    lst = url.split('/')
    state_code = lst[6]
    page = opener.open(url)
    data = page.readlines()
    n = transform(data)
    for i in n:
        code_dct[i[0]] = state_code
        d = []
        state = state_code
        district = i[1].lstrip('0')
        urban = i[5]
        congress = '109'
        d.append(state)
        d.append(district)
        d.append(urban)
        d.append(congress)
        districts.append(d)

# problem pages

# Indiana
page = opener.open('http://www2.census.gov/geo/relfiles/cd109th/IN/ur_c9_18.txt')
data = page.readlines()
# for i in data:
#     if i.startswith('Note:'):
#         print data.index(i)
new_data = data[4:]
#print len(new_data)
new_data = new_data[:-33]
n = specials(new_data)
for i in n:
    code_dct[i[0]] = 'IN'
    d = []
    state = 'IN'
    district = i[1].lstrip('0')
    urban = i[5]
    congress = '109'
    d.append(state)
    d.append(district)
    d.append(urban)
    d.append(congress)
    districts.append(d)


# Kentucky
page = opener.open('http://www2.census.gov/geo/relfiles/cd109th/KY/ur_c9_21.txt')
data = page.readlines()
# for i in data:
#     if i.startswith('Note:'):
#         print data.index(i)
new_data = data[4:]
#print len(new_data)
new_data = new_data[:-33]
n = specials(new_data)
for i in n:
    code_dct[i[0]] = 'KY'
    d = []
    state = 'KY'
    district = i[1].lstrip('0')
    urban = i[5]
    congress = '109'
    d.append(state)
    d.append(district)
    d.append(urban)
    d.append(congress)
    districts.append(d)

# Pennsylvania
page = opener.open('http://www2.census.gov/geo/relfiles/cd109th/PA/ur_c9_42.txt')
data = page.readlines()
# for i in data:
#     if i.startswith('Note:'):
#         print data.index(i)
new_data = data[4:]
# print len(new_data)
new_data = new_data[:-209]
n = specials(new_data)
for i in n:
    code_dct[i[0]] = 'PA'
    d = []
    state = 'PA'
    district = i[1].lstrip('0')
    urban = i[5]
    congress = '109'
    d.append(state)
    d.append(district)
    d.append(urban)
    d.append(congress)
    districts.append(d)

# Wisconsin
page = opener.open('http://www2.census.gov/geo/relfiles/cd109th/WI/ur_c9_55.txt')
data = page.readlines()
# for i in data:
#     if i.startswith('Note:'):
#         print data.index(i)
new_data = data[4:]
#print len(new_data)
new_data = new_data[:-20]
n = specials(new_data)
for i in n:
    code_dct[i[0]] = 'WI'
    d = []
    state = 'WI'
    district = i[1].lstrip('0')
    urban = i[5]
    congress = '109'
    d.append(state)
    d.append(district)
    d.append(urban)
    d.append(congress)
    districts.append(d)


# 110th Congress
# Georgia
page = opener.open('http://www2.census.gov/geo/relfiles/cd110th/GA/ur_c10_13.txt')
data = page.readlines()
n = transform(data)
for i in n:
    d = []
    state = 'GA'
    district = i[1].lstrip('0')
    urban = i[5]
    congress = '110'
    d.append(state)
    d.append(district)
    d.append(urban)
    d.append(congress)
    districts.append(d)

# Texas
page = opener.open('http://www2.census.gov/geo/relfiles/cd110th/TX/ur_c10_48.txt')
data = page.readlines()
n = transform(data)
for i in n:
    d = []
    state = 'TX'
    district = i[1].lstrip('0')
    urban = i[5]
    congress = '110'
    d.append(state)
    d.append(district)
    d.append(urban)
    d.append(congress)
    districts.append(d)


# 113th Congress
page = opener.open('https://www.census.gov/geo/maps-data/data/cd_state.html')
data = page.read()
soup = BeautifulSoup(data, 'lxml')
urls_113 = soup.find("select", {"id": "ur113Stated"})
urls = []
for row in urls_113.find_all('option'):
    url = row.get('value')
    urls.append(url)
del urls[0]

districts113 = []
for url in urls:
    page = opener.open(url)
    data = page.readlines()
    data = data[2:]
    for lst in data:
        d = []
        lst = lst.strip()
        lst = lst.split(',')
        state = lst[0]
        district = lst[1].lstrip('0')
        urban = lst[5]
        congress = '113'
        d.append(state)
        d.append(district)
        d.append(urban)
        d.append(congress)
        districts113.append(d)

for i in districts113:
    state_no = i[0]
    if state_no in code_dct:
        i[0] = code_dct[state_no]
        i[2] = i[2].rstrip('%')

master = districts + districts113

final_master = []
for i in master:
    if i[0] == 'TX' and i[3] == '109':
        pass
    if i[0] == 'GA' and i[3] == '109':
        pass
    else:
        final_master.append(i)

# for i in final_master:
#     congress = i[3]
#     if congress == '109':
#         i[3] = ['2008','2010','2012']
#     elif congress == '110':
#         i[3] = ['2008','2010','2012']
#     elif congress == '113':
#         i[3] = ['2014', '2016']

# Districts at large (whole state counts as district)
# source for urban percentage: US Census decennial data (2010)

# Montana

# mt = ['MT', '0', 104170.0, 1024000.0]
# mtpct = mt[2]/mt[3] * 100
# mt.append(mtpct)
# del mt[2:4]
# mt.append('113')
mt = ['MT', '0', 55.9, '113']
final_master.append(mt)

# mt2 = ['MT', '0', 104170.0, 1024000.0]
# mtpct = mt2[2]/mt2[3] * 100
# mt2.append(mtpct)
# del mt2[2:4]
# mt2.append('109')
mt2 = ['MT', '0', 55.9, '109']
final_master.append(mt2)

# Wyoming

# wy = ['WY','0', 59466.0, 584153.0]
# wypct = wy[2]/wy[3] * 100
# wy.append(wypct)
# del wy[2:4]
# wy.append('113')
wy = ['WY','0', 64.8, '113']
final_master.append(wy)

# wy2 = ['WY','0', 59466.0, 584153.0]
# wypct = wy2[2]/wy2[3] * 100
# wy2.append(wypct)
# del wy2[2:4]
# wy2.append('109')
wy2 = ['WY','0', 64.8, '109']
final_master.append(wy2)


# North Dakota

# nd = ['ND','0', 105549.0, 739482.0]
# ndpct = nd[2]/nd[3] * 100
# nd.append(ndpct)
# del nd[2:4]
# nd.append('113')
nd = ['ND','0', 59.9, '113']
final_master.append(nd)

# nd2 = ['ND','0', 105549.0, 739482.0]
# ndpct = nd2[2]/nd2[3] * 100
# nd2.append(ndpct)
# del nd2[2:4]
# nd2.append('109')
nd2 = ['ND','0', 59.9, '109']
final_master.append(nd2)

# Delaware

# de = ['DE','0', 70851.0, 935614.0]
# depct = de[2]/de[3] * 100
# de.append(depct)
# del de[2:4]
# de.append('113')
de = ['DE','0', 83.3, '113']
final_master.append(de)

# de2 = ['DE','0', 70851.0, 935614.0]
# depct = de2[2]/de2[3] * 100
# de2.append(depct)
# del de2[2:4]
# de2.append('109')
de2 = ['DE','0', 83.3, '109']
final_master.append(de2)


for i in final_master:
    if i[3] == '109':
        i[3] = 2012
    if i[3] == '110':
        i[3] = 2012
    if i[3] == '113':
        i[3] = 2016

# for i in final_master:
#     if i[0] == 'TX' and i[3]==2016:
#         print i
#     if i[0] == 'NV' and i[3]==2016:
#         print i
#     if i[0] == 'AZ' and i[3]==2016:
#         print i
#     if i[0] == 'UT' and i[3]==2016:
#         print i

# l1 =[]
# l2 = []
# l3 = []
# for i in master:
#     if i[0] == 'TX' and i[3] == '109':
#         l1.append(i)
#     elif i[0] == 'TX' and i[3] == '110':
#         l2.append(i)
#     elif i[0] == 'TX' and i[3] == '113':
#         l3.append(i)
# print l1
# print l2
# print l3