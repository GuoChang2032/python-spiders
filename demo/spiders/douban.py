import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse
from demo.items import DoubanItem
import random


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domain = ['movie.douban.com']

    def start_requests(self):
        for page in range(10):

            user_agent = random.choice(self.settings.get('USER_AGENT_LIST'))
            yield Request(url=f'https://movie.douban.com/top250?start={page*25}', headers={'User-Agent': user_agent}, callback=self.parse)

    def parse(self, response: HtmlResponse):
        sel = Selector(response)
        movie_item = sel.css('#content > div > div.article > ol > li')

        for movie_sel in movie_item:
            item = DoubanItem()
            item['title'] = movie_sel.css('.title::text').extract_first()
            item['score'] = movie_sel.css('.rating_num::text').extract_first()
            item['motto'] = movie_sel.css('.inq::text').extract_first()
            yield item
