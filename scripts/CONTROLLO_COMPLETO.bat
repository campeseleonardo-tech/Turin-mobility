@echo off
rem CONTROLLO_COMPLETO.bat - gli stessi passi del controllo di GitHub (.github\workflows\controllo.yml), in locale, nello stesso ordine.
rem Doppio clic. Alla fine di ogni giro: se qui e' tutto verde, lo e' anche su GitHub. Log in logs\controllo_completo.log
cd /d "%~dp0.."
if not exist logs mkdir logs
python scripts\controllo_completo.py > logs\controllo_completo.log 2>&1
type logs\controllo_completo.log
if errorlevel 1 (
  echo.
  echo ATTENZIONE: ci sono passi rossi, vedi sopra.
)
pause
