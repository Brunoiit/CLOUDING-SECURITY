import scrapy

class WebSpider(scrapy.Spider):
    name = 'cloudspider'
    start_urls = ['http://www.sapuyes-narino.gov.co/']  # Replace with your target URL

    def parse(self, response):
        # Extract URLs from the current page
        urls = response.css('a::attr(href)').getall()

        # Yield a new Request for each URL
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

class MySpider(scrapy.Spider):
    name = "my_spider"

    def start_requests(self):
        with open('urls.txt', 'r') as f:
            urls = f.read().splitlines()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)