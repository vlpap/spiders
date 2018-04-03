import scrapy
from collections import defaultdict

class Liquidations(scrapy.Spider):
	name = "liquidations"
	start_urls = ['https://roi.aib.gov.uk/roi/Receiverships/Receivership/Details/1', 'https://roi.aib.gov.uk/roi/Insolvency/Insolvency/Details/1']
			
	def parse(self, response):
		res = defaultdict(list)
        	
		for fieldset in response.xpath('//fieldset [@class = "form-horizontal well"]'):
                	table = dict()
                	tableHeader = fieldset.xpath('.//h3/text()').extract_first()
                	for x in fieldset.xpath('.//div [@class = "form-group"]'):
                        	table[x.xpath('string( .//* [position() = 1])').extract_first()] = x.xpath('string( .//* [position() = 2])').extract_first()
                	res[tableHeader].append(table)
		
		for fieldset in response.xpath('//fieldset [not(@*)]'):
			th = fieldset.xpath('.//div//th/text()').extract()
			for tr in fieldset.xpath('.//div//tbody//tr'):
				td = list()
				tableHeader = fieldset.xpath('.//legend/text()').extract_first()
				for x in tr.xpath('.//td'):
					td += x.xpath('string()').extract()
				table = dict()
				for x in range(0, len(th)):
					table[th[x]] = td[x]
				res[tableHeader].append(table)
		yield res
		
		urlSplit = str.rsplit(response.request.url, '/', 1)
		urlSplit[1] = str(int(urlSplit[1]) + 1)
		
		yield scrapy.Request("/".join(urlSplit)) 
		
