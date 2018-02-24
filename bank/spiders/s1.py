import scrapy


class QLsSpider(scrapy.Spider):
	name = "QL"
	start_urls = [
		'https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=en&ondernemingsnummer=896214177',
        ]
        
	def parse(self, response):
        	page = response.url.split("/")[-2]
        	filename = 'QL-%s.html' % page
        	with open(filename, 'wb') as f:
        		f.write(response.body)
        	






