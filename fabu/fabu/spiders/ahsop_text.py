# -*- coding: utf-8 -*-
import scrapy
from pyquery import  PyQuery
from ..items import Ahsop
import re
import requests
import time

se = requests.session()

class AhsopTextSpider(scrapy.Spider):
    name = 'ahsop_text'
    allowed_domains = ['ahsop.com']
    start_urls = ['http://www.ahsop.com/fuke/vip_doc/15622375_1343364_0_1.html']

    def parse(self, response):
        it = Ahsop()
        url_list = response.xpath("//span[@class='text-list-a']/a/@href").extract()
        for i in url_list:

            url = response.urljoin(i)

            headers = {

                'Cookie':'PHPSESSID=i00d1dq1c9n355mces52g72t53; fuke_pro_history=%2C6190874%2C; qx_trespass=http%3A%2F%2Fwww.ahsop.com%2Ffuke%2Fvip_doc%2F7434119.html',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',


            }


            print(url)
            se.headers.clear()
            se.headers.update(headers)
            str = se.get(url).text
            jpy = PyQuery(str)
            it['title'] = jpy('#pDetailsTitle > div > h1').text()
            it['content'] = jpy('#proShowDetail_3 > div').text()

            yield it
            time.sleep(7200)

        l = response.xpath("//div[@class='inner']/a/@href").extract()[-2]
        next = response.urljoin(l)
        yield scrapy.Request(next,callback=self.parse)





