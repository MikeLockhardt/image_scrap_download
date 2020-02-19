# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagedownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Url = scrapy.Field()
    Date = scrapy.Field()
    Title = scrapy.Field()
    Content = scrapy.Field()
    Meta = scrapy.Field()
    ImgUrl = scrapy.Field()
    pass
