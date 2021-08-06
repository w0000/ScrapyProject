import scrapy
from Pro1.items import Pro1Item

class FirstSpider(scrapy.Spider):
    name = 'first'
    #allowed_domains = ['https://movie.douban.com/']
    start_urls = ['https://movie.douban.com/subject/30174085/?from=showing']
    # def parse(self, response):
    #     all_data = []
    #     #xpath返回的时列表，列表元素是Selector类型的对象
    #     div_list = response.xpath('//div[@class="comment"]')
    #     for div in div_list:
    #         # extract可以将Selector对象中data参数存储的字符串提取出来
    #         name = div.xpath('./h3/span[@class="comment-info"]/a/text()')[0].extract()
    #         #Selector列表调用extract后，表示将每个Selector对象中data数据取出，返回也是列表
    #         content = div.xpath('./p/span/text()').extract()
    #         #当列表中只有一个元素 content = div.xpath('./p/span/text()').extract_first()相当于[0].extract().
    #         content = ''.join(content)
    #         print(name + ":" + content)
    #         dic = {
    #             'name' : name,
    #             'content' : content
    #         }
    #         all_data.append(dic)
    #     return all_data
    def parse(self, response):
        all_data = []
        #xpath返回的时列表，列表元素是Selector类型的对象
        div_list = response.xpath('//div[@class="comment"]')
        for div in div_list:
            # extract可以将Selector对象中data参数存储的字符串提取出来
            name = div.xpath('./h3/span[@class="comment-info"]/a/text()')[0].extract()
            #Selector列表调用extract后，表示将每个Selector对象中data数据取出，返回也是列表
            content = div.xpath('./p/span/text()').extract()
            #当列表中只有一个元素 content = div.xpath('./p/span/text()').extract_first()相当于[0].extract().
            content = ''.join(content)
            item = Pro1Item()
            item['name'] = name
            item['content'] = content
            yield item#将item提交给管道