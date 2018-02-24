import scrapy
from pprint import pprint

def values(x):
	v = list()
	for i in range(len(x)):
	#for i in range(1,len(x)):
		v.append(x[i])
	
	return  v

class QLsSpider(scrapy.Spider):
	name = "btable"
	start_urls = [ 'https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html;jsessionid=B5F93F9F7C1105D9B98D9EBEB8CE7733.worker4b?lang=en&ondernemingsnummer=896214177',
	]

	def parse(self, response):
		
		self.log('I just visited: ' + response.url)

		spisok=list()
				
		for tr in response.css("tr"):
			podspisok=list()	
			if tr.css("td.I"):
				title=tr.css("td.I::text").extract()

			else:
				podspisok+=title
			#	podspisok.append(tr.xpath('.//text()')[0].extract())
				podspisok += tr.xpath('.//text()').extract()
				
				podspisok = [el.replace(u'\t','') for el in podspisok]
				podspisok = [el.replace(u'\n','') for el in podspisok]
				podspisok = [el.replace(u'\xa0','') for el in podspisok]			
				podspisok = [el.replace(u'\xe9','e') for el in podspisok]
				podspisok = [el.replace(u'\xe0','a') for el in podspisok]

	
				podspisok = [i for i in podspisok if i !=u'']

				if len(podspisok) > 1:
					spisok.append(podspisok)

			#print(tr.extract()) 
		pprint(spisok)
		yield {
			"" : spisok
		}






























