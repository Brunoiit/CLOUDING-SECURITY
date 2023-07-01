import scrapy

class XsMySpider(scrapy.Spider):
  name = 'cloudspider'
  start_urls = ['http://quotes.toscrape.com/']

  # Definir la salida como archivo JSON
  custom_settings = {
    'FEED_URI' : 'output.json',
    'FEED_FORMAT' : 'json',
  }
  
  def parse(self, response):
    yield {
      'title': response.css('title::text').get()
    }
