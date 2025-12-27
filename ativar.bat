@echo off
echo ======================================
echo   ATIVANDO AMBIENTE VIRTUAL
echo ======================================
echo.

REM Verificar se venv existe
if not exist "venv\Scripts\activate.bat" (
    echo ERRO: Ambiente virtual nao encontrado!
    echo Execute setup.bat primeiro
    pause
    exit
)

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

echo Ambiente virtual ATIVADO!
echo.
echo Agora instale as dependencias:
echo   pip install -r requirements.txt
echo.
echo Para executar o projeto:
echo   python src\interface.py
echo.
echo Para desativar:
echo   deactivate
echo.
cmd /k