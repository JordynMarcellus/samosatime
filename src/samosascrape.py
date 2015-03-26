#!/usr/bin/python
import json
import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.yelp.ca/search?find_desc=samosa&find_loc=Toronto%2C+ON&ns=1').read())

data = []

for listing in soup.findAll('div', attrs={'class': 'biz-listing-large'}):
	data.append({
		"name": listing.find('a',attrs={'class':'biz-name'}).contents[0],
		"address": listing.find('address').contents[0].lstrip() # removes newline and leading whitespace
		})

# print data
json.dump(data, open("data/samosadump.json", 'w'), indent=1)