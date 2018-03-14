# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import Milanstand
import re
import requests
import time

se = requests.session()

class MilanstandTextSpider(scrapy.Spider):
    name = 'milanstand_text'
    allowed_domains = ['milanstand.com']
    start_urls = ['http://www.milanstand.com/article-zixun-1/']

    def parse(self, response):

        ss = response.xpath("//div[@align='left']/a/@href").extract()
        for i in ss:
            it = Milanstand()
            url = response.urljoin(i)
            cont = se.get(url).text
            jpy = PyQuery(cont)
            it['title'] = jpy('body > div.mainx > div.mainxr > div.box > div > div > div.tc > font.f5').text()
            it['content'] =jpy('body > div.mainx > div.mainxr > div.box > div > div > div.mcontent').text()
            yield it
            time.sleep(7200)

        l = response.xpath("//p[@class='nx']/a/@href").extract()[0]
        next = response.urljoin(l)

        yield scrapy.Request(next,callback=self.parse)





