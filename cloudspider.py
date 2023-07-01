import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://www.sapuyes-narino.gov.co/']  # Inserte la URL que desea analizar

    def parse(self, response):
        # Procesa la respuesta de la página
        self.log('Visitado %s' % response.url)

        # Guardar la URL en un archivo
        with open('urls.txt', 'a') as f:
            f.write(response.url + '\n')

        # Seguir enlaces a otras páginas
        for href in response.css('a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), self.parse)