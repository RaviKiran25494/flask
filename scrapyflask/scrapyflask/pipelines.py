# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyflaskPipeline(object):
    def process_item(self, item, spider):
        return item
# import sys
# import MySQLdb
# import hashlib
# from scrapy.exceptions import DropItem
# from scrapy.http import Request

# class MySQLStorePipeline(object):


#     host = 'localhost'
#     user = 'root'
#     password = ''
#     db = 'amazon'

#     def __init__(self):
#         self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
#         self.cursor = self.connection.cursor()

#     def process_item(self, item, spider):   
#         try:
#             self.cursor.execute("""INSERT INTO amazon_project.ProductDepartment (ProductDepartmentLilnk) 
#                             VALUES (%s)""",
#                            (
#                             item['link'].encode('utf-8')))

#             self.connection.commit()

#         except MySQLdb.Error, e:
#             print "Error %d: %s" % (e.args[0], e.args[1])
#         return item