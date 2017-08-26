# import scrapy
# from craigslist_sample.items import AmazonDepartmentItem
# from scrapy.contrib.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors import LinkExtractor

# class AmazonAllDepartmentSpider(scrapy.Spider):

#     name = "amazon"
#     allowed_domains = ["amazon.com"]
#     start_urls = [
#         "http://www.amazon.com/gp/site-directory/ref=nav_sad/187-3757581-3331414"
#     ]
#     def parse(self, response):
#         for sel in response.xpath('//ul/li'):
#             item = AmazonDepartmentItem()
#             item['title'] = sel.xpath('a/text()').extract()[0]
#             item['link'] = sel.xpath('a/@href').extract()[0]
#             item['desc'] = sel.xpath('text()').extract()[0]
#             yield item