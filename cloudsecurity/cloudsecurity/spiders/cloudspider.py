import scrapy


class CloudSpider(scrapy.Spider):
    name = 'cloudspider'

    def start_requests(self):
        url = input('Ingresa la URL a escanear: ')
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Aquí se procesa la respuesta de la URL ingresada

        # Obtener los enlaces de las páginas internas del sitio web
        internal_links = response.css('a::attr(href)').getall()

        # Recorrer los enlaces y generar solicitudes (requests) para cada página interna
        for link in internal_links:
            yield response.follow(url=link, callback=self.parse)

        # Aquí puedes escribir la lógica para extraer datos de la página actual
        # Utiliza selectores CSS o XPath para seleccionar elementos y extraer información

        # Ejemplo de extracción de datos utilizando selectores CSS
        title = response.css('h1::text').get()
        description = response.css('p::text').get()

        # Otra forma de extraer datos utilizando XPath
        # title = response.xpath('//h1/text()').get()
        # description = response.xpath('//p/text()').get()

        # Puedes hacer lo que quieras con los datos extraídos, como imprimirlos o almacenarlos en un archivo

        # Por ejemplo, imprimir los datos extraídos
        print('Título:', title)
        print('Descripción:', description)
