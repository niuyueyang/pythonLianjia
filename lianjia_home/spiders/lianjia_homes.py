import scrapy
from lianjia_home.items import LianjiaHomeItem


class LianjiaHomesSpider(scrapy.Spider):
    name = 'lianjia_homes'
    current_page = 1

    def start_requests(self):
        url = 'https://su.lianjia.com/ershoufang/'
        yield scrapy.Request(url)
        pass

    def parse(self, response):
        # li_selector = response.xpath('//div[@class="leftContent"]//ul[@class="sellListContent"]/li')
        li_selector = response.css('.sellListContent>.LOGCLICKDATA')
        for one_selector in li_selector:
            item = LianjiaHomeItem()  # 生成对象
            name = one_selector.css('.title>a::text').extract_first()
            other = one_selector.css('.address>.houseInfo::text').extract_first().split('|')
            item['name'] = name # 房屋名称
            types = other[0].strip(' ') #类型
            item['type'] = types
            item['area'] = other[1].strip(' ') #面积
            item['direction'] = other[2].strip(' ') #方向
            item['fitment'] = other[3].strip(' ') #是否装修
            item['elevator'] = other[4].strip(' ') #有无电梯
            total_price = one_selector.xpath('.//div[@class="info clear"]//div[@class="priceInfo"]//div[@class="totalPrice"]//span/text()').extract_first()
            item['total_price'] = total_price #总价
            unit_price = one_selector.xpath('.//div[@class="info clear"]//div[@class="priceInfo"]//div[@class="unitPrice"]/@data-price').extract_first()
            item['unit_price'] = unit_price #单价

            # 获取房屋详细信息
            url = one_selector.xpath('.//div[@class="title"]/a/@href').extract_first()

            #生成详情页面请求对象
            yield scrapy.Request(url, meta={"item": item}, callback=self.property_parse)
            yield item

        next_url = response.xpath("//div[@class='page-box fr']//div[@class='page-box house-lst-page-box']/@page-data").extract_first().strip(' ')
        current_page = int(eval(next_url)["curPage"])
        total_page = int(eval(next_url)["totalPage"])
        if (current_page < total_page):
            self.current_page += 1
            print(self.current_page)
            next_urls = "https://su.lianjia.com/ershoufang/pg"+str(self.current_page)+"/"
            print(next_urls)
            yield scrapy.Request(
                next_urls,
                callback=self.parse
            )
        pass

    # 详情页面解析
    def property_parse(self, response):
        # 获取产权信息
        property = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[6]/span[2]/text()").extract_first()
        # 获取主页房屋信息
        item = response.meta["item"]
        #将产权信息添加到item中，返回给引擎
        item["property"] = property
        yield item
