class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com']

    # Definir la salida como archivo JSON
    custom_settings = {
      'FEED_URI' : 'output.json',
      'FEED_FORMAT' : 'json',
    }