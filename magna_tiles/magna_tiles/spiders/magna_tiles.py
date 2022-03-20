import scrapy 
from ..items import MagnaTilesItem
from scrapy.loader import ItemLoader

class MagnaTiles(scrapy.Spider):

    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['https://www.magnatiles.com/products/']


    def parse(self, response):
    
        for p in response.css("ul.products li"):
            il = ItemLoader(item=MagnaTilesItem(), selector=p)

            il.add_css('sku', "a.button::attr(data-product_sku)")
            il.add_css('name', "h2")
            il.add_css('price', "span.price bdi")

            yield il.load_item()
            
        next_page = response.css("ul.page-numbers a.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)