from collections import OrderedDict
from kafka import KafkaProducer
import scrapy
import json
class CaseDetails(scrapy.Spider):
	producer = KafkaProducer(bootstrap_servers = '10.93.221.39:9092')
	name = "caseDetails"
	start_urls = ['https://www.insolvencydirect.bis.gov.uk/piudb/viewqryl.asp']

	def parse(self, response):
		for href in response.xpath('//a [contains(@href, "companyname")]/@href'):
			yield response.follow(href, self.parse_company)

	def parse_company(self, response):
		res = OrderedDict()
		for x in response.xpath('//tr[2]//tr [position() > 1]'):
			res[x.xpath('string(.//td [position() = 1])').extract()[0]] = x.xpath('string(.//td [position() = 2])').extract()[0]
		
		self.producer.send('theIS', json.dumps(res).encode('utf-8'))				
		yield res
		
	







