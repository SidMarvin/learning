# аутенфикация и регистрация нового пользователя
 
import tkinter as tk
from tkinter import messagebox

# Словарь для хранения пользователей и их ролей
users = {
    "admin": ("admin_password", "Администратор"),
    "user": ("user_password", "Пользователь")
}

def admin_window():
    win = tk.Tk()
    win.title("Панель администратора")
    win.geometry("800x650")
    win.resizable(False, False)
    win.mainloop()
    
def user_window():
    win = tk.Tk()
    win.title("Панель пользователя")
    win.geometry("800x650")
    win.resizable(False, False)
    win.mainloop()

def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username][0] == password:
        role = users[username][1]
        messagebox.showinfo("Успех", f"Добро пожаловать, {role}!")
        root.destroy()  # Закрытие окна после успешного входа
        if role == "Администратор":
            admin_window()
        elif role == "Пользователь":
            user_window()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

def register():
    def create_user():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()
        new_role = entry_new_role.get()

        if new_username in users:
            messagebox.showerror("Ошибка", "Пользователь уже существует")
        else:
            users[new_username] = (new_password, new_role)
            messagebox.showinfo("Успех", "Пользователь зарегистрирован!")
            registration_window.destroy()

    registration_window = tk.Toplevel(root)
    registration_window.title("Регистрация")

    tk.Label(registration_window, text="Логин:").pack()
    entry_new_username = tk.Entry(registration_window)
    entry_new_username.pack()

    tk.Label(registration_window, text="Пароль:").pack()
    entry_new_password = tk.Entry(registration_window, show='*')
    entry_new_password.pack()

    tk.Label(registration_window, text="Роль:").pack()
    entry_new_role = tk.Entry(registration_window)
    entry_new_role.pack()

    tk.Button(registration_window, text="Создать аккаунт", command=create_user).pack()

# Основное окно
root = tk.Tk()
root.title("Аутентификация")

tk.Label(root, text="Логин:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Пароль:").pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

tk.Button(root, text="Войти", command=authenticate).pack()
tk.Button(root, text="Регистрация", command=register).pack()

root.mainloop()