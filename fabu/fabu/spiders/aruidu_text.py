# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import Aruidu
import requests
import re
import  time


se = requests.session()
it = Aruidu()

class AruiduTextSpider(scrapy.Spider):
    name = 'aruidu_text'
    allowed_domains = ['aruidu.com']
    start_urls = ['http://www.aruidu.com/article_cat-18-1.html']

    def parse(self, response):
        it = Aruidu()
        list_url = response.xpath("//td/a/@href").extract()
        for url in list_url:
            str = se.get(url).text
            jpy = PyQuery(str)
            it['title'] = jpy('body > div.block.clearfix > div.AreaR > div.box > div > div > div.tc > font.f5.f6').text()
            it['content'] = jpy('body > div.block.clearfix > div.AreaR > div.box > div > div > p').text()
            yield it
        time.sleep(7200)
        n1 = '<a class="next" href="'
        n2 = '">下一页</a>'
        n = re.compile(n1+"(.*?)"+n2,re.S)
        next = re.findall(n,response.text)[0]


        yield scrapy.Request(next,callback=self.parse)

        print(next)






