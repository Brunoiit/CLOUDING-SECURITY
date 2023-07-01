import os
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


def start_scraping():
    url = input("Ingrese la URL: ")

    if url:
        # Crear instancia del proceso de Scrapy
        process = CrawlerProcess()

        # Agregar la araña al proceso
        process.crawl(CloudSpider, start_urls=[url])

        # Iniciar el proceso
        process.start()

        # Obtener el objeto spider
        spider = process.spider_loader.load("cloudspider")

        # Exportar los resultados
        spider.export_results()
    else:
        print("URL vacía. Por favor, ingrese una URL válida.")


# Iniciar el escaneo
start_scraping()