@echo off

echo Validando la existencia de Django...
pip show django > nul
if %errorlevel% neq 0 (
    echo Instalando Django...
    pip install django
) else (
    echo Django ya está instalado.
)

echo Validando la existencia de validators...
pip show validators > nul
if %errorlevel% neq 0 (
    echo Instalando validators...
    pip install validators
) else (
    echo validators ya está instalado.
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
pause