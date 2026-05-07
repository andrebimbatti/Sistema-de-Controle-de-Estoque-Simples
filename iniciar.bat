@echo off
:: Muda o diretório de trabalho para a pasta onde o .bat está
cd /d "%~dp0"

echo Executando script na pasta: %cd%

:: Executa o arquivo .py que deve estar na mesma pasta
python "main.py"

pause