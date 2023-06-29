from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .xsscraping import XXScrapyScraper, SQLInjectionScraper
from .forms import ScrapeForm
import validators

@csrf_exempt
def scrape(request):
    if request.method == 'POST':
        form = ScrapeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            # Validar que la URL sea válida
            if not validators.url(url):
                error_message = "La URL ingresada no es válida."
                return render(request, 'scrape.html', {'form': form, 'error_message': error_message})

            # Realizar el scraping
            xx_scrapy_scraper = XXScrapyScraper()
            xx_results = xx_scrapy_scraper.scrape(url)

            sql_injection_scraper = SQLInjectionScraper()
            sql_injection_results = sql_injection_scraper.scrape(url)

            context = {
                'xx_results': xx_results,
                'sql_injection_results': sql_injection_results
            }
            return render(request, 'results.html', context)
    else:
        form = ScrapeForm()

    context = {
        'form': form
    }
    return render(request, 'scrape.html', context)