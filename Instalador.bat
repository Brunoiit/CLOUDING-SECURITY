@echo off

echo Validando la existencia de tkinter...
pip show tkinter > nul
if %errorlevel% neq 0 (
    echo Instalando tkinter...
    pip install tkinter
    @REM pip install Twisted==16.4.1
) else (
    echo requests ya está instalado.
)

echo Validando la existencia de requests...
pip show requests > nul
if %errorlevel% neq 0 (
    echo Instalando requests...
    pip install requests
) else (
    echo requests ya está instalado.
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
echo iniciando el programa.
cd .\cloudsecurity\
scrapy crawl cloudspider
pause