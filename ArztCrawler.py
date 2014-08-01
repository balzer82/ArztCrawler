# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Scraper für http://www.kvs-sachsen.de/arztsuche/

# <codecell>

import requests
from bs4 import BeautifulSoup

# <codecell>

searchurl = 'http://www.kvs-sachsen.de/arztsuche/pages/search.jsf'

# <codecell>

s = requests.session()

# <codecell>

data = 'p-additional_collapsed=true&additionalName_focus=&permittedService=selectTree_selection&time-afternoon_input=on&specialismRoot=search.subject.specialismRoot.any&p-surgery_collapsed=true&street=&days-mon_input=on&searchButton=&distance_input=-SAXONY-&p-empowerment_collapsed=true&days-thu_input=on&days-fri_input=on&specialismDetail=selectTree_selection&accessibility_input=-UNSELECTED-&days-sun_input=on&firstName=&p-subject_collapsed=false&accessibility_focus=&days-sat_input=on&p-common_collapsed=false&days-tue_input=on&distance_focus=&foreignLanguage_focus=&days-all_input=on&location-postal-combination=&days-wed_input=on&plz_input=01277&lastName=&foreignLanguage_input=-UNSELECTED-&additionalName_input=-UNSELECTED-&location_input=&displayEmpowered=no&time-morning_input=on'

# <codecell>

datasplit = data.split('&')
datasplit

# <codecell>

formdata = {}
for d in datasplit:
    formfield = d.split('=')
    print formfield
    try:
        formdata[formfield[0]] = formfield[1]
    except:
        continue

# <codecell>

formdata

# <codecell>

r = s.post(searchurl, params=formdata)
print(r.url)

# <codecell>

#print 'cookies:', requests.utils.dict_from_cookiejar(s.cookies)
cookie={}
cookie['JSESSIONID'] = s.cookies['JSESSIONID']
cookie['PHPSESSID'] = 'd77901m7eun4b8vj7lh3q1fngnak8sm9'
cookie['_pk_ref.1.2219'] = '%5B%22%22%2C%22%22%2C1406882756%2C%22http%3A%2F%2Fwww.kbv.de%2Fhtml%2Farztsuche.php%22%5D'
cookie['_pk_id.1.2219'] = '7a033f237c7bb7f6.1406882756.1.1406884688.1406882756.'

cookie

# <codecell>

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
          'referer': r.url,
          'Connection': 'keep-alive',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Cache-Control': 'max-age=0'}

arzte = requests.get('http://www.kvs-sachsen.de/arztsuche/pages/list.jsf', cookies=cookie, headers=header)
print(arzte.url)

# <markdowncell>

# Hm. Irgendwie klappt die Sache mit dem Cookie oder sowas nicht.

# <codecell>

soup = BeautifulSoup(arzte.text)

# <codecell>

print(soup.prettify())

# <codecell>


# <codecell>


