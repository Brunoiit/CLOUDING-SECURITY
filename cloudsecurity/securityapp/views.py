import scrapy
from scrapy.crawler import CrawlerProcess
from django.shortcuts import render
from validators import url as validate_url

class MySpider(scrapy.Spider):
    name = 'myspider'

    def __init__(self, url):
        self.allowed_domains = [url.split('//')[1]]
        self.start_urls = [url]

    def parse(self, response):
        # Realiza el procesamiento de la respuesta de la página aquí
        # ...

        # Encuentra enlaces adicionales y realiza un escaneo recursivo en ellos
        for link in response.xpath('//a/@href').getall():
            yield response.follow(link, callback=self.parse)

def run_spider(url):
    process = CrawlerProcess()
    process.crawl(MySpider, url=url)
    process.start()

def scrape(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # Validar la URL
        if not validate_url(url):
            error_message = 'La URL ingresada no es válida.'
            return render(request, 'scrape.html', {'error_message': error_message})

        # Realizar el proceso de Xsscraping utilizando la URL proporcionada
        xsscraping_result = xsscraping_process(url)
        # Hacer algo con el resultado del proceso de Xsscraping

        return render(request, 'scrape.html', {'result': xsscraping_result})

    return render(request, 'scrape.html')
