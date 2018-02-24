import scrapy


class QLsSpider(scrapy.Spider):
	name = "QLson"
	start_urls = [
		'https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=en&ondernemingsnummer=896214177',
        ]
        
	def parse(self, response):

		#values=response.xpath('//td[@colspan="3"]//text()').extract()
			
		#table=response.xpath('//div[@id="table"]//text()').extract()
		#del table[0]
		#keys=[x for x in table if x not in values]
		
		for tr in response.xpath('//tr//text()'):  #response.xpath('.//div[@id="table"]//text()[normalize-space()]'):		
			yield {
				"":tr.extract()# key : values 
			}
		      	

