# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meimeiproject.items import MeimeiprojectItem
import urllib.request
import urllib.parse
import re

class MeituSpider(CrawlSpider):
    name = 'meitu'
    allowed_domains = ['www.meizitu.com']
    start_urls = ['http://www.meizitu.com/a/more_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'more_\d+\.html'), callback='parse_table', follow=True),
    )

    def parse_table(self, response):

        div_list = response.xpath('//div[@class="inWrap"]/ul[@class="wp-list clearfix"]/li[@class="wp-item"]')

        for div in div_list:

            item = MeimeiprojectItem()

            # item['info'] = div.xpath('./div[@class="con"]/div[@class="pic"]/a/img/@alt').extract_first()
            link = div.xpath('./div[@class="con"]/div[@class="pic"]/a/@href').extract_first()
            # yield item
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            yield scrapy.Request(url=link, callback=self.parse_info, meta={'item': item}, headers=headers)

    def parse_info(self, response):
        # 获取到传递过来的参数
        item = response.meta['item']
        # 接着解析网页，获取item的其它信息
        # item['tags'] = response.xpath('//div[@class="postmeta  clearfix"]/div[@class="metaRight"]/p/text()').extract_first()
        div_list = response.xpath('//div[@class="postContent"]/div[@id="picture"]/p')

        for div in div_list:

            name_list = div.xpath('./img/@alt').extract()
            image_list = div.xpath('./img/@src').extract()
            # for image in image_list:
            #     item['image_url'] = image
            # for name1 in name_list:
            #     item['name'] = name1
            # yield item
            for i in range(len(image_list)):
                item['image_url'] = image_list[i]
                item['name'] = name_list[i]

                yield item

