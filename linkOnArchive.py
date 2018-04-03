#!/usr/bin/env python
import requests 
from bs4 import BeautifulSoup

def linkOnArchive(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	return soup.find('div', {'class' : 'grid_7 push_1 omega'}).find('a').get('href')

linkOnArchive('http://download.companieshouse.gov.uk/en_output.html')


