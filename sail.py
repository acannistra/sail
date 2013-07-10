#! /usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
import json
import urllib2
from time import time

SAILCBI = "https://portal.community-boating.org/apex/f?p=710:1"
WEATHER = "https://api.forecast.io/forecast/7516bbf0f9e3cf4343c3744256fd183d/42.359439,-71.073260"

sail_cbi_resp = mechanize.urlopen(SAILCBI)
sail_cbi_soup = BeautifulSoup(sail_cbi_resp.read())
flagcolor = sail_cbi_soup.findAll('h2')[0].contents[2]

#json   = json.loads(urllib2.urlopen(WEATHER).read())

print "flag: "+flagcolor+' |',
#print "temp: "+str(json['currentTemp'])+'F |',
#print "hour: "+str(json['hourSummary'])



