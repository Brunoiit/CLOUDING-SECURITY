import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    
    start_urls = ['http://example.com']  # URL de inicio para el rastreo
    
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