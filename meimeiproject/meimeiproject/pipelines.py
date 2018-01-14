# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request
import urllib.error
import requests

class MeimeiprojectPipeline(object):
    def __init__(self):
        self.fp = open('meitu.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        obj = dict(item)
        dirpath = r"C:\Users\Administrator\Desktop\pachong\meimeiproject\meimeiproject\spiders\images"
        suffix = os.path.splitext(obj['image_url'])[-1]
        # 拼接文件名
        filename = obj['name'] + suffix
        # 将文件路径和文件名拼接出来文件的全路径
        filepath = os.path.join(dirpath, filename)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(obj['image_url'], filepath)

        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()

