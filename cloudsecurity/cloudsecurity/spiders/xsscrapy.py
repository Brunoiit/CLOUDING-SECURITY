class MySpider(scrapy.Spider):
    name = 'cloudspider'
    start_urls = ['http://www.sapuyes-narino.gov.co/']

    # Definir la salida como archivo JSON
    custom_settings = {
      'FEED_URI' : 'output.json',
      'FEED_FORMAT' : 'json',
    }