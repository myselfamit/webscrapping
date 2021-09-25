
import scrapy
import datetime
import w3lib
from scrapy.crawler import CrawlerProcess
from w3lib.http import basic_auth_header
import pandas as pd

def read_csv():
    df = pd.read_csv('/home/ec2-user/e/trial/clean/all_level_urls.csv')
    return df["urls"][:250]


# return df["urls"][:10].values.tolist()

class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    main_url = scrapy.Field()
    cat = scrapy.Field()
    urls_100 = scrapy.Field()
    cat = scrapy.Field()
    rank = scrapy.Field()
    asin = scrapy.Field()


class appSpider(scrapy.Spider):
    name = "entero"


    def start_requests(self):
        for x in read_csv():
            yield scrapy.Request(format(x))

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'c1c100items.csv',
        'DOWNLOAD_DELAY': 2.5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    }

    def parse(self, response):
        items = ProjectItem()

        # 100 asin
        asin = response.xpath('//*[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
        # empty_list = []


        # 100 urls
        urls_100 = response.xpath('//*[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
        #empty_list = []

        #categories
        cat = response.css('.zg_browseUp a::text').extract() + response.css('.zg_selected::text').extract()
        #cat_lst=[]

        #link from which 50 urls has been fetched
        main_url = response.url
        #main_url_list=[]

        # rank of the product
        rank = response.xpath('//*[@id="zg-ordered-list"]/li/span/div/div/span/span/text()').extract()



        items['main_url'] = main_url
        items['cat'] = cat
        items['urls_100'] = urls_100
        items['rank'] = rank
        items['asin'] = asin


        return items



process = CrawlerProcess()
process.crawl(appSpider)
process.start()



#response.css('.zg_browseUp a::text').extract()+ response.css('.zg_selected::text').extract()
#level2
#response.xpath('//*[@id="zg_browseRoot"]/ul/ul/li/a/@href').extract()
#level3
#response.xpath('//*[@id="zg_browseRoot"]/ul/ul/ul/li/a/@href').extract()
#level4
#response.xpath('//*[@id="zg_browseRoot"]/ul/ul/ul/ul/li/a/@href').extract()
#level5
#response.xpath('//*[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/li/a/@href').extract()
##level6
#response.xpath('//*[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/li/a/@href').extract()
#response.css('li.zg_browseUp a::text').extract()

#for page 1
#ref=zg_bs_pg_1
#for page 2
#ref=zg_bs_pg_2?ie=UTF8&pg=2

#sold_1 = response.xpath('//*[@id="sellerProfileTriggerId"]/text()').extract()
#sold_2 = response.xpath('//*[@id="mbc-sold-by-1"]/span[2]/text()').extract()
#sold_3 = response.xpath('//*[@id="mbc-sold-by-2"]/span[2]/text()').extract()
#sold_4 = response.xpath('//*[@id="mbc-sold-by-3"]/span[2]/text()').extract()

#.a-last a

# name of the product
#name = response.xpath('//*[@id="zg-ordered-list"]/li/span/div/span/a/div/text()').extract()