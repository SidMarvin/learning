#создание окна на tkinter и визуализация в Treeview

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

# Создание окна
root = tk.Tk()
root.title("Customers Data")

# Создание Treeview для отображения данных
tree = ttk.Treeview(root)
tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Получение данных из таблицы customers
cursor = mydb.cursor()
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

# Получение названий столбцов
column_names = [i[0] for i in cursor.description]
tree["columns"] = column_names
tree["show"] = "headings"  # Скрыть первый столбец (пустой)

# Настройка столбцов
for col in column_names:
    tree.heading(col, text=col)  # Названия столбцов
    tree.column(col, anchor="center")

# Добавление данных в Treeview
for row in rows:
    tree.insert("", "end", values=row)

# Закрытие курсора
cursor.close()

# Запуск основного цикла
root.mainloop()

# Закрытие соединения с базой данных
mydb.close()