# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FabuItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()


class Aruidu(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class Ahsop(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class Milanstand(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()