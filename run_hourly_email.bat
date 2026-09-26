@echo off
REM Переходим в папку со скриптом
cd /d "%~dp0"

REM Запускаем Python-скрипт
python hourly_email_sender.py

REM Пауза, чтобы окно не закрывалось сразу, если возникнет ошибка
pause