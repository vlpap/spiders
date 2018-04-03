#!/usr/bin/env python3.6
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from kafka import KafkaProducer

def linkOnArchive(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        return soup.find('div', {'class' : 'grid_7 push_1 omega'}).find('a').get('href')

def joinUrls(url):
        return urljoin(url, linkOnArchive(url))

producer = KafkaProducer(bootstrap_servers=['10.10.14.95:9092'])
producer.send('test', str.encode(joinUrls('http://download.companieshouse.gov.uk/en_output.html')))

producer.flush()
#print(joinUrls('http://download.companieshouse.gov.uk/en_output.html'))

