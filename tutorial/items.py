# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join

class ProductItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field(output_processor=Join())
    description = scrapy.Field(output_processor=Join())
    category = scrapy.Field()
