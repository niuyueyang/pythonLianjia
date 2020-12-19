# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LianjiaHomePipeline:
    index = 0
    file = None
    def open_spider(self, spider):
        # 以追加的方式打开文件
        self.file = open("home.csv", "a", encoding="utf-8")
        pass

    def process_item(self, item, spider):
        # 第一行写入列名
        if (self.index == 0) :
            column_name="名称,户型,面积,朝向,是否装修,有无电梯,总价,单价,产权信息\n"
            # 将字符串写入文件中
            self.file.write(column_name)
            self.index = 1
        # 获取item中各个字段，将其连接成一个字符串
        home_str = item['name']+","+ \
                   item['type'] + "," + \
                   item['area'] + "," + \
                   item['direction'] + "," + \
                   item['fitment'] + "," + \
                   item['elevator'] + "," + \
                   item['total_price'] + "," + \
                   item['unit_price'] + "," + \
                   item['property'] + "\n"
        # 将字符串写入文件中
        self.file.write(home_str)
        return item

    def close_spider(self, spider):
        # 关闭文件
        self.file.close()
        pass
