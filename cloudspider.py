import scrapy

class WebSpider(scrapy.Spider):
    name = 'webspider'
    start_urls = ['http://www.sapuyes-narino.gov.co/']  # Replace with your target URL

    def parse(self, response):
        self.log('Visited %s' % response.url)

        # Store visited URL to .txt file
        with open('urls.txt', 'a') as url_file:
            url_file.write(response.url + '\n')
    
        # Follow the hyperlinks on the page
        for link in response.css('a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(link), self.parse)