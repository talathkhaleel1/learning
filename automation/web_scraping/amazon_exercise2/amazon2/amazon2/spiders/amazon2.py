# Amazon 2
# Create a crawler that gets at least 5000 product names, ratings and prices from the book category

import scrapy


class Amazon2Spider(scrapy.Spider):
    name = 'amazon2'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Potter-Chamber-Secrets-MinaLima-Illustrated/dp/1338716530/ref=pd_sbs_4/143-3999652-6742566?pd_rd_w=8RlDc&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=87PX59N1HPB4Y0X1C2HT&pd_rd_r=18fb9602-2042-4d42-87bf-65f7193e8f47&pd_rd_wg=EdLEV&pd_rd_i=1338716530&psc=1']
    def parse(self, response):
        product_names = response.css("#productTitle::text").getall()
        print(product_names)
        ratings = response.css(".a-icon-alt::text").getall()
        prices = response.css(".a-price::text").getall()
        yield {"Product names: ": product_names,
               "Ratings: ": ratings,
               "Prices: ": prices}
        links = response.css(".a-carousel-card a::attr(href)").getall()
        for link in links:
            yield scrapy.Request("https://www.amazon.com" + link, callback = self.parse)