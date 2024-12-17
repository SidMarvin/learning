@echo off
echo Установка библиотек Python...

python -m pip install --upgrade pip
python -m pip install openai
python -m pip install tkinter
python -m pip install pyodbc
python -m pip install mysql-connector-python
python -m pip install pytest
python -m pip install sqlalchemy

echo Установка завершена.
pause
