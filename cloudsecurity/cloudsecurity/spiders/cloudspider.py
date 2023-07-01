import scrapy
from cloudsecurity.spiders.xsscrapy import XSSSpider

class CloudSpider(XSSSpider):
    name = 'cloudspider'

    def start_requests(self):
        # Obtener la URL proporcionada por el usuario
        url = input("Ingrese la URL a escrapear: ")
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extraer enlaces
        for link in response.css('a::attr(href)').getall():
            yield {
                'tag': 'a',
                'href': link,
                'html': response.css('a[href="' + link + '"]').get(),
            }

        # Extraer contenidos de formulario
        for form in response.css('form'):
            yield {
                'tag': 'form',
                'action': form.css('::attr(action)').get(),
                'method': form.css('::attr(method)').get(),
                'inputs': form.css('input::attr(name)').getall(),
                'html': form.get(),
            }

        # Extraer todo el HTML de la página
        html = response.body.decode('utf-8')
        formatted_html = self.format_html(html)
        yield {
            'tag': 'html',
            'html': formatted_html,
        }

    def format_html(self, html):
        # Organizar el HTML en múltiples líneas para mayor legibilidad
        lines = []
        indent_level = 0
        for char in html:
            if char == '<':
                lines.append('\t' * indent_level + char)
                indent_level += 1
            elif char == '>':
                indent_level -= 1
                lines[-1] += char
                if lines[-1].startswith('</'):
                    lines[-1] += '\n'
            elif char == '\n':
                pass
            else:
                if not lines[-1].endswith('\n'):
                    lines[-1] += '\n'
                lines.append('\t' * indent_level + char)

        formatted_html = ''.join(lines)
        return formatted_html
