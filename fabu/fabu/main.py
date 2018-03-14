#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings()) 
process.crawl('ahsop_text')
process.crawl('aruidu_text')
process.crawl('fabu_text')
process.crawl('milanstand_text')
process.start() 