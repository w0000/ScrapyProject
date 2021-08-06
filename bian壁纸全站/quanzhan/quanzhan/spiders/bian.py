import scrapy
from quanzhan.items import QuanzhanItem


class BianSpider(scrapy.Spider):
    name = 'bian'

    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.netbian.com/weimei/index.htm']
    page_num = 1
    url = 'http://www.netbian.com/weimei/index_{0}.htm'

    def parse(self, response):
        li_list = response.xpath('//div[@class="list"]/ul/li')
        if self.page_num <= 3:
            for li in li_list:
                if len(li.xpath('./a/@href').extract()) != 0:
                    detail_url = 'http://www.netbian.com' + li.xpath('./a/@href')[0].extract()
                    print(detail_url)
                    # title = li.xpath('./a/@alt')[0].extract()
                    # print(self.url.format(self.page_num))
                    yield scrapy.Request(detail_url, callback=self.url_parse)
            self.page_num += 1
            yield scrapy.Request(self.url.format(self.page_num), callback=self.parse)

    def url_parse(self, response):
        img_src = response.xpath('//div[@class="pic"]/p/a/img/@src')[0].extract()
        print(img_src)
        title = response.xpath('//div[@class="action"]/h1/text()')[0].extract()
        item = QuanzhanItem()
        item['img_data'] = {
            'title' : title,
            'src' : img_src
        }
        print(title)
        yield item
