import scrapy


class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://goodreads.com/book/show/2203.John_Adams']

    def parse(self, response):
        book_details = response.css(".mainContentContainer")
        for book in book_details:
            book_name = book.css("#bookTitle::text").get()
            book_rating = book.css("#bookMeta span::text").get()
            author_name = book.css (".authorName span::text").get()
            book_name = book_name.strip()
            book_rating = book_rating.strip()
            author_name = author_name.strip()
            yield {"Book Name:": book_name,
                   "Rating:": book_rating,
                   "Author:": author_name}
        links = response.css(".cover a::attr(href)").getall()
        for link in links:
            yield scrapy.Request(link, callback=self.parse)

