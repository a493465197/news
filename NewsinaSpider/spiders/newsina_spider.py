# -*- coding: utf-8 -*-

from scrapy import Request
from ..items import *
import random
import json
import re
from datetime import datetime
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context
class NewsinaSpiderSpider(scrapy.Spider):
    def __init__(self, id1=None, *args, **kwargs):
        super(NewsinaSpiderSpider, self).__init__(*args, **kwargs)
        self.id1 = id1
    name = 'newsina_spider'

    base_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid={}&k=&num=1&page={}&r={}'

    #     "2509": "全部",
    #     "2510": "国内",
    #     "2511": "国际",
    #     "2669": "社会",
    #     "2512": "体育",
    #     "2513": "娱乐",
    #     "2514": "军事",
    #     "2515": "科技",
    #     "2516": "财经",
    #     "2517": "股市",
    #     "2518": "美股",
    #     "2968": "国内_国际",
    #     "2970": "国内_社会",
    #     "2972": "国际_社会",
    #     "2974": "国内国际社会"

    def start_requests(self):
        #  可修改  这里设置爬取100页
        page_total = 1
        for page in range(1, page_total+1):
            lid = "2509"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2510"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2669"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2512"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2513"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2514"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2515"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2516"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2517"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)
        for page in range(1, page_total+1):
            lid = "2518"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        data_list = result.get('result').get('data')

        for data in data_list:
            item = NewsinaspiderItem()
            ctime = datetime.fromtimestamp(int(data.get('ctime')))
            ctime = datetime.strftime(ctime, '%Y-%m-%d %H:%M')
            lids = data.get('lids')
            lids = lids.replace('2510', '国内')
            lids = lids.replace('2511', '国际')
            lids = lids.replace('2669', '社会')
            lids = lids.replace('2512', '体育')
            lids = lids.replace('2513', '娱乐')
            lids = lids.replace('2514', '军事')
            lids = lids.replace('2515', '科技')
            lids = lids.replace('2516', '财经')
            lids = lids.replace('2517', '股市')
            lids = lids.replace('2518', '美股')
            item['ctime'] = ctime
            item['url'] = data.get('url')
            item['wapurl'] = data.get('wapurl')
            item['title'] = data.get('title')
            item['media_name'] = data.get('media_name')
            item['keywords'] = data.get('keywords')
            item['lids'] = lids
            item['id1'] = str(random.random())[2:10]


            yield Request(url=item['url'], callback=self.parse_content, meta={'item': item})

    # 进入到详情页面 爬取新闻内容
    def parse_content(self, response):
        item =response.meta['item']
        content = ''.join(response.xpath('//*[@id="artibody" or @id="article"]//p/text()').extract())
        content = re.sub(r'\u3000', '', content)
        content = re.sub(r'[ \xa0?]+', ' ', content)
        content = re.sub(r'\s*\n\s*', '\n', content)
        content = re.sub(r'\s*(\s)', r'\1', content)
        content = ''.join([x.strip() for x in content])

        # content_list = response.xpath('//*[@id="artibody" or @id="article"]//p/text()').extract()
        # content = r""
        # for part in content_list:
        #     part = part.strip()
        #     content += part

        item['content'] = content
        yield item




