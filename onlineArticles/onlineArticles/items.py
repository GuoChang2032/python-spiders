# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OnlinearticlesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    href = scrapy.Field()
    author = scrapy.Field()
    rank = scrapy.Field()
    desc = scrapy.Field()



class ArticleContentItem(scrapy.Item):
    content = scrapy.Field()