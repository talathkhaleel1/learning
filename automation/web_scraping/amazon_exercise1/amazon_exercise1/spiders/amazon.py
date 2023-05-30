# Amazon
# Create a crawler that gets all the product names, \
# ratings and prices from this page: https://www.amazon.com/s?k=kindle

import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=kindle']

    def parse(self, response):
        product_details = response.css(".s-result-item")
        for product in product_details:
            product_names = product.css(".a-color-base.a-text-normal::text").getall()
            ratings = product.css(".a-icon-alt::text").getall()
            prices = product.css(".a-price-whole::text").getall()
            yield  {"Product names: " : product_names,\
                    "Ratings: ": ratings,\
                    "Prices: ": prices}

