import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://www.sapuyes-narino.gov.co/']

    def parse(self, response):
        # Extraer enlaces
        for link in response.css('a::attr(href)').getall():
            yield scrapy.Request(response.urljoin(link), callback=self.parse)

        # Extraer contenidos de formulario
        for form in response.css('form'):
            yield {
                'action': form.css('::attr(action)').get(),
                'method': form.css('::attr(method)').get(),
                'inputs': form.css('input::attr(name)').getall(),
            }
            
class TextWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = str(item) + "\n"
        self.file.write(line)
        return item