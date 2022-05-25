# -*- coding: utf-8 -*-

from scrapy import Request
from ..items import *
import random
import json
import re
from datetime import datetime
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context
class QqSpider(scrapy.Spider):
    def __init__(self, id1=None, *args, **kwargs):
        super(QqSpider, self).__init__(*args, **kwargs)
        self.id1 = id1
    name = 'qq_spider'

    base_url = 'https://pacaio.match.qq.com/xw/recommend?num=10'


    def start_requests(self):
        yield Request(self.base_url, callback=self.parse)


    def parse(self, response):
        result = json.loads(response.text)
        data_list = result.get('data')
        for data in data_list:
            item = NewsinaspiderItem()

            # ctime = datetime.fromtimestamp(int(data.get('publish_time')))
            # ctime = datetime.strftime(ctime, '%Y-%m-%d %H:%M')

            item['ctime'] = data.get('publish_time')
            item['url'] = data.get('vurl')
            item['wapurl'] = data.get('vurl')
            item['title'] = data.get('intro')
            item['lids'] = data.get('category_chn')
            item['media_name'] = '腾讯网'
            item['keywords'] = data.get('keywords')
            item['id1'] = str(random.random())[2:10]

            yield Request(url=item['url'], callback=self.parse_content, meta={'item': item})

    # 进入到详情页面 爬取新闻内容
    def parse_content(self, response):
        item =response.meta['item']

        # content = ''.join(response.xpath('//*[@id="artibody" or @id="article"]//p/text()').extract())
        # content = re.sub(r'\u3000', '', content)
        # content = re.sub(r'[ \xa0?]+', ' ', content)
        # content = re.sub(r'\s*\n\s*', '\n', content)
        # content = re.sub(r'\s*(\s)', r'\1', content)
        # content = ''.join([x.strip() for x in content])

        content_list = response.xpath('//p[@class="one-p"]/text()').extract()
        content = r""
        for part in content_list:
            part = part.strip()
            content += part

        item['content'] = content

        yield item




