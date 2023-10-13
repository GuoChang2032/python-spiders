from typing import Iterable
import scrapy
from scrapy.http import HtmlResponse, Request
from onlineArticles.items import OnlinearticlesItem

class QimaoSpider(scrapy.Spider):
    name = "qimao"
    allowed_domains = ["www.qimao.com"]
    start_urls = ["https://www.qimao.com/paihang"]



    # def start_requests(self):
    #     for page in range(5):
    #         yield scrapy.Request(url=f'https://www.qimao.com/api/rank/book-list?is_girl=0&rank_type=7&date_type=2&date=202309&page={page}',callback=self.parse)

    def parse(self, response:HtmlResponse):
        # print('res----------------------',response)
        items = response.css('#__layout > div > div.wrapper > div > div.paihang-wrap > div.paihang-wrap-content.clearfix > div.paihang-wrap-content-detail > div > ul > li')

        for i in items:
            item = OnlinearticlesItem()
            item['name'] = i.css('.pic-txt-info > .txt > .txt-row > a::text').extract_first()
            item['href'] = i.css('.pic-txt-info > .txt > .txt-row > a::attr(href)').extract_first()
            item['author'] = i.css('.pic-txt-info > .txt > .txt-row > a::text').extract_first()
            item['rank'] = i.css('div > div.pic > a > span::text').extract_first()
            item['desc'] = i.css('.pic-txt-info > .txt > .s-book-intro::text').extract_first()
            yield item