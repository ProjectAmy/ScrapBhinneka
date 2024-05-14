# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TerlarisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nama = scrapy.Field()
    harga = scrapy.Field()
    cicilan = scrapy.Field()
    link = scrapy.Field()

class PerkakasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nama = scrapy.Field()
    harga = scrapy.Field()
    cicilan = scrapy.Field()
    link = scrapy.Field()
