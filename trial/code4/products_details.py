import scrapy
import datetime
import w3lib
from scrapy.crawler import CrawlerProcess
from w3lib.http import basic_auth_header
import pandas as pd

def read_csv():
    df = pd.read_csv('/home/ec2-user/e/trial/code4/cleaned_100items.csv')
    return df["Product_Url"]

# return df["Product_Url"][5].values.tolist()


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:

    Product_Url = scrapy.Field()
    ASIN = scrapy.Field()
    name = scrapy.Field()
    price1 = scrapy.Field()
    price2 = scrapy.Field()
    price3 = scrapy.Field()
    review = scrapy.Field()
    sold_1 = scrapy.Field()
    sold_2 = scrapy.Field()
    sold_3 = scrapy.Field()
    sold_4 = scrapy.Field()


class appSpider(scrapy.Spider):
    name = "entero"



    def start_requests(self):
        for x in read_csv():
            yield scrapy.Request(format(x))

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'c4product_details_urls.csv',
        'DOWNLOAD_DELAY': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1}

    def parse(self, response):
        items = ProjectItem()


        Product_Url = response.url
        ASIN = response.url
        name = response.xpath('//*[@id="productTitle"]/text()').extract()
        price1 = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()
        price2 = response.xpath('//*[@id="priceblock_dealprice"]/text()').extract()
        price3 = response.xpath('//*[@id="priceblock_saleprice"]/text()').extract()
        review = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()
        sold_1 = response.xpath('//*[@id="sellerProfileTriggerId"]/text()').extract()
        sold_2 = response.xpath('//*[@id="mbc-sold-by-1"]/span[2]/text()').extract()
        sold_3 = response.xpath('//*[@id="mbc-sold-by-2"]/span[2]/text()').extract()
        sold_4 = response.xpath('//*[@id="mbc-sold-by-3"]/span[2]/text()').extract()

        items['Product_Url'] = Product_Url
        items['ASIN'] = ASIN
        items['name'] = name
        items['price1'] = price1
        items['price2'] = price2
        items['price3'] = price3
        items['review'] = review
        items['sold_1'] = sold_1
        items['sold_2'] = sold_2
        items['sold_3'] = sold_3
        items['sold_4'] = sold_4


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

#C:/Users/Amit.Chaudhari/Desktop
#'FEED_URI': 'product_details_{}.csv'.format(datetime.date.today()),


