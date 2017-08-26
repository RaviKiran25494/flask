from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapyflask.items import ScrapyflaskItem

# class MySpider(BaseSpider):
# 	"""docstring for ClassName"""
# 	name='flipkart'
# 	allowed_domains=['flipkart.com']
# 	start_urls=['https://www.flipkart.com/mens-clothing/tshirts/pr?sid=2oq,s9b,j9y&otracker=nmenu_sub_Men_0_T-Shirts/']


# 	def parse(self, response):
# 		hxs=HtmlXPathSelector(response)
# 		titles=hxs.select("//p")
# 		items=[]
# 		for titles in titles:
# 			item=ScrapyflaskItem()
# 			item["title"]=titles.select('a/text()').extract()
# 			item["link"]=titles.select('a/@href').extract()
# 			item.append(item)
# 		return items
# class ReviewSpider(BaseSpider):
#     name = 'review'
#     allowed_domains = ['https://www.flipkart.com/']
#     start_urls = ['https://www.flipkart.com/samsung-galaxy-j3-pro-gold-16-gb/p/itmeu35jfryetgew?pid=MOBEU35JAZKVWRPV&srno=b_1_2&otracker=nmenu_sub_Electronics_0_Samsung&lid=LSTMOBEU35JAZKVWRPVUXDI0L&fm=organic&iid=c9be448f-e34e-462a-8917-f9de923e844e.MOBEU35JAZKVWRPV.SEARCH/']

#     def parse(self, response):
#         for review in response.css('div._390CkK'):
#             dict ={
#                 'number':review.css('div.hGSR34::text').extract(),
#                 'comment':review.css('p._2xg6Ul::text').extract(),
#                 'details':review.css('div.qwjRop > div > div::text').extract()
#             }
#             yield dict
# # https://www.flipkart.com/wd-elements-2-5-inch-1-tb-external-hard-drive/p/itmdmhdqfhr4ndhq?pid=ACCDMHDQJHVRPYAN&srno=b_1_2&otracker=hp_omu_Deals%20of%20the%20day%20_1_From%20%E2%82%B93699_N9VHUP1HH1_0&lid=LSTACCDMHDQJHVRPYANAOZZLA&fm=merchandising&iid=5f943ab7-4596-4e8b-9351-2c1903ebae1a.ACCDMHDQJHVRPYAN.SEARCH
# class ReviewSpider(BaseSpider):
#     name = 'review1'
#     allowed_domains = ['https://www.flipkart.com/']
#     start_urls = ['https://www.flipkart.com/wd-elements-2-5-inch-1-tb-external-hard-drive/p/itmdmhdqfhr4ndhq?pid=ACCDMHDQJHVRPYAN&srno=b_1_2&otracker=hp_omu_Deals%20of%20the%20day%20_1_From%20%E2%82%B93699_N9VHUP1HH1_0&lid=LSTACCDMHDQJHVRPYANAOZZLA&fm=merchandising&iid=5f943ab7-4596-4e8b-9351-2c1903ebae1a.ACCDMHDQJHVRPYAN.SEARCH/']

#     def parse(self, response):
#         for review in response.css('div._390CkK'):
#             dict ={
#                 'number':review.css('div.hGSR34::text').extract(),
#                 'comment':review.css('p._2xg6Ul::text').extract(),
#                 'details':review.css('div.qwjRop > div > div::text').extract(),
                
#             }
#             print("--------------------------------------------------------")
#             yield dict
    

# class MySpider(BaseSpider):
#     name = 'wikimedia'
#     allowed_domains = ['https://www.flipkart.com/']
#     start_urls = ['https://www.flipkart.com/wd-elements-2-5-inch-1-tb-external-hard-drive/p/itmdmhdqfhr4ndhq?pid=ACCDMHDQJHVRPYAN&srno=b_1_2&otracker=hp_omu_Deals%20of%20the%20day%20_1_From%20%E2%82%B93699_N9VHUP1HH1_0&lid=LSTACCDMHDQJHVRPYANAOZZLA&fm=merchandising&iid=5f943ab7-4596-4e8b-9351-2c1903ebae1a.ACCDMHDQJHVRPYAN.SEARCH/']
#     l=[]
#     def parse1(self, response):
#         hxs=HtmlXPathSelector(response)
#         a=hxs.select('//div/a').extract()
#         l.append(a)
#         print(l)
#         print('--------------------------------')
            # https://www.flipkart.com/gadget-deals-soft-waterproof-2-5-inch-external-hard-disk-cover/p/itmehfamuajjfhjq?pid=HDEEHFAMKVJHSSXA&fm=productRecommendation/attach&iid=a:ACCDMHDQJHVRPYAN:6c2e66ed-96d8-4428-a2f0-1e0e25e42606.HDEEHFAMKVJHSSXA&otracker=pp_reco_Frequently+Bought+Together_1_Gadget+Deals+Soft+%26+Waterproof+2.5+inch+External+Hard+Disk+Cover_HDEEHFAMKVJHSSXA_productRecommendation/attach&cid=HDEEHFAMKVJHSSXA
class ReviewSpider(BaseSpider):
    name = 'review2'
    allowed_domains = ['https://www.flipkart.com/']
    start_urls = ['https://www.flipkart.com/gadget-deals-soft-waterproof-2-5-inch-external-hard-disk-cover/p/itmehfamuajjfhjq?pid=HDEEHFAMKVJHSSXA&fm=productRecommendation/attach&iid=a:ACCDMHDQJHVRPYAN:6c2e66ed-96d8-4428-a2f0-1e0e25e42606.HDEEHFAMKVJHSSXA&otracker=pp_reco_Frequently+Bought+Together_1_Gadget+Deals+Soft+%26+Waterproof+2.5+inch+External+Hard+Disk+Cover_HDEEHFAMKVJHSSXA_productRecommendation/attach&cid=HDEEHFAMKVJHSSXA/']
    
    def parse(self, response):
        list=[]
        for review in response.css('div._390CkK'):
            dict ={
                'number':review.css('div.hGSR34::text').extract(),
                'comment':review.css('p._2xg6Ul::text').extract(),
                'details':review.css('div.qwjRop > div > div::text').extract(),
                
            }
            print("--------------------------------------------------------")
            a=dict
            list.append(a)
            print("--------------------------------------------------------")
            yield dict
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(list)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    