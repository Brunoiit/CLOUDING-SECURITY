import scrapy
from securityapp.xsscraping import xsscraping_process
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from django.shortcuts import render
from validators import url as validate_url
from twisted.internet import reactor, defer
from twisted.internet.protocol import ProcessProtocol
import sys

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

class ScrapingProtocol(ProcessProtocol):
    def __init__(self, deferred):
        self.deferred = deferred

    def processEnded(self, reason):
        self.deferred.callback(None)

def run_spider(url):
    deferred = defer.Deferred()
    configure_logging()
    runner = CrawlerRunner()
    d = runner.crawl(MySpider, url=url)
    d.addBoth(lambda _: reactor.stop())
    reactor.spawnProcess(ScrapingProtocol(deferred), sys.executable, ['scrapy', 'crawl', 'myspider'])
    return deferred

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
        deferred = run_spider(url)
        deferred.addBoth(lambda _: render(request, 'results.html', {'xss_results': xsscraping_result}))

        return deferred

    return render(request, 'scrape.html')
