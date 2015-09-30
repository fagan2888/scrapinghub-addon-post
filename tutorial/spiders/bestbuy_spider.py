# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider

from tutorial.items import ProductItem


class BestbuySpider(CrawlSpider):
    name = 'bestbuy'
    allowed_domains = ['bestbuy.com']
    start_urls = ('http://www.bestbuy.com',)
    item_count = 0
    rules = (
        # Extract links matching categories
        Rule(LinkExtractor(allow=(r'\wcat\d+\.c', ), deny=('subsection\.php', ))),
        # Extract links matching items and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r'\d\.p', )), callback='parse_item'),
    )

    def parse_item(self, response):
        # you can limit the items to finish the crawling.
        if self.item_count >= 100:
             raise CloseSpider('Max items reached.')
        loader = ItemLoader(response=response, item=ProductItem())
        loader.add_value('url', response.url)
        loader.add_xpath('title', '//title/text()')
        loader.add_xpath('description', '//div[@itemprop="description"]//text()')
        item = loader.load_item()
        self.item_count += 1
        yield item
