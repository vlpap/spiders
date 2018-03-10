from pyspider.libs.base_handler import *
from collections import OrderedDict
from collections import defaultdict
import scrapy

class Liquidations(scrapy.Spider):
	name = "liquidations"
	start_urls = ['https://roi.aib.gov.uk/roi/Receiverships/Receivership/Details/1']
	base_url = 'https://roi.aib.gov.uk/roi/Receiverships/Receivership/Details/'
	
	def crawlingOfLinks(self, response):
		for link in range(1,3):
			absolute_url = self.base_url + str(link)
			yield scrapy.Request(absolute_url, callback=self.parse)
		

	def parse(self, response):
		res = defaultdict(dict)
		table = OrderedDict()
		tableHeader = list()
		for x in response.xpath('//div [@class = "form-group"]'):
			table[x.xpath('string( .//* [position() = 1])').extract_first()] = x.xpath('string( .//* [position() = 2])').extract_first()
		
		tableHeader = response.xpath('//h3/text()').extract()
		res[tableHeader.pop()].update(table)
				
		for fieldset in response.xpath('//fieldset [position() > 1]'):
			tableHeader += fieldset.xpath('.//legend/text()').extract()
			th = fieldset.xpath('.//div//th/text()').extract()
			td = list()
			for x in  fieldset.xpath('.//div//tbody//td'):
				td += x.xpath('string()').extract()
			table = OrderedDict()
			for x in range(0, len(td)):
				table[th[x]] = td[x]
			res[tableHeader.pop()].update(table)
			
		yield res




