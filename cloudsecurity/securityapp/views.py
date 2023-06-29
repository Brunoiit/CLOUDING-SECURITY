import scrapy
from securityapp.xsscraping import xsscraping_process
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from django.shortcuts import render
from validators import url as validate_url
from twisted.internet import reactor, defer

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

@defer.inlineCallbacks
def run_spider(url):
    runner = CrawlerRunner()
    yield runner.crawl(MySpider, url=url)
    reactor.stop()

def scrape(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # Validar la URL
        if not validate_url(url):
            error_message = 'La URL ingresada no es válida.'
            return render(request, 'scrape.html', {'error_message': error_message})

        # Realizar el proceso de Xsscraping utilizando la URL proporcionada
        xsscraping_result = xsscraping_process(url)

        # Realizar el proceso de Scrapy utilizando la URL proporcionada
        configure_logging()
        reactor.callFromThread(run_spider, url)
        reactor.run()

        # Renderizar la página de resultados
        return render(request, 'results.html', {'xss_results': xsscraping_result})

    return render(request, 'scrape.html')