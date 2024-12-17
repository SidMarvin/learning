#pip install pyodbc

import pyodbc

# Параметры подключения
server = '192.168.1.36'  # Например, 'localhost' или '192.168.1.1'
database = 'user_db_1'  # Название вашей базы данных
username = 'user_1'  # Имя пользователя
password = '12345'  # Пароль

# Строка подключения
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Подключение к базе данных
    conn = pyodbc.connect(connectionString) 
    print("Подключение успешно!")

    # Создание курсора для выполнения запросов
    cursor = connection.cursor()

    # Пример выполнения запроса
    cursor.execute("SELECT * FROM your_table")  # Замените your_table на имя вашей таблицы
    rows = cursor.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print(f"Ошибка подключения: {e}")

finally:
    # Закрытие подключения
    if 'connection' in locals():
        connection.close()
        print("Соединение закрыто.")