import os
import tkinter as tk
from tkinter import filedialog, messagebox
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor


class CloudSpider(scrapy.Spider):
    name = "cloudspider"
    allowed_domains = []
    start_urls = []
    results = []

    def parse(self, response):
        # Obtener los enlaces de la página actual
        le = LinkExtractor()
        links = le.extract_links(response)

        # Agregar los enlaces encontrados a los resultados
        for link in links:
            self.results.append(link.url)

    def export_results(self, output_path):
        # Guardar los resultados en un archivo de texto
        with open(output_path, 'w') as file:
            for result in self.results:
                file.write(result + '\n')


def start_scraping():
    url = url_entry.get()

    if url:
        # Obtener la ruta del archivo de salida
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=os.path.expanduser("~/Desktop"))

        if output_file:
            # Crear instancia del proceso de Scrapy
            process = CrawlerProcess(settings={
                "FEEDS": {output_file: {"format": "jsonlines"}},
            })

            # Agregar la araña al proceso
            process.crawl(CloudSpider, start_urls=[url])

            # Iniciar el proceso
            process.start()

            # Obtener el objeto spider
            spider = process.spider

            # Exportar los resultados
            spider.export_results(output_file)

            # Mostrar mensaje de finalización
            messagebox.showinfo("Finalizado", "El escaneo ha sido completado. Los resultados se han guardado en {}".format(output_file))
        else:
            messagebox.showwarning("Ruta de salida no seleccionada", "No se ha seleccionado una ruta de salida.")
    else:
        messagebox.showwarning("URL Vacía", "Por favor, ingresa una URL válida.")


# Crear la ventana principal
window = tk.Tk()
window.title("Cloud Security Scanner")

# Crear y posicionar los elementos de la interfaz
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

start_button = tk.Button(window, text="Iniciar escaneo", command=start_scraping)
start_button.pack()

# Ejecutar la ventana principal
window.mainloop()