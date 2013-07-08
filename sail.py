#! /usr/bin/env python

import re
import mechanize
from BeautifulSoup import BeautifulSoup

SAILCBI = "https://portal.community-boating.org/apex/f?p=710:1"

resp    = mechanize.urlopen(SAILCBI)
soup    = BeautifulSoup(resp.read())

flagcolor = soup.findAll('h2')[0].contents[2]

print "flag: "+flagcolor



