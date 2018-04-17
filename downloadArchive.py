#!/usr/bin/env python3.6
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from kafka import KafkaProducer
import sys

def linkOnArchive(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        return soup.find('div', {'class' : 'grid_7 push_1 omega'}).find('a').get('href')

def joinUrls(url):
        return urljoin(url, linkOnArchive(url))

def downloadFile(url):
	r = requests.get(url)
	return r.content
		
def test():
	s = b'x'
	producer = KafkaProducer(bootstrap_servers=['10.10.14.95:9092'])
	#producer.send('test', b'1KB' + 1000 * s + b'1KB')
	#producer.send('test', b'10KB' + 10000 * s + b'10KB')
	#producer.send('test', b'100KB' + 100000 * s + b'100KB')
	producer.send('test', 1000000 * s + b'1MB')
	#producer.send('test', 10000000 * s + b'10MB')
	#producer.send('test', 100000000 * s + b'100MB')
	
	producer.flush()
	#print(b'1KB' + 1000 * s)
	#print(sys.getsizeof(1000 * s))
#producer = KafkaProducer(bootstrap_servers=['10.10.14.95:9092'])
#producer.send('test', downloadFile(joinUrls('http://download.companieshouse.gov.uk/en_output.html')))
#producer.flush()
test()
#print(downloadFile(joinUrls('http://download.companieshouse.gov.uk/en_output.html')))
