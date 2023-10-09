import scrapy
from scrapy.http import HtmlResponse
from onlineArticles.items import OnlinearticlesItem
import random


class QidianSpider(scrapy.Spider):
    name = "qidian"
    allowed_domains = ["qidian.com"]
    start_urls = ["https://www.qidian.com/rank/"]
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
    ]

    def start_requests(self):
        for url in self.start_urls:
            user_agent = random.choice(self.user_agent_list)
            yield scrapy.Request(url, headers={'User-Agent': user_agent}, callback=self.parse)

    def parse(self, response: HtmlResponse):
        item = OnlinearticlesItem()

        items = response.css(
            '.wrap > .rank-box > .main-content-wrap > .rank-body > .rank-list-row > .rank-list > .book-list > ul > li')
        
        for i in items:
            no_1_name = i.css(
                'div > div.book-info.fl > h2 > a::text').extract_first()
            no_1_href = i.css(
                'div > div.book-info.fl > h2 > a::attr(href)').extract_first()
            name = i.css('div.name-box > a > h2::text').extract_first()
            href = i.css('div.name-box  > a::attr(href)').extract_first()
            item['name'] = no_1_name if no_1_name != None else name
            item['href'] = no_1_href if no_1_href != None else href
            yield item
