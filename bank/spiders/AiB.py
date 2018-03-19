import scrapy
from scrapy.exceptions import CloseSpider
from collections import defaultdict

class Liquidations(scrapy.Spider):
	name = "liquidations"
	start_urls = ['https://roi.aib.gov.uk/roi/Receiverships/Receivership/Details/1']
	base_url = 'https://roi.aib.gov.uk/roi/Receiverships/Receivership/Details/'
	
	def parse(self, response):
		for link in range(540,545):
			absolute_url = self.base_url + str(link)
			print (response.xpath('//h3//text()'))
			print (response)
			yield scrapy.Request(absolute_url, callback=self.parse_company)
	
	def parse_company(self, response):
		print (response)
		res = defaultdict(list)
                for fieldset in response.xpath('//fieldset [@class = "form-horizontal well"]'):
                        table = dict()
                        tableHeader = fieldset.xpath('.//h3/text()').extract()
                        for x in fieldset.xpath('.//div [@class = "form-group"]'):
                                table[x.xpath('string( .//* [position() = 1])').extract_first()] = x.xpath('string( .//* [position() = 2])').extract_first()
                        res[tableHeader.pop()].append(table)
                for fieldset in response.xpath('//fieldset [not(@*)]'):
                        th = fieldset.xpath('.//div//th/text()').extract()
                        for tr in fieldset.xpath('.//div//tbody//tr'):
                                td = list()
                                tableHeader = fieldset.xpath('.//legend/text()').extract()
                                for x in tr.xpath('.//td'):
                                        td += x.xpath('string()').extract()
                                table = dict()
                                for x in range(0, len(th)):
                                        table[th[x]] = td[x]
                                res[tableHeader.pop()].append(table)

                yield res
