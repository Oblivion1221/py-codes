# -*- coding: utf-8 -*-
import scrapy
from louspider.items import CourseItem
from scrapy.selector import Selector

class LouSpider(scrapy.Spider):
    name = "ourlouspider"
    allowed_domains = ["shiyanlou.com"]
    start_urls = ['https://www.shiyanlou.com/courses/?course_type=all&tag=all&free=yes']
    
    def parse(self,response):
        items = []
        hxs = Selector(response)
        courses = hxs.select('//div[@class="col-md-4 col-sm-6  course"]')
        for course in courses:
            item = CourseItem()
            item['name'] = course.xpath('a/div[3]/span[1]/text()').extract()
            item['learned'] = course.xpath('a/div[4]/span').extract()
            item['image'] = course.xpath('a/div[2]/img/@src').extract()
            items.append(item)
        return items
