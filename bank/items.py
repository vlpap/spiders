# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class TheInsolvencyServiceItems(Item):
    
	CompanyName = Field()
        TradingName = Field()
 	CompanyRegisteredNumber = Field()
	CourtNumber = Field()
	Addres1 = Field()
	Addres2 = Field()
	Addres3 = Field()
	PetitionDate = Field()
	ProvisionalLiquidationOrder = Field()
	PetitionHearingDate = Field()
	WindingUpOrderDate = Field()
	CurrentStatus = Field()
	Contact = Field()
	TelephoneNumber1 = Field()
	TelephoneNumber2 = Field()
	TelephoneNumber3 = Field()
	Email = Field()

