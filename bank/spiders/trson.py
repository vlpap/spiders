import scrapy


class TRsSpider(scrapy.Spider):
	name = "trson"
	start_urls = [
		'https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=en&ondernemingsnummer=896214177',
        ]
        
	def parse(self, response):
		     	
		tr_size=len(response.xpath('//tr//text()'))
		keys=list()
		values=list()
		i=1
		while i < tr_size:
			temp=response.xpath('//tr')[i]
			keys.append(temp.xpath('descendant::*//text()')[0])
			values.append(temp.xpath('descendant::*//text()')[1])
			i+=1
		
		print(keys)
		
		for tr in response.xpath('//tr//text()'):  		
				yield {
					"":tr.extract() 
				}
		


