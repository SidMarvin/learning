#pip install mysql-connector-python

import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
  host="192.168.1.36",
  user="user_1",
  password="12345",
  database="test_db"
)

print("Соединение успешно установлено")

# Создание курсора
mycursor = mydb.cursor()

# Данные для вставки
customers_data = [
    ("Иван Иванов", "Улица 1, дом 1"),
    ("Петр Петров", "Улица 2, дом 2"),
    ("Сидор Сидоров", "Улица 3, дом 3"),
    ("Алексей Алексеева", "Улица 4, дом 4"),
    ("Мария Мариева", "Улица 5, дом 5"),
    ("Елена Еленова", "Улица 6, дом 6")
]

# SQL-запрос для вставки данных
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

# Выполнение запроса для каждой строки данных
mycursor.executemany(sql, customers_data)

# Подтверждение изменений в базе данных
mydb.commit()

print(mycursor.rowcount, "записей вставлено.")

# Закрытие курсора и соединения
mycursor.close()
mydb.close()


"""
#получаем значения из БД
# Создание курсора
cursor = mydb.cursor()
# SQL-запрос для выборки данных из таблицы customers
query = "SELECT * FROM customers"
# Выполнение запроса
cursor.execute(query)
# Получение всех результатов
results = cursor.fetchall()
# Обработка и вывод результатов
for row in results:
    print(row)
# Закрытие курсора и соединения
cursor.close()
mydb.close()
"""

"""
# Создание курсора для выполнения запросов
cursor = mydb.cursor()

# Выполнение запроса для получения списка таблиц
cursor.execute("SHOW TABLES")

# Получение и вывод всех таблиц
tables = cursor.fetchall()
for table in tables:
    print(table[0])  # table[0] содержит имя таблицы

# Закрытие курсора и соединения
cursor.close()
mydb.close()
"""


"""
#создаем и вставляем данные в таблицу
# Создание таблицы
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Вставка данных в таблицу
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()"""