import scrapy
from zt.items import DmozItem
class Dmozspider(scrapy.Spider):
	"""docstring for Dmozspider"""
	name="dmoz"#唯一标识
	allowed_domains=['dmoztools.net']#范围
	start_urls=['http://dmoztools.net/Computers/Programming/Languages/Python/Resources/','http://dmoztools.net/Computers/Programming/Languages/Python/Books/']

	def parse(self, response):
		sel=scrapy.selector.Selector(response)
		sites=sel.xpath('//div[@class="site-title"]')
		items=[]
		for site in sites:
			item= DmozItem()
			item['title']=site.xpath('text()').extract()
			item['link']=site.xpath('@href').extract()
			item['desc']=site.xpath('text()').extract()
			items.append(item)

		return items