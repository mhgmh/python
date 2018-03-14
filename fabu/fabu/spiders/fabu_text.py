# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import FabuItem
import re
import requests
import json
import  time



se = requests.session()

class FabuTextSpider(scrapy.Spider):

    name = 'fabu_text'
    allowed_domains = ['pipixiabao.com']
    start_urls = ['http://www.pipixiabao.com/article_cat.php?id=6']

    def parse(self, response):
        it = FabuItem()
        url_list = response.xpath("//td/a[@style='text-decoration:none']/@href").extract()
        for url in url_list:
            con = se.get(response.urljoin(url)).text
            recon = PyQuery(con)
            it['title'] = recon('body > div.block.clearfix > div.AreaR > div.box > div > div > div.tc > font.f5.f6').text()
            it['content'] = recon('body > div.block.clearfix > div.AreaR > div.box > div > div > p > span > span').text()
            print(it['content'])

            yield it
            time.sleep(7200)
        all1 = '上一页</a> <a href="'
        all2 = '">下一页</a>'
        pet = re.compile(all1+"(.*?)"+all2)
        tourl = re.findall(pet,response.text)[0]
        if 'amp;' in tourl:
            turl = tourl.replace('amp;','')
            urls = response.urljoin(turl)
            yield scrapy.Request(urls,callback=self.parse)













