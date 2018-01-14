def parse_info(self, response):
    # 获取到传递过来的参数
    item = response.meta['item']
    # 接着解析网页，获取item的其它信息
    # item['tags'] = response.xpath('//div[@class="postmeta  clearfix"]/div[@class="metaRight"]/p/text()').extract_first()
    div_list = response.xpath('//div[@class="postContent"]/div[@id="picture"]/p')

    for div in div_list:

        namex = div.xpath('./img/@alt').extract()
        image_list = div.xpath('./img/@src').extract()
        for image in image_list:
            item['image_url'] = image

        for name1 in namex:
            item['name'] = name1
        yield item