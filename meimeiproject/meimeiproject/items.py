# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeimeiprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    # info = scrapy.Field()
    # tags = scrapy.Field()
    name = scrapy.Field()
    image_url = scrapy.Field()
