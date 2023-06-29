import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, url):
        self.allowed_domains = [url.split('//')[1]]
        self.start_urls = [url]

    def parse(self, response):
        # Extrae los elementos deseados de la página actual
        title = response.xpath('//title/text()').get()
        url = response.url

        # Realiza acciones con los datos extraídos
        # ...

        # Encuentra enlaces adicionales y realiza un escaneo recursivo en ellos
        for link in response.xpath('//a/@href').getall():
            yield response.follow(link, callback=self.parse)

def run_spider(url):
    process = CrawlerProcess()
    process.crawl(MySpider, url=url)
    process.start()