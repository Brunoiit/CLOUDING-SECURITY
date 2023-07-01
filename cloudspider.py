import os
import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor


class CloudSpider(scrapy.Spider):
    name = "cloudspider"
    allowed_domains = []
    start_urls = []
    results = []

    def parse(self, response):
        # Obtener los enlaces de la página actual
        le = LinkExtractor()
        links = le.extract_links(response)

        # Agregar los enlaces encontrados a los resultados
        for link in links:
            self.results.append(link.url)

    def export_results(self):
        # Mostrar los resultados en la consola
        for result in self.results:
            print(result)


def start_scraping(urls):
    if urls:
        # Crear instancia del proceso de Scrapy
        process = CrawlerProcess()

        # Configurar la araña y las URLs de inicio
        spider = CloudSpider()
        spider.start_urls = urls

        # Agregar la araña al proceso
        process.crawl(spider)

        # Iniciar el proceso
        process.start()
    else:
        print("No se han proporcionado URLs. Por favor, ingrese al menos una URL válida.")


# Obtener las URLs pasadas como argumentos desde la línea de comandos
urls = sys.argv[1:]

# Iniciar el escaneo con las URLs proporcionadas
start_scraping(urls)