# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import requests

class QuanzhanPipeline:
    path = 'D:\Download\Dldpic'
    def creatPath(self,path):
        if not os.path.exists(path):
            print("Creat path: " + path)
            os.makedirs(path)

    def open_spider(self,spider):
        print('start...')
        self.creatPath(self.path)

    def process_item(self, item, spider):


        fp = open(self.path+'\\' + item['img_data']['title'] + '.jpg','wb')
        content = requests.get(item['img_data']['src']).content
        fp.write(content)

        return item
    def close_spider(self,spider):
        print('end...')