import scrapy

class MySpider(scrapy.Spider):
    name = 'cloudspider'
    start_urls = ['http://quotes.toscrape.com/']

    # Definir la salida como archivo JSON
    custom_settings = {
      'FEED_URI' : 'output.json',
      'FEED_FORMAT' : 'json',
    }