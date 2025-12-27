@echo off
echo ======================================
echo   CONFIGURADOR PROJETO REDES
echo ======================================
echo.

REM 1. Verificar se Python está instalado
python --version > nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit
)

REM 2. Criar ambiente virtual
echo Criando ambiente virtual...
python -m venv venv

REM 3. Criar arquivos necessarios
echo Criando estrutura de arquivos...

REM requirements.txt
echo psutil==5.9.5 > requirements.txt
echo speedtest-cli==2.1.3 >> requirements.txt

REM README.md
echo # Analisador de Rede - Projeto Faculdade > README.md
echo. >> README.md
echo ## Como usar: >> README.md
echo 1. Execute ativar.bat >> README.md
echo 2. Execute: python src\interface.py >> README.md

REM Criar pasta src
if not exist "src" mkdir src

echo.
echo ======================================
echo   AMBIENTE CRIADO COM SUCESSO!
echo ======================================
echo.
echo Use 'ativar.bat' para ativar o ambiente
echo Depois instale: pip install -r requirements.txt
echo.
pause