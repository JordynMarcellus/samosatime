#!/usr/bin/python
import json
import urllib2
import requests
from bs4 import BeautifulSoup

data = []

for x in xrange(0,39):
	url_append = x*10
	url = 'http://www.yelp.ca/search?find_desc=samosa&find_loc=Toronto%2C+ON&start='+str(url_append)
	soup = BeautifulSoup(urllib2.urlopen(url).read())

	for listing in soup.findAll('div', attrs={'class': 'biz-listing-large'}):
		name = listing.find('a',attrs={'class':'biz-name'}).strings
		name = "".join(name)
		address = listing.find('address').contents[0].lstrip() # removes newline and leading whitespace
		phone = listing.find('span',attrs={'class':'biz-phone'}).contents[0].lstrip().rstrip()

		data.append({
			"name": "".join(name),
			"address": address,
			"phone": phone
		})

#print data
json.dump(data, open("data/samosadump.json", 'w'), indent=1)