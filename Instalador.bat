@echo off

echo Validando la existencia de beautifulsoup4...
pip show beautifulsoup4 > nul
if %errorlevel% neq 0 (
    echo Instalando beautifulsoup4...
    pip install beautifulsoup4
) else (
    echo beautifulsoup4 ya está instalado.
)

echo Validando la existencia de XSSCRAPY...
pip show xsscrapy > nul
if %errorlevel% neq 0 (
    echo Instalando XSSCRAPY...
    pip install xsscrapy
) else (
    echo XSSCRAPY ya está instalado.
)

echo Validando la existencia de Scrapy...
pip show scrapy > nul
if %errorlevel% neq 0 (
    echo Instalando Scrapy...
    pip install scrapy
) else (
    echo Scrapy ya está instalado.
)

echo Dependencias instaladas correctamente.
echo Iniciando arañas
cd cloudsecurity
scrapy crawl cloudspider

pause