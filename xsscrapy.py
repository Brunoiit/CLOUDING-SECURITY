class MySpider(scrapy.Spider):
    name = "my_spider"

    def start_requests(self):
        with open('urls.txt', 'r') as f:
            urls = f.read().splitlines()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
