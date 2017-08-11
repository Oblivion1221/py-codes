# Spider
@shiyanlou.com Python爬虫 尝试Scrapy框架

--------------------------------------


使用Scrapy爬虫框架：

Item用于储存爬取到的数据

在items.py中初始化item时用scrapy.Field()

Spider是爬虫的主体程序 应具有三个要素

name 用于区分Spider start_urls 是个列表 表示要爬取的url 
parse()用于分析url下载的信息 提取 作为items 其实这里不用加[0]和.strip() 一样运行（可能是因为没有空白符吧）
    # item['name'] = course.xpath('a/div[3]/span[1]/text()').extract()


Pipelines是对爬到结果进行分析提取的程序 主要用了正则表达式提取人数 并用utf-8对items里的内容编码 原始爬取到的内容是unicode编码（因为extract()）

Scrapy的模块化真的很不错 比我一年多之前用urllib库写爬虫简单多了【而且那次最后还失败了

help from shiyanlou.com
