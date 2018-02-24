from pyspider.libs.base_handler import *
from pprint import pprint
import itertools
from collections import OrderedDict
import re
import scrapy
from bank.items import TheInsolvencyServiceItems

class CaseDetails(scrapy.Spider):
	name = "caseDetails"
	start_urls = ['https://www.insolvencydirect.bis.gov.uk/piudb/viewpiucasedetails.asp?companyname-Foxton%20Furniture%20Group%20%20Ltd',]

	def parse(self, response):
	
		trP = response.xpath('//tr [position() = 2]')
		tr = trP.xpath('.//tr [position() > 1]')
		res = OrderedDict()
		i = 1
		for x in tr:
			res[x.xpath('string(.//td [position() = 1])').extract()[0]] = x.xpath('string(.//td [position() = 2])').extract()[0]

			if i % 23 == 0:
				yield res
		
			i += 1

		
			

	






