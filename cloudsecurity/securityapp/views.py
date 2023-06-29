from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from xsscrapy import Xsscrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import validators

@csrf_exempt
def scrape(request):
    if request.method == 'POST':
        url = request.POST.get('Url')

        # Validar si el enlace ingresado es válido
        if not validators.url(url):
            error_message = 'URL inválida. Por favor, ingresa una URL válida.'
            return render(request, 'scraping_app/scrape.html', {'error_message': error_message})

        # Ejecutar XSSCRAPY para detectar vulnerabilidades de SQL injection
        xsscrapy = Xsscrapy()
        vulnerabilities = xsscrapy.run(url)

        # Ejecutar Scrapy para escanear de forma recursiva los contenidos del sitio web
        process = CrawlerProcess(get_project_settings())
        spider_name = 'your_spider_name'  # Reemplaza 'your_spider_name' con el nombre de tu araña en Scrapy

        # Definir las opciones de configuración para Scrapy (si es necesario)
        # settings = {
        #     'OPTION_NAME': 'OPTION_VALUE',
        # }

        # Pasar las opciones de configuración a Scrapy (si es necesario)
        # process = CrawlerProcess({**get_project_settings(), **settings})

        process.crawl(spider_name, start_urls=[url])
        process.start()

        # Obtener los resultados de Scrapy
        # results = process.spider_results

        context = {
            'vulnerabilities': vulnerabilities,
            # 'results': results,
        }

        return render(request, 'scraping_app/results.html', context)

    return render(request, 'scraping_app/scrape.html')