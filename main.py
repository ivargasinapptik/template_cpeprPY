# main.py
from tkinter import *
from tkinter import messagebox
from db import verificar_login

def abrir_ventana_base():
    ventana_base = Toplevel()
    ventana_base.title("Panel Principal")
    ventana_base.geometry("400x200")
    Label(ventana_base, text="¡Bienvenido al sistema del colegio!").pack(pady=20)

def login():
    email = entry_email.get()
    password = entry_password.get()

    resultado = verificar_login(email, password)

    if resultado == "login_exitoso":
        messagebox.showinfo("Éxito", "Login exitoso")
        root.withdraw()
        abrir_ventana_base()
    elif resultado == "no_admin":
        messagebox.showerror("Acceso denegado", "No tiene permisos de administrador")
    elif resultado == "password_incorrecto":
        messagebox.showerror("Error", "Contraseña incorrecta")
    elif resultado == "email_invalido":
        messagebox.showerror("Error", "El correo no está registrado")

# GUI Login
root = Tk()
root.title("Login - Colegio")
root.geometry("300x200")

Label(root, text="Email").pack(pady=5)
entry_email = Entry(root, width=30)
entry_email.pack()

Label(root, text="Contraseña").pack(pady=5)
entry_password = Entry(root, width=30, show="*")
entry_password.pack()

Button(root, text="Iniciar sesión", command=login).pack(pady=20)

root.mainloop()
