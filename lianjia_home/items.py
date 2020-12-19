# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaHomeItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    fitment = scrapy.Field()
    elevator = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    property = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
