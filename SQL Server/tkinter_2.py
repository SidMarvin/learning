#создание окна на tkinter и визуализация при помощи label

import tkinter as tk
from tkinter import ttk
import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
    host="192.168.1.36",
    user="user_1",
    password="12345",
    database="test_db"
)

print("Соединение успешно установлено")

# Функция для получения данных из таблицы customers
def fetch_data():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM customers")
    return cursor.fetchall(), [i[0] for i in cursor.description]  # возвращаем данные и названия столбцов

# Создание основного окна
root = tk.Tk()
root.title("Данные из таблицы customers")

# Получаем данные из базы данных
data, columns = fetch_data()

# Создание меток для названий столбцов
for col in range(len(columns)):
    label = tk.Label(root, text=columns[col], font=('Arial', 12, 'bold'), borderwidth=1, relief='solid', width=18, height=1)
    label.grid(row=0, column=col)

# Создание меток для данных
for row_num, row in enumerate(data, start=1):
    for col_num, value in enumerate(row):
        label = tk.Label(root, text=value, font=('Arial', 12), borderwidth=1, relief='solid', width=20, height=1)
        label.grid(row=row_num, column=col_num)

# Запуск основного цикла
root.mainloop()

# Закрываем соединение с БД
mydb.close()