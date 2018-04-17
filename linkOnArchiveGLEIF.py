#!/usr/bin/env python3.6
import requests
import re
from bs4 import BeautifulSoup
from kafka import KafkaProducer

def linkOnArchive(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	listOfHref = list();
	for x in soup.find('div', {'class' : 'row leidata-download-btns remove-margin-right-for-rtl-filelinks'}).find_all(href = re.compile("https://leidata.gleif.org/api/v1/concatenated-files/")):
		listOfHref.append(x.get('href'))
	return listOfHref
	
producer = KafkaProducer(bootstrap_servers=['10.10.14.95:9092'])
for x in linkOnArchive('https://www.gleif.org/ru/lei-data/gleif-concatenated-file/download-the-concatenated-file'):
	producer.send('test2', str.encode(x), str.encode(x))

producer.flush()

#print(linkOnArchive('https://www.gleif.org/ru/lei-data/gleif-concatenated-file/download-the-concatenated-file'))

