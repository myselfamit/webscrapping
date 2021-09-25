import scrapy
import datetime
import w3lib
from scrapy.crawler import CrawlerProcess
from w3lib.http import basic_auth_header
import pandas as pd




def read_csv():
    df = pd.read_csv('/home/ec2-user/e/trial/clean/cll4.csv')
    return df["0"].values.tolist()


class ProjectItem(scrapy.Item):
    urls = scrapy.Field()



class appSpider(scrapy.Spider):
    name = "entero"


    def start_requests(self):
        for x in read_csv():
            yield scrapy.Request(format(x))


    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'll5.csv',
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    }

    def parse(self, response):
        items = ProjectItem()


        urls = response.xpath('//*[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/li/a/@href').extract()

        items['urls'] = urls


        return items


process = CrawlerProcess()
process.crawl(appSpider)
process.start()

