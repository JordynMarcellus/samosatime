#!/usr/bin/python
import json
import urllib2
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.yelp.ca'
url = 'http://www.yelp.ca/search?find_desc=samosa&find_loc=Toronto%2C+ON&ns=1'
soup = BeautifulSoup(urllib2.urlopen(url).read())

data = []
pages = []

r = requests.get(url)
nextlink = soup.find('a', { 'class': 'next' })['href']
pages.append(nextlink)

for listing in soup.find_all('div', attrs={'class': 'biz-listing-large'}):
	data.append({
		"name": listing.find('a',attrs={'class':'biz-name'}).contents[0],
		"address": listing.find('address').contents[0].lstrip() # removes newline and leading whitespace
		})

# print data
json.dump(data, open("data/samosadump.json", 'w'), indent=1)

# todo: 
# - exclude first search result (advertisement)
# - handle paginated results
# - add other data (phone? $? etc)