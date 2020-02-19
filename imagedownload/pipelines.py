# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline




class ImagedownloadPipeline(FilesPipeline):


    # def process_item(self, item, spider):
    #     return item

    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1].split('?')[0]
        return file_name


    # def get_media_requests(self, item, info):
    #     file_url = item['image_url']
    #     meta = {'filename': item['name']}
    #     yield Request(url=file_url, meta=meta)

    # def get_media_requests(self, item, info):
    #     return [Request(x, meta={'image_name': item["image_name"]})
    #             for x in item.get('image_urls', [])]

    # def file_path(self, request, response=None, info=None):
    #     return '%s.jpg' % request.meta['image_name']

    # def file_path(self, request, response=None, info=None):
    #     original_path = super(ImagedownloadPipeline, self).file_path(request, response=None, info=None)
    #     # sha1_and_extension = original_path.split('/')[1] # delete 'full/' from the path
    #     return request.meta.get('filename','') + "_ddd"

    # # def file_path(self, request, response=None, info=None):
    # #     return request.meta.get('filename','')

    # def get_media_requests(self, item, info):
    #     file_url = item['file_url']
    #     meta = {'filename': item['SKU']}
    #     yield Request(url=file_url, meta=meta)