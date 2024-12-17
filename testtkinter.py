from tkinter import * 
from tkinter import messagebox
from tkinter import ttk     # подключаем пакет ttk

#окно
window = Tk() 
window.title("Описание")
window.geometry("500x500")
window.resizable(False, False)
window.mainloop()

"""
Упаковщики
pack предназначается для работы с контейнерами для элементов. С помощью него можно позиционировать содержимое контейнеров.
place нужен для размещения объектов с помощью координат.
grid размещает элементы в соответствии с ячейками сетки, разделяющей окно приложения. grid(row=50, column=2)
"""

#фрейм, который организует виджеты в группы
frame = Frame(window, padx=10, pady=10) 
frame.pack(expand=True) #expand=True указывается, что виджет заполняет весь контейнер, выделенный для него.
frame.pack(fill=Y) #fill, заставляющее виджет заполнять все доступное пространство

###виджеты
#Button: кнопка
btn = Button(text="Click", command=lambda: funktion()) # создаем кнопку из пакета tkinter
btn = ttk.Button(text="Click") # создаем кнопку из пакета ttk
btn.pack()

#Label: текстовая метка
python_logo = PhotoImage(file="./python_logo.png")
label = ttk.Label(window, text="Hello METANIT.COM", font=("Arial", 14), width=20, height=10, image=python_logo)
label.pack()

#Entry: однострочное текстовое поле
ttk.Entry().pack(anchor=NW, padx=8, pady= 8)

#Text: многострочное текстовое поле
editor = Text()
editor.pack(fill=BOTH, expand=1)

#Checkbutton: флажок
enabled = IntVar()

enabled_checkbutton = ttk.Checkbutton(text="Включить", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)
  
enabled_label = ttk.Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)

#Radiobutton: переключатель или радиокнопка
position = {"padx":6, "pady":6, "anchor":NW}
 
python = "Python"
java = "Java"
javascript = "JavaScript"
 
lang = StringVar(value=java)    # по умолчанию будет выбран элемент с value=java
 
header = ttk.Label(textvariable=lang)
header.pack(**position)
  
python_btn = ttk.Radiobutton(text=python, value=python, variable=lang)
python_btn.pack(**position)
  
javascript_btn = ttk.Radiobutton(text=javascript, value=javascript, variable=lang)
javascript_btn.pack(**position)
 
java_btn = ttk.Radiobutton(text=java, value=java, variable=lang)
java_btn.pack(**position)

#Listbox: список
languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)
languages_listbox = Listbox(listvariable=languages_var)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

#Combobox: выпадающий список
from tkinter.ttk import Combobox 
languages = ["Python", "C#", "Java", "JavaScript"]
combobox = ttk.Combobox(values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)


#Menu: элемент меню
main_menu = Menu()
 
file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")
 
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")
 
root.config(menu=main_menu)

#Scrollbar: полоса прокрутки
languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
  
scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)


#Treeview: позволяет создавать древовидные и табличные элементы
# определяем данные для отображения
people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
 
# определяем столбцы
columns = ("name", "age", "email")
 
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
 
# определяем заголовки
tree.heading("name", text="Имя")
tree.heading("age", text="Возраст")
tree.heading("email", text="Email")
 
# добавляем данные
for person in people:
    tree.insert("", END, values=person)


#Scale: текстовая метка
verticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
verticalScale.pack()
 
horizontalScale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)
horizontalScale.pack()

#Spinbox: список значений со стрелками для перемещения по элементам
spinbox = ttk.Spinbox(from_=1.0, to=100.0)
spinbox.pack(anchor=NW)

#Progressbar: текстовая метка
value_var = IntVar(value=30)
 
progressbar =  ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)
 
label = ttk.Label(textvariable=value_var)
label.pack(anchor=NW, padx=6, pady=6)
 

#Canvas: текстовая метка

#Notebook: вкладки
# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
 
# создаем пару фреймвов
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
 
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
 
# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Python")
notebook.add(frame2, text="Java")
 
root.mainloop()
