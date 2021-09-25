import scrapy
import datetime
import w3lib
from scrapy.crawler import CrawlerProcess
from w3lib.http import basic_auth_header
import pandas as pd



class ProjectItem(scrapy.Item):
    urls = scrapy.Field()

class appSpider(scrapy.Spider):
    name = "entero"
    start_urls = ['https://www.amazon.in/gp/bestsellers/hpc/']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'll2.csv',
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1}


    def parse(self, response):
        items = ProjectItem()


        urls = response.xpath('//*[@id="zg_browseRoot"]/ul/ul/li/a/@href').extract()

        items['urls'] = urls


        return items


process = CrawlerProcess()
process.crawl(appSpider)
process.start()