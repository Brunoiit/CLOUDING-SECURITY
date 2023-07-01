import scrapy
from cloudsecurity.spiders.xsscrapy import XSSSpider

class CloudSpider(XSSSpider):
    name = 'cloudspider'

    def start_requests(self):
        # Obtener la URL proporcionada por el usuario
        url = input("Ingrese la URL a escrapear: ")
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extraer enlaces
        for link in response.css('a::attr(href)').getall():
            yield {
                'tag': 'a',
                'href': link,
                'html': response.css('a[href="' + link + '"]').get(),
            }

        # Extraer contenidos de formulario
        for form in response.css('form'):
            yield {
                'tag': 'form',
                'action': form.css('::attr(action)').get(),
                'method': form.css('::attr(method)').get(),
                'inputs': form.css('input::attr(name)').getall(),
                'html': form.get(),
            }

        # Extraer todo el HTML de la página
        yield {
            'tag': 'html',
            'html': response.body.decode('utf-8'),
        }