# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

class LouPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        with open('courses.txt', 'a') as file:
            learned = re.findall("\d+", item['learned'])[0]
            line = u"course_name: {0}, learned_count: {1}, image: {2}\n".format(item['name'], learned, item['image'])
            file.write(line.encode('utf-8'))
        return item
